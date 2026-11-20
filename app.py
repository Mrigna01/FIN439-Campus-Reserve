"""Campus Scholarship Reserve committee app. Run: python -m streamlit run app.py."""

import streamlit as st

from campus import DEFAULT, Inputs, STARTING_CAPITAL, TICKERS, load_snapshot, run, stress_action, stress_results
from operations import Assumptions, PAYMENT_ILLUSTRATION_NOTE, load_evidence, operational_detail
from portfolio import largest_weight_change
from report import summary

st.set_page_config(page_title="Campus Scholarship Reserve", layout="wide")
st.title("Campus Scholarship Reserve")
st.caption("Investment committee review · $1 million fictional fund · Education, not investment advice")

with st.sidebar:
    st.header("Scenario inputs")
    last_36 = st.selectbox("Lookback", ("60 monthly returns", "36 monthly returns")) == "36 monthly returns"
    shift = st.number_input("VT annual return shift (percentage points)", value=0.0, step=0.25)
    cost = st.number_input("Additional annual cost (bp)", min_value=0.0, value=float(DEFAULT.cost_bp), step=1.0)
    floor = st.number_input("Minimum eligible reserve (%)", min_value=0.0, max_value=100.0,
                            value=float(DEFAULT.reserve_floor_pct), step=1.0)
    st.caption("The 5.50% net target holds across scenarios.")
    with st.expander("Illustrative operational inputs"):
        defaults = Assumptions()
        opening_cash = st.number_input("Opening cash for standalone payment illustration (USD)",
                                       0.0, float(STARTING_CAPITAL),
                                       value=float(defaults.opening_cash), step=1000.0)
        st.caption(PAYMENT_ILLUSTRATION_NOTE)
        dates = tuple(st.date_input(f"Illustrative payment {i}", day)
                      for i, day in enumerate(defaults.payment_dates, 1))
        starting = tuple(st.number_input(f"Starting {ticker} (%)", 0.0, 100.0,
                                         value=weight * 100, step=1.0) / 100
                         for ticker, weight in zip(TICKERS, defaults.starting_weights))
        try:
            assumptions = Assumptions(dates, opening_cash, starting)
        except ValueError as error:
            st.warning(f"{error} Operational displays use the default assumptions until the inputs are valid.")
            assumptions = defaults

try:
    snapshot = load_snapshot()
    evidence = load_evidence()
    baseline = run(snapshot=snapshot, assumptions=assumptions, evidence=evidence)
    fixed = baseline["mixes"]["Constrained"]["weights"]
    inputs = Inputs(last_36=last_36, vt_shift_points=shift, cost_bp=cost, reserve_floor_pct=floor)
    active = (baseline if inputs == DEFAULT else
              run(inputs, fixed_weights=fixed, snapshot=snapshot, assumptions=assumptions, evidence=evidence))
except (OSError, ValueError, KeyError) as error:
    st.error(f"Cannot evaluate the snapshot or scenario: {error}")
    st.stop()

data, signal = active["estimate"], active["signal"]
st.caption(f"Decision {signal['cutoff']} · {data['observations']} monthly returns "
           f"from {data['return_start']} to {data['end']} · {cost:g} bp annual cost")
st.subheader("Committee action")
st.write(active["action"])
if active["candidate"] is None:
    st.warning("No feasible mix on the five-percentage-point grid.")
if active["mixes"].get("Original weights", {}).get("verdict") == "Fails modeled checks":
    st.warning("Original pilot fails at least one active modeled rule. Review before switching allocations.")

st.subheader("Portfolio comparison")
st.table([
    {"Portfolio": name, **{ticker: f"{weight:.0%}" for ticker, weight in zip(TICKERS, mix["weights"])},
     "Before extra cost": f"{mix['before_cost']:.2%}", "Net return": f"{mix['net']:.2%}",
     "Annual volatility": f"{mix['volatility']:.2%}", "Eligible reserves": f"{mix['reserve']:.2%}",
     "Eligible USD at $1m": f"${mix['reserve'] * STARTING_CAPITAL:,.0f}", "Verdict": mix["verdict"]}
    for name, mix in active["mixes"].items()
])
st.caption("Equal weight holds 25% in each fund. The policy benchmark holds 60% VT and 40% USIG. "
           "The constrained search minimizes estimated annual volatility on a five-point grid.")
with st.expander("Mandate checks by portfolio", expanded=True):
    mixes = active["mixes"]
    st.table([{"Rule": rule, **{name: mix["checks"][rule] for name, mix in mixes.items()}}
              for rule in next(iter(mixes.values()))["checks"]])
    st.caption("SGOV and SCHR count as classroom reserves. Operational statuses are separate from the modeled verdict. "
               "The case assumes a seven-year horizon and $10,000 quarterly distributions.")

with st.expander("Point-in-time signal and data card", expanded=True):
    st.write(f"**VT trailing 12-month adjusted-price return: {signal['return']:.2%}.** "
             f"Observation endpoints {signal['start']} to {signal['end']}.")
    st.write(f"Latest VT adjusted close ÷ adjusted close 12 months earlier − 1. Real USD Yahoo Finance "
             f"prices in the archived snapshot were available {signal['available_on']} UTC date "
             f"({signal['lag_days']} days after the last observation) for decision cutoff {signal['cutoff']}. "
             "No signal is available before archive availability or with fewer than 13 monthly prices. "
             "Malformed or missing observations stop evaluation.")
    st.write("A nonpositive or unavailable signal blocks the paper-pilot recommendation pending review. "
             "The signal does not alter weights or forecast returns. One archived vintage cannot validate "
             "historical timing or a momentum premium.")

with st.expander("One-at-a-time stresses"):
    rows = []
    stresses = stress_results(snapshot, baseline, assumptions, evidence)
    for label, trial in stresses.items():
        new = trial["mixes"].get("Constrained")
        delta = largest_weight_change(baseline["mixes"]["Constrained"], new)
        rows.append({"Scenario": label, "Original weights": summary(trial["mixes"]["Original weights"]),
                     "Reoptimized": summary(new),
                     "New weights (SGOV/SCHR/USIG/VT)": "/".join(f"{w:.0%}" for w in new["weights"]) if new else "—",
                     "Largest move": f"{delta:.0f} points" if delta is not None else "—", "Action": stress_action(trial)})
    st.table(rows)
    st.caption("Review the original mix whenever it fails a rule, even if a new optimized allocation passes.")

with st.expander("Operational mandate evidence"):
    portfolios = dict(active["mixes"])
    for scenario, trial in stresses.items():
        for label in ("Original weights", "Constrained"):
            if label in trial["mixes"]:
                portfolios[f"{scenario} · {label}"] = trial["mixes"][label]
    choices = list(portfolios)
    selection = st.selectbox("Portfolio for operational review", choices,
                             index=choices.index("Constrained") if "Constrained" in choices else 0)
    st.markdown(operational_detail(portfolios[selection]["operational"], evidence, snapshot[2][-1]))

with st.expander("Return and risk assumptions"):
    st.table([{"Fund": s["name"], "Annual return": f"{s['return']:.2%}",
               "Annual volatility": f"{s['volatility']:.2%}"} for s in data["sleeves"]])
    st.write("Monthly adjusted close ratios produce simple returns. Annual return is 12 × the arithmetic "
             "monthly mean. Annual volatility is the square root of 12 times monthly variance, including "
             "cross-fund covariance. Historical estimates are scenario inputs. The uniform annual cost "
             "reduces estimated return once and leaves volatility unchanged.")
