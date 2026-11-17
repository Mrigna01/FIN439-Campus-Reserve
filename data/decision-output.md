# Campus Scholarship Reserve results

Decision date 2026-11-17. Price vintage retrieved 2026-10-22T19:41:10.270903+00:00.
60 USD monthly returns from 2021-10-29 to 2026-09-30.
Net target 5.50%, reserve floor 4%, additional annual cost 10 bp, VT return shift +0 points.
VT trailing 12-month signal 16.45% (2025-09-30 to 2026-09-30), archive available 2026-10-22 (22 days after last observation).

**Pilot on paper only. Hold any trades until assumptions and open checks are verified.**

| Annual estimate | SGOV | SCHR | USIG | VT |
|---|---:|---:|---:|---:|
| Return before additional cost | 3.72% | -0.30% | 0.12% | 11.90% |
| Volatility | 0.50% | 5.41% | 7.86% | 14.92% |

| Mix | SGOV | SCHR | USIG | VT | Return before extra cost | Net return | Volatility | Eligible reserve | Verdict |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| Equal weight | 25% | 25% | 25% | 25% | 3.86% | 3.76% | 6.51% | 50.00% | Fails modeled checks |
| 60/40 benchmark | 0% | 0% | 40% | 60% | 7.18% | 7.08% | 11.59% | 0.00% | Fails modeled checks |
| Constrained | 75% | 0% | 0% | 25% | 5.76% | 5.66% | 3.82% | 75.00% | Passes modeled checks |

Feasible grid mixes: 392 / 1,771.

## Rule-level verdicts

| Rule | Equal weight | 60/40 benchmark | Constrained |
|---|---|---|---|
| Weights total 100% | Pass | Pass | Pass |
| Long-only within the ETF universe | Pass | Pass | Pass |
| Net objective ≥ 5.50% | Fail | Pass | Pass |
| Eligible reserve ≥ 4% | Pass | Fail | Pass |
| At least 90% redeemable within five business days | Not established | Not established | Not established |
| Company issuer exposure ≤ 8% under case exemptions | Not established | Not established | Not established |
| Annual rebalance and approval above 25% annual turnover | Not established | Not established | Not established |
| Cash available on scholarship payment dates | Not established | Not established | Not established |
| Underlying exposures and account permissions | Not established | Not established | Not established |

## One-at-a-time stresses

The fixed column holds the original constrained weights. Risk uses each scenario's inputs.

| Input | Original weights | Reoptimized | New weights (SGOV/SCHR/USIG/VT) | Largest change | Action |
|---|---|---|---|---|---|
| VT estimate −1 percentage point | 5.41% net / 3.82% risk / 75% reserve · Fails modeled checks | 5.77% net / 4.55% risk / 70% reserve · Passes modeled checks | 70%/0%/0%/30% | 5 points | Review original weights before proceeding |
| Trailing 36 months | 8.29% net / 2.95% risk / 75% reserve · Passes modeled checks | 5.92% net / 1.21% risk / 90% reserve · Passes modeled checks | 90%/0%/0%/10% | 15 points | Paper pilot remains conditional |
| Additional cost 30 bp | 5.46% net / 3.82% risk / 75% reserve · Fails modeled checks | 5.87% net / 4.55% risk / 70% reserve · Passes modeled checks | 70%/0%/0%/30% | 5 points | Review original weights before proceeding |
| Reserve floor 80% | 5.66% net / 3.82% risk / 75% reserve · Fails modeled checks | No feasible grid allocation | — | — | Stop: no allocation passes the active constraints on the grid. |

Before funding, verify forward-looking assumptions, all open mandate rules and dated payouts. Hold if the VT signal is unavailable or nonpositive. Stop if the pilot mix misses the 5.50% estimated net target or the reserve floor.
