"""Offline operational checks for the fictional Campus portfolio."""

from collections import defaultdict
from dataclasses import dataclass
from datetime import date, timedelta
import json
from math import isclose, isfinite
from pathlib import Path

ASSUMED = "Passes under stated assumptions"
VERIFIED = "Verified against dated evidence"
UNKNOWN = "Not established"
FAIL = "Fails"
EVIDENCE_PATH = Path(__file__).resolve().parent / "data/operational-evidence.json"
RULES = (
    "Scholarship payment-date cash availability",
    "Corporate issuer exposure ≤ 8% under case exemptions",
    "Illustrative rebalance turnover (approval above 25%)",
    "At least 90% redeemable within five business days",
    "Account permissions",
    "Annual review and cumulative turnover",
)


@dataclass(frozen=True)
class Assumptions:
    payment_dates: tuple = tuple(date(2027, month, 15) for month in (3, 6, 9, 12))
    opening_cash: float = 0
    starting_weights: tuple = (.60, .10, .10, .20)

    def __post_init__(self):
        dates = self.payment_dates
        if len(dates) != 4 or any(
            (following.year * 12 + following.month) - (current.year * 12 + current.month) != 3
            for current, following in zip(dates, dates[1:])
        ):
            raise ValueError("Enter four dates in successive quarter-spaced months.")
        if not isfinite(self.opening_cash) or self.opening_cash < 0:
            raise ValueError("Starting cash must be finite and nonnegative.")
        if (len(self.starting_weights) != 4
                or any(not isfinite(w) or w < 0 for w in self.starting_weights)
                or not isclose(sum(self.starting_weights), 1, rel_tol=0, abs_tol=1e-9)):
            raise ValueError("Illustrative starting ETF weights must be nonnegative and total 100%.")


def weekdays(day, count):
    """Shift by modeled weekdays. Exchange/bank holidays and cutoffs are omitted."""
    while count:
        step = 1 if count > 0 else -1
        day += timedelta(days=step)
        if day.weekday() < 5:
            count -= step
    return day


def cash_schedule(holdings, payment_dates, opening_cash, payout, lag=1, loss=0):
    """Sell a fixed reference-dollar quantity pro rata from eligible holdings each quarter."""
    balance = round(opening_cash, 2)
    remaining = dict(holdings)
    pending = []
    rows = []
    for payment in payment_dates:
        if payment.weekday() >= 5:
            payment = weekdays(payment, 1)
        trade = weekdays(payment, -2)
        available = weekdays(trade, lag)
        total = sum(remaining.values())
        reference_sale = min(total, payout)
        sales = {ticker: value * reference_sale / total for ticker, value in remaining.items()} if total else {}
        for ticker, sold in sales.items():
            remaining[ticker] = max(0.0, remaining[ticker] - sold)
        proceeds = round(reference_sale * (1 - loss), 2)
        if proceeds:
            pending.append((available, proceeds))
        settled = sum(amount for day, amount in pending if day <= payment)
        pending = [(day, amount) for day, amount in pending if day > payment]
        opening = balance
        paid = min(payout, round(opening + settled, 2))
        balance = round(opening + settled - paid, 2)
        rows.append({"payment": payment, "opening": opening, "trade": trade, "sales": sales,
                     "proceeds": proceeds, "available": available, "settled": settled,
                     "due": payout, "paid": paid, "closing": balance, "shortfall": round(payout - paid, 2)})
    return rows


def issuer_exposure(weights, coverage):
    """Aggregate mapped corporate issuers and bound the possible contribution of unmapped holdings."""
    companies = defaultdict(float)
    unmapped = 0.0
    assumed = False
    for ticker, weight in weights.items():
        if weight == 0:
            continue
        fund = coverage.get(ticker, {})
        mapped = fund.get("companies", {})
        classified = fund.get("exempt", 0) + sum(mapped.values())
        if (not 0 <= classified <= 1 + 1e-12
                or fund.get("exempt", 0) < 0 or any(not 0 <= value <= 1 for value in mapped.values())):
            raise ValueError(f"Invalid issuer coverage for {ticker}.")
        unmapped += weight * max(0, 1 - classified)
        assumed |= fund.get("policy_assumption", False)
        for issuer, amount in mapped.items():
            companies[issuer] += weight * amount
    largest = max(companies.values(), default=0)
    upper = largest + unmapped
    if largest > .08 + 1e-12:
        status = FAIL
    elif upper > .08 + 1e-12:
        status = UNKNOWN
    else:
        status = ASSUMED if assumed else VERIFIED
    return {"status": status, "companies": dict(companies), "unmapped": unmapped, "upper": upper}


