"""Render the Campus app's calculations as a reproducible Markdown report."""

import argparse
from dataclasses import replace

from campus import DEFAULT, TICKERS, load_snapshot, run, stress_action, stress_results
from operations import RULES, load_evidence, markdown_table, operational_detail
from portfolio import largest_weight_change


def summary(mix):
    if mix is None:
        return "No feasible grid allocation"
    return (f"{mix['net']:.2%} net / {mix['volatility']:.2%} risk / "
            f"{mix['reserve']:.0%} reserve · {mix['verdict']}")


def render(inputs=DEFAULT, include_stress=True):
    snapshot = load_snapshot()
    evidence = load_evidence()
    baseline = run(snapshot=snapshot, evidence=evidence)
    initial = baseline["mixes"]["Constrained"]
    result = baseline if inputs == DEFAULT else run(inputs, fixed_weights=initial["weights"],
                                                     snapshot=snapshot, evidence=evidence)
    estimate, signal = result["estimate"], result["signal"]
    lines = [
        "# Campus Scholarship Reserve results", "",
        f"Decision date {signal['cutoff']}. Price vintage retrieved {snapshot[1]['downloaded_at_utc']}.",
        f"{estimate['observations']} USD monthly returns from {estimate['return_start']} to {estimate['end']}.",
        f"Net target {inputs.net_target_pct:.2f}%, reserve floor {inputs.reserve_floor_pct:g}%, "
        f"additional annual cost {inputs.cost_bp:g} bp, VT return shift {inputs.vt_shift_points:+g} points.",
        f"VT trailing 12-month signal {signal['return']:.2%} ({signal['start']} to {signal['end']}), "
        f"archive available {signal['available_on']} ({signal['lag_days']} days after last observation).",
        "", f"**{result['action']}**", "",
        "| Annual estimate | " + " | ".join(TICKERS) + " |",
        "|---|---:|---:|---:|---:|",
        "| Return before additional cost | " + " | ".join(f"{s['return']:.2%}" for s in estimate["sleeves"]) + " |",
        "| Volatility | " + " | ".join(f"{s['volatility']:.2%}" for s in estimate["sleeves"]) + " |", "",
        "| Mix | " + " | ".join(TICKERS) + " | Return before extra cost | Net return | Volatility | Eligible reserve | Verdict |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---|",
    ]
    for name, mix in result["mixes"].items():
        weights = " | ".join(f"{w:.0%}" for w in mix["weights"])
        lines.append(f"| {name} | {weights} | {mix['before_cost']:.2%} | {mix['net']:.2%} | "
                     f"{mix['volatility']:.2%} | {mix['reserve']:.2%} | {mix['verdict']} |")
    candidate = result["candidate"]
    lines.extend(["", f"Feasible grid mixes: {candidate['feasible']:,} / {candidate['evaluated']:,}."
                  if candidate else "No feasible grid mix.", "", "## Rule-level verdicts", ""])
    names = list(result["mixes"])
    lines.extend(["| Rule | " + " | ".join(names) + " |", "|---|" + "---|" * len(names)])
    for rule in result["mixes"][names[0]]["checks"]:
        lines.append("| " + rule + " | " + " | ".join(result["mixes"][name]["checks"][rule] for name in names) + " |")
    lines.extend(["", "## Operational mandate evidence", ""])
    for name, mix in result["mixes"].items():
        lines.extend([f"### {name}", "", operational_detail(mix["operational"], evidence, snapshot[2][-1]), ""])
    if include_stress:
        lines.extend(["", "## One-at-a-time stresses", "",
                      "The fixed column holds the original constrained weights. Risk uses each scenario's inputs.",
                      "", "| Input | Original weights | Reoptimized | New weights (SGOV/SCHR/USIG/VT) | Largest change | Action |",
                      "|---|---|---|---|---|---|"])
        stresses = stress_results(snapshot, baseline, evidence=evidence)
        for label, trial in stresses.items():
            new = trial["mixes"].get("Constrained")
            delta = largest_weight_change(initial, new)
            weight_text = "/".join(f"{w:.0%}" for w in new["weights"]) if new else "—"
            shift_text = f"{delta:.0f} points" if delta is not None else "—"
            lines.append(f"| {label} | {summary(trial['mixes']['Original weights'])} | {summary(new)} | "
                         f"{weight_text} | {shift_text} | {stress_action(trial)} |")
        lines.extend(["", "### Operational checks by stress and allocation", "",
                      "Liquidity percentages are volume proxies. Account permissions are not established in every scenario.", "",
                      markdown_table(("Scenario", "Mix", "Payment illustration (normal)", "Issuer cap", "Turnover",
                                      "Normal liquidity proxy"), (
                          (label, name, mix["checks"][RULES[0]], mix["checks"][RULES[1]],
                           f"{op['turnover']['turnover']:.2%} · {op['turnover']['status']}",
                           f"{op['liquidity']['normal']:.1%} · {op['liquidity']['status']}")
                          for label, trial in stresses.items()
                          for name, mix in trial["mixes"].items()
                          if name in ("Original weights", "Constrained")
                          for op in (mix["operational"],)))])
        lines.extend(["", "Before funding, verify forward-looking assumptions, all open mandate rules and dated payouts. "
                      "Hold if the VT signal is unavailable or nonpositive. Stop if the pilot mix misses the "
                      "5.50% estimated net target or the reserve floor."])
    return "\n".join(lines) + "\n"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cost-bp", type=float, help="Run one cost scenario with the original weights alongside it.")
    args = parser.parse_args()
    print(render() if args.cost_bp is None else render(replace(DEFAULT, cost_bp=args.cost_bp), False), end="")
