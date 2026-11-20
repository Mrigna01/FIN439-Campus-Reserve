"""Campus mandate, point-in-time review gate and reproducible portfolio scenarios."""

from dataclasses import dataclass, replace
from datetime import date, datetime
import json
from math import isclose, isfinite
from pathlib import Path

import portfolio as portfolio
from operations import Assumptions, assess, load_evidence

ROOT = Path(__file__).resolve().parent
TICKERS = ("SGOV", "SCHR", "USIG", "VT")
BENCHMARK = {"USIG": .4, "VT": .6}
NET_TARGET = .055
STARTING_CAPITAL = 1_000_000
QUARTERLY_PAYOUT = 10_000
DECISION_DATE = date(2026, 11, 17)
TOLERANCE = 1e-12


@dataclass(frozen=True)
class Inputs:
    last_36: bool = False
    vt_shift_points: float = 0
    cost_bp: float = 10
    reserve_floor_pct: float = 4
    net_target_pct: float = NET_TARGET * 100

    def __post_init__(self):
        if not all(isfinite(value) for value in (
            self.vt_shift_points, self.cost_bp, self.reserve_floor_pct, self.net_target_pct
        )) or self.cost_bp < 0 or not 0 <= self.reserve_floor_pct <= 100:
            raise ValueError("Use finite inputs, nonnegative cost and a reserve floor from 0 to 100%.")

    @property
    def annual_cost(self):
        return self.cost_bp / 10_000


DEFAULT = Inputs()
STRESSES = {
    "VT estimate −1 percentage point": replace(DEFAULT, vt_shift_points=-1),
    "Trailing 36 months": replace(DEFAULT, last_36=True),
    "Additional cost 30 bp": replace(DEFAULT, cost_bp=30),
    "Reserve floor 80%": replace(DEFAULT, reserve_floor_pct=80),
}


def load_snapshot(path=ROOT / "prices.csv", metadata_path=ROOT / "data/prices_source.json"):
    source = path.read_bytes()
    names, dates, prices = portfolio.read_monthly_prices(source)
    metadata = json.loads(metadata_path.read_text())
    if tuple(names) != TICKERS or metadata["columns"] != ["Date", *TICKERS]:
        raise ValueError("Snapshot fund order differs from the Campus mandate.")
    if metadata["rows"] != [[day.isoformat(), *row] for day, row in zip(dates, prices)]:
        raise ValueError("CSV prices differ from the archived source metadata.")
    for index, ticker in enumerate(TICKERS):
        details = metadata["sources"][ticker]
        if details["currency"] != "USD":
            raise ValueError(f"{ticker}: expected USD adjusted prices.")
        observations = details["monthly_observations"]
        if len(observations) != len(dates) or any(
            observations.get(day.isoformat()[:7], {}).get("date") != day.isoformat()
            or observations[day.isoformat()[:7]]["adj_close"] != row[index]
            for day, row in zip(dates, prices)
        ):
            raise ValueError(f"{ticker}: source observations differ from the CSV.")
    return source, metadata, dates, prices


def trend_signal(dates, vt_prices, available_on, cutoff):
    """Use only the archived vintage, starting on its verified availability date."""
    if cutoff < available_on:
        return None
    observed = [(day, price) for day, price in zip(dates, vt_prices) if day <= cutoff]
    if len(observed) < 13:
        return None
    start, start_price = observed[-13]
    end, end_price = observed[-1]
    return {"start": start, "end": end, "return": end_price / start_price - 1,
            "available_on": available_on, "cutoff": cutoff,
            "lag_days": (available_on - end).days}


