"""Load dated forward assumptions and apply them through the Campus engine."""

from dataclasses import replace
from datetime import date
import json
from math import isfinite

from campus import DEFAULT, ROOT, TICKERS, run
from operations import markdown_table

FORWARD_LABEL = "Forward assumptions — illustrative"
FORWARD_PATH = ROOT / "data/forward-assumptions.json"
RISK_NOTE = (
    "Volatility uses historical ETF covariance from the selected lookback. "
    "It is a historical risk proxy, not a forward volatility forecast."
)
HURDLE_NOTE = (
    "The case keeps 2.50% illustrative inflation plus 3 percentage points, for a 5.50% annual net screen. "
    "This arithmetic screening hurdle approximates the objective and cannot establish rolling five-year CPI + 3% achievement."
)
MONITORING_NOTE = (
    "The archived VT signal applies to the November 17 historical case. Current monitoring readiness is not established "
    "for the forward scenario. Refresh the signal and verify operational evidence before funding."
)


def load_forward(path=FORWARD_PATH):
    return json.loads(path.read_text())


def selected_returns(record, cutoff):
    """Convert sourced percent and expense basis points to annual decimal returns."""
    def check_date(label, available, measurement):
        if date.fromisoformat(available) > cutoff or (measurement and date.fromisoformat(measurement) > cutoff):
            raise ValueError(f"{label}: evidence was unavailable by {cutoff}.")

    if cutoff < date.fromisoformat(record["retrieved"]):
        raise ValueError(f"The saved forward evidence was not available in this record by {cutoff}.")
    for name, source in record["sources"].items():
        check_date(name, source["available_by"], source["as_of"])

    rates = {}
    for ticker in TICKERS:
        fund = record["funds"].get(ticker, {})
        arithmetic = fund.get("arithmetic_pct")
        expense = fund.get("expense_bp")
        if (fund.get("cma") not in record["sources"]
                or not isinstance(arithmetic, (float, int)) or not isfinite(arithmetic)
                or not isinstance(expense, (float, int)) or not isfinite(expense) or expense < 0):
            raise ValueError(f"{ticker}: forward return or expense evidence is unresolved. Forward screening is unavailable.")
        check_date(ticker, fund["fund_available_by"], fund["fund_as_of"])
        rates[ticker] = arithmetic / 100 - expense / 10_000
    return rates


def run_forward(record, inputs=DEFAULT, **kwargs):
    cutoff = date.fromisoformat(record["analysis_date"])
    result = run(inputs, cutoff=cutoff, expected_returns=selected_returns(record, cutoff), **kwargs)
    if result["mixes"].get("Constrained", {}).get("verdict") == "Passes modeled checks":
        result["action"] = ("Hold funding. Review the forward screen and refresh monitoring evidence "
                            "before acting on any allocation.")
    return result


def forward_stresses(record, **kwargs):
    cost = record["analyst_costs"]
    low, high = cost["annual_sensitivity_bp"]
    downside = cost["vt_downside_points"]
    return {
        label: run_forward(record, inputs, **kwargs)
        for label, inputs in (
            (f"VT return {downside:g} percentage points", replace(DEFAULT, vt_shift_points=downside)),
            (f"Recurring cost {low:g} bp", replace(DEFAULT, cost_bp=low)),
            (f"Recurring cost {high:g} bp", replace(DEFAULT, cost_bp=high)),
        )
    }


def forward_detail(record):
    cutoff = date.fromisoformat(record["analysis_date"])
    rates = selected_returns(record, cutoff)
    sources = record["sources"]
    bill, broker = sources["bills"], sources["broker"]
    costs = record["analyst_costs"]

    def rows():
        for ticker in TICKERS:
            fund = record["funds"][ticker]
            cma = sources[fund["cma"]]
            yield (ticker, fund["proxy"], f"{fund['arithmetic_pct']:.2f}% / {fund['geometric_pct']:.2f}%",
                   f"{fund['expense_bp']:g} bp", f"{rates[ticker]:.2%}",
                   f"[{cma['title']}]({cma['url']}) · observed {cma['as_of']} · published {cma['published']}",
                   f"[{fund['fund_title']}]({fund['fund_url']}) · reference date {fund['fund_as_of']} "
                   f"· {fund['fund_published']}", fund["rationale"])

    return "\n\n".join((
        f"**Forward source record.** Retrieved {record['retrieved']} for the {cutoff} analysis.",
        record["convention"],
        "Use the arithmetic column directly and convert percent to decimal. The geometric column is shown for context. "
        "The source forecasts are index-level proxies. Subtract the fund expense in basis points once and then "
        "deduct the portfolio-level recurring cost once. The arithmetic stress control is in percentage points.",
        markdown_table(("ETF", "Index proxy", "Arithmetic / geometric", "Fund expense", "Selected annual rate",
                        "Capital-market source", "Fund source", "Rationale and limitations"), rows()),
        f"The Treasury’s {bill['as_of']} 13-week reference is {bill['value_pct']:.2f}%. "
        f"{bill['definition']} [{bill['title']}]({bill['url']})",
        f"Schwab lists USD {broker['commission_usd']:g} per eligible online trade. "
        f"Source edition: {broker['published']}. {broker['definition']} "
        f"Zero commission still leaves spread, slippage and possible account charges. [{broker['title']}]({broker['url']})",
        costs["definition"],
        HURDLE_NOTE,
        RISK_NOTE,
        MONITORING_NOTE,
    ))