def rebalance(weights, starting_weights, capital):
    """One-way turnover for a fully invested rebalance without external flows."""
    rows = []
    for (ticker, weight), starting in zip(weights.items(), starting_weights, strict=True):
        start = round(starting * capital, 2)
        target = round(weight * capital, 2)
        rows.append({"fund": ticker, "start": start, "target": target,
                     "buy": max(0, target - start), "sell": max(0, start - target)})
    turnover = sum(abs(weight - start) for weight, start in zip(weights.values(), starting_weights)) / 2
    approval = turnover > .25 + 1e-12
    return {"status": "Approval required" if approval else ASSUMED, "turnover": turnover, "rows": rows}


def liquidity(weights, capital, funds, fallback_prices):
    """Compare liquidation size with dated volume under a participation assumption."""
    rows = []
    for ticker, weight in weights.items():
        if not weight:
            continue
        fund = funds[ticker]
        reference = fund.get("price", fallback_prices[ticker])
        shares = weight * capital / reference
        volume = fund.get("volume")
        # Order on days 1–4, normal T+1 by day 5. Stress: days 1–2, T+3 by day 5.
        daily = volume * .01 if volume is not None else 0
        normal = min(shares, 4 * daily) * reference
        stress = min(shares, 2 * daily * .10) * reference
        rows.append({"fund": ticker, "dollars": weight * capital, "price": reference, "shares": shares,
                     "normal": normal, "stress": stress, "share_of_volume": shares / volume if volume else None})
    return {"status": UNKNOWN, "rows": rows,
            "normal": sum(row["normal"] for row in rows) / capital,
            "stress": sum(row["stress"] for row in rows) / capital}


def load_evidence():
    return json.loads(EVIDENCE_PATH.read_text())


def assess(weights, eligible, capital, payout, assumptions, evidence, fallback_prices):
    funds = evidence["funds"]
    if assumptions.opening_cash > capital:
        raise ValueError("Illustrative opening cash cannot exceed the reserve capital.")
    holdings = {ticker: weights[ticker] * (capital - assumptions.opening_cash)
                for ticker in eligible if weights[ticker]}
    cash_args = (holdings, assumptions.payment_dates, assumptions.opening_cash, payout)
    cash = {label: cash_schedule(*cash_args, **kwargs) for label, kwargs in (
        ("Normal", {}), ("Delayed proceeds", {"lag": 3}), ("Market loss", {"loss": .05}),
    )}
    issuer = issuer_exposure(weights, {ticker: fund["issuer"] for ticker, fund in funds.items()})
    turnover = rebalance(weights, assumptions.starting_weights, capital)
    market = liquidity(weights, capital, funds, fallback_prices)
    status = cash_status(cash["Normal"])
    return {"cash": cash, "issuer": issuer, "turnover": turnover, "liquidity": market,
            "checks": dict(zip(RULES, (status, issuer["status"], turnover["status"],
                                      UNKNOWN, UNKNOWN, UNKNOWN), strict=True))}


def cash_status(rows):
    return FAIL if any(row["shortfall"] for row in rows) else ASSUMED


def money(value):
    return f"\\${value:,.2f}"


def markdown_table(headers, rows):
    return "\n".join(("| " + " | ".join(headers) + " |",
                      "|" + "---|" * len(headers),
                      *("| " + " | ".join(row) + " |" for row in rows)))