def evaluate(weights, sleeves, covariance, inputs, assumptions, evidence, reference_prices):
    before_cost = portfolio.expected_return(weights, sleeves)
    reserve = portfolio.reserve_weight(weights, sleeves)
    net = before_cost - inputs.annual_cost
    modeled = {
        "Weights total 100%": isclose(sum(weights), 1, rel_tol=0, abs_tol=TOLERANCE),
        "Long-only within the ETF universe": all(weight >= 0 for weight in weights),
        f"Net objective ≥ {inputs.net_target_pct:.2f}%": net >= inputs.net_target_pct / 100 - TOLERANCE,
        f"Eligible reserve ≥ {inputs.reserve_floor_pct:g}%": reserve >= inputs.reserve_floor_pct / 100 - TOLERANCE,
    }
    checks = {rule: "Pass" if passed else "Fail" for rule, passed in modeled.items()}
    if inputs.reserve_floor_pct < DEFAULT.reserve_floor_pct:
        checks["Case reserve ≥ 4%"] = "Pass" if reserve >= .04 - TOLERANCE else "Fail"
    if inputs.net_target_pct < DEFAULT.net_target_pct:
        checks["Case net objective ≥ 5.50%"] = "Pass" if net >= NET_TARGET - TOLERANCE else "Fail"
    verdict = "Fails modeled checks" if "Fail" in checks.values() else "Passes modeled checks"
    operational = assess(dict(zip(TICKERS, weights)), (s["name"] for s in sleeves if s["reserve_eligible"]),
                         STARTING_CAPITAL, QUARTERLY_PAYOUT, assumptions, evidence, reference_prices)
    checks.update(operational["checks"])
    return {"weights": weights, "before_cost": before_cost, "net": net,
            "volatility": portfolio.portfolio_volatility(weights, covariance),
            "reserve": reserve, "checks": checks,
            "operational": operational, "verdict": verdict}


def recommendation(optimized, signal):
    if optimized is None:
        return "Stop: no allocation passes the active constraints on the grid."
    if optimized["verdict"] != "Passes modeled checks":
        return "Stop: the allocation fails the Campus case rules."
    if signal is None or signal["return"] <= 0:
        return "Hold for review: the equity signal is unavailable or nonpositive."
    return "Pilot on paper only. Hold any trades until assumptions and open checks are verified."


def run(inputs=DEFAULT, fixed_weights=None, cutoff=DECISION_DATE, snapshot=None,
        assumptions=Assumptions(), evidence=None):
    source, metadata, dates, prices = load_snapshot() if snapshot is None else snapshot
    availability = datetime.fromisoformat(metadata["downloaded_at_utc"]).date()
    if cutoff < availability or cutoff < dates[-1]:
        raise ValueError("The archived price vintage was not available by this decision date.")
    signal = trend_signal(dates, [row[3] for row in prices], availability, cutoff)
    estimate = portfolio.estimate_from_csv(source, last_36=inputs.last_36)
    sleeves, correlations = estimate["sleeves"], estimate["correlations"]
    sleeves[3]["return"] += inputs.vt_shift_points / 100
    covariance = portfolio.covariance_matrix(sleeves, correlations)
    candidate = portfolio.search_portfolio(sleeves, correlations, inputs.net_target_pct / 100,
                                      inputs.reserve_floor_pct / 100, inputs.annual_cost)
    weights = {
        "Equal weight": portfolio.equal_weights(sleeves),
        "60/40 benchmark": portfolio.benchmark_weights(sleeves, BENCHMARK),
    }
    if candidate is not None:
        weights["Constrained"] = candidate["weights"]
    if fixed_weights is not None:
        weights["Original weights"] = fixed_weights
    evidence = load_evidence() if evidence is None else evidence
    reference_prices = dict(zip(TICKERS, prices[-1]))
    mixes = {label: evaluate(mix, sleeves, covariance, inputs, assumptions, evidence, reference_prices)
             for label, mix in weights.items()}
    optimized = mixes.get("Constrained")
    return {"estimate": estimate, "mixes": mixes, "candidate": candidate,
            "signal": signal, "action": recommendation(optimized, signal)}


def stress_results(snapshot, baseline, assumptions=Assumptions(), evidence=None):
    fixed = baseline["mixes"]["Constrained"]["weights"]
    return {
        label: run(inputs, fixed_weights=fixed, snapshot=snapshot, assumptions=assumptions, evidence=evidence)
        for label, inputs in STRESSES.items()
    }



def stress_action(trial):
    if trial["mixes"].get("Constrained") is None:
        return trial["action"]
    if trial["mixes"]["Original weights"]["verdict"] == "Fails modeled checks":
        return "Review original weights before proceeding"
    return "Paper pilot remains conditional"