def operational_detail(result, evidence, price_date):
    """Describe the same computed detail in the app and reproducible report."""
    cash, issuer, turnover, market = (result[key] for key in ("cash", "issuer", "turnover", "liquidity"))
    checks = result["checks"]
    funds = evidence["funds"]
    lines = [
        f"**Scholarship payments · {checks[RULES[0]]}.** Four illustrative quarters use separate cash funded "
        "from the USD 1 million reserve, with ETF weights applied to the remainder. Each sale targets USD 10,000 in "
        "pre-shock units from SGOV/SCHR pro rata, capped at remaining holdings. No automatic top-up or sale of other ETFs.",
        "Sales are planned two weekdays early. Weekend payments roll forward to Monday. An illustrative weekday calendar "
        "omits exchange and banking holidays, cutoffs and transfer delays. Normal proceeds are usable at T+1, "
        f"consistent with standard [ETF settlement]({evidence['settlement']}). Delay assumes T+3; "
        "market loss assumes 5% lower sale prices for the same units throughout. No growth, dividends, account fees, "
        "execution costs or late payment catch-up are modeled. Opening cash is prior closing cash before crediting newly available proceeds.",
        "Before funding, confirm actual dates, balances, order execution, settlement and payment cutoffs with the custodian.",
    ]
    for label, rows in cash.items():
        lines.extend([f"**{label} · {cash_status(rows)}**", markdown_table(
            ("Payment", "Opening cash", "Sale date", "Sale at reference prices", "Proceeds", "Available",
             "Newly available cash", "Due", "Paid", "Closing cash", "Shortfall"),
            ((str(row["payment"]), money(row["opening"]), str(row["trade"]),
              ", ".join(f"{ticker} {money(value)}" for ticker, value in row["sales"].items()) or "—",
              money(row["proceeds"]), str(row["available"]) if row["proceeds"] else "—",
              money(row["settled"]), money(row["due"]), money(row["paid"]),
              money(row["closing"]), money(row["shortfall"])) for row in rows),
        )])
    held = [row["fund"] for row in market["rows"]]
    known = ", ".join(f"{name} {value:.2%}" for name, value in issuer["companies"].items()) or "none mapped"
    lines.extend([
        f"**Issuer cap · {issuer['status']}.** Mapped company exposure: {known}. "
        f"Unmapped portfolio share {issuer['unmapped']:.3%}; conservative single-company upper bound "
        f"{issuer['upper']:.3%} versus 8%.",
        f"The [Campus mandate]({evidence['mandate']}) exempts cash, U.S. Treasury securities and diversified funds. "
        "For other holdings, multiply fund weight by each mapped company weight and sum by company across funds. "
        "The ETF sponsor is not substituted for underlying issuers. The upper bound assigns all unmapped "
        "weight to the largest mapped company (or one new company). Before funding, confirm exemption "
        "interpretation and refresh holdings and company mappings for nonexempt positions.",
        markdown_table(("Fund", "Holdings / policy as of", "Dated evidence"),
                       ((ticker, funds[ticker]["issuer_as_of"],
                         f"[Provider]({funds[ticker]['issuer_source']}) · {funds[ticker]['issuer_note']}")
                        for ticker in held)),
        f"**Rebalance turnover · {turnover['status']}.** {turnover['turnover']:.2%} one-way turnover "
        "(half the sum of absolute weight changes), on USD 1 million with no external flows. Approval applies "
        "strictly above 25%. The starting weights are illustrative. Initial funding and scholarship sales "
        f"are outside this rebalance. Annual review and cumulative turnover: {UNKNOWN}. Obtain beginning holdings, "
        "dated trade and flow records, an agreed annual turnover convention, annual review evidence and any required approval.",
        markdown_table(("Fund", "Starting", "Proposed", "Buy", "Sell"),
                       ((row["fund"], money(row["start"]), money(row["target"]),
                         money(row["buy"]), money(row["sell"])) for row in turnover["rows"])),
        f"**Five-business-day liquidity · {market['status']}.** The dated volume proxy covers {market['normal']:.1%} "
        f"of portfolio value in the normal case and {market['stress']:.1%} in the stress case, versus the 90% requirement.",
        "Compare full sleeve sales on the USD 1 million portfolio. Normal uses 1% of observed daily share volume over "
        "four trading sessions with T+1. Stress uses 10% of observed volume, the same 1% participation and two "
        "trading sessions with T+3. Capacity is capped at each sleeve. Missing volume contributes no capacity to "
        "this evidence screen. SCHR uses a historical single-day observation, and VT uses a historical provider view. "
        "Share estimates for funds without "
        f"a provider price use the {price_date} adjusted-price archive as a scale proxy. "
        "Capacity uses reference prices and excludes market impact and price gaps. Historical volume and a displayed "
        "spread cannot establish depth, fills, execution costs, access to proceeds or reliable stressed liquidity. "
        "ETF holders generally sell in the secondary market. Before funding, obtain fresh multi-session volume, "
        "quotes, depth and broker execution and cash-release confirmation for the full portfolio.",
        f"Provider spreads are 30-day median quoted spreads relative to the midpoint "
        f"([measurement definition]({evidence['spread_definition']})). Evidence retrieved {evidence['retrieved']} "
        "for this operational review, after the original investment decision date.",
        markdown_table(("Fund", "Liquidation USD", "Reference price", "Approx. shares", "% daily shares", "Volume evidence",
                        "Median spread", "Normal capacity", "Stress capacity"), (
            (row["fund"], money(row["dollars"]), money(row["price"]), f"{row['shares']:,.0f}",
             f"{row['share_of_volume']:.2%}" if row["share_of_volume"] is not None else "—",
             (f"[{fund['market_as_of'] or 'Unavailable'}]({fund['market_source']}) · "
              f"{fund.get('volume', 0):,} shares · {fund['window']}" if "volume" in fund
              else f"[Unavailable]({fund['market_source']}) · {fund['window']}"),
             f"{fund['spread_pct']:.2f}% ({fund.get('spread_window', fund['market_as_of'])})" if "spread_pct" in fund else "—",
             money(row["normal"]), money(row["stress"]))
            for row in market["rows"] for fund in (funds[row["fund"]],))),
        f"**Account permissions · {UNKNOWN}.** No actual account documentation exists in the case. "
        "Before funding, obtain custodian confirmation of the permitted instruments, authorized traders and "
        "disbursement signatories, approval limits, and cash transfer rules. Keep credentials and account identifiers "
        "out of the repository.",
    ])
    return "\n\n".join(lines)
