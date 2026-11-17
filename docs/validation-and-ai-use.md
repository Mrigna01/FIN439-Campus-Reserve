# Validation and AI use

## Data and decision boundary

The fictional case decision is dated November 17, 2026. The frozen [CSV](../prices.csv) has 61 aligned USD observations per fund from September 30, 2021 to September 30, 2026. The [archive metadata](../data/prices_source.json) records October 22, 2026 at 19:41:10 UTC as retrieval time and preserves the source query URLs and per-fund records. The loader compares each CSV value and trading date against both the combined source rows and ticker-specific metadata. It rejects gaps, duplicates, nonpositive or nonfinite prices, unexpected funds and zero sample variation. There is no filling, interpolation or live refresh.

| Fund | Exposure and model use | Sources |
|---|---|---|
| SGOV | Very short U.S. Treasuries, the primary reserve proxy; future yield is sensitive to reinvestment rates | [iShares prospectus](https://www.ishares.com/us/literature/summary-prospectus/sp-ishares-0-3-month-treasury-bond-etf-2-28.pdf) · [Yahoo history](https://finance.yahoo.com/quote/SGOV/history/) |
| SCHR | Intermediate U.S. Treasuries, eligible under the classroom rule with more duration exposure than SGOV | [Schwab](https://www.schwabassetmanagement.com/products/schr) · [Yahoo history](https://finance.yahoo.com/quote/SCHR/history/) |
| USIG | USD investment-grade corporate credit, the bond side of the benchmark | [iShares](https://www.ishares.com/us/literature/fact-sheet/usig-ishares-broad-usd-investment-grade-corporate-bond-etf-fund-fact-sheet-en-us.pdf) · [Yahoo history](https://finance.yahoo.com/quote/USIG/history/) |
| VT | Broad global equity, the benchmark growth sleeve and source of the review signal | [Vanguard](https://investor.vanguard.com/investment-products/etfs/profile/vt) · [Yahoo history](https://finance.yahoo.com/quote/VT/history/) |

The parser uses the last observed adjusted close of each month. Monthly simple return is current adjusted close divided by previous adjusted close, less one. The default first return is October 29, 2021; the 36-return window begins October 31, 2023. Return is the arithmetic monthly mean times 12, covariance uses monthly sample risk scaled by 12, and portfolio volatility is the square root of the weight-covariance-weight product. There is no compounding or distribution cash-flow simulation. Adjustments account for distributions and splits. Historical fund prices already reflect fund-level operating expenses. Subtract the separate annual cost in basis points once from each portfolio’s estimate. The 10 and 30 bp cost cases are explicit budgeting assumptions. They do not represent prices quoted by a broker or custodian.

The 2.50% inflation input is inherited from the lab and isolates portfolio effects. The BLS CPI measures changes in consumer prices. The case assumption is not a BLS forecast. The historical 3.72% SGOV and 11.90% VT arithmetic estimates are descriptive. Treasury reinvestment, equity drawdowns and the differing sample windows argue against underwriting either estimate as a forward rate. Before funding, obtain current Treasury reinvestment yields, an approved forward equity assumption and executable cost estimates. The benchmark is a fixed Lab 14 comparison of global equity and corporate credit. It omits a dedicated reserve sleeve by construction. [BLS CPI](https://www.bls.gov/cpi/) · [Original benchmark](https://github.com/Mrigna01/FIN439Project2/blob/15a6d0a3dd1bf883e264aa1d3a0f18596ad5c03b/lab14.md)

## Point-in-time data card

- **Feature and source.** Real VT USD adjusted-close ratio over 12 months, less one, from the same archived Yahoo snapshot. It is a total-return proxy.
- **Observation and availability.** September 30, 2025 to September 30, 2026. The archived series was verified available October 22, 2026 at 19:41:10 UTC. The date-based gate treats October 22 as an end-of-day cutoff, 22 calendar days after the last observation. No earlier availability is assumed.
- **Cutoff and missing values.** At the November 17 cutoff, the signal is 16.45%. Before archive availability, the app refuses to evaluate the price vintage; fewer than 13 observations produce no signal. Missing, malformed or misaligned data stop evaluation.
- **Decision role.** Positive trend allows the paper recommendation to proceed if modeled rules pass. A nonpositive or missing trend puts the decision on hold. This simple review gate is a case design choice. It has no role in the optimizer or return forecasts. The single vintage cannot establish how provider-adjusted history looked on earlier dates, a predictive edge, or an investable backtest.

## Stress evidence

The [generated report](../data/decision-output.md) uses the same engine as the app. One change at a time is applied to the 60-return, 10 bp, 4%-reserve case. The fixed check answers whether the original pilot survives; the fresh search answers whether a different five-point allocation qualifies. Lower VT estimates and higher costs separately fail the original mix. The 36-return window keeps the original feasible and changes the lowest-risk weights. The 80% reserve stress has no feasible result. An unchecked mandate rule remains open across all scenarios.

## Locked Changed-Input Record

**Pending human AI-off prediction and run.** The 17 bp cost case is reserved and has not been run. See the [prediction worksheet](locked-prediction-template.md).

The [original prediction commit](https://github.com/Mrigna01/FIN439Project2/commit/5e4320622c5c438109794c43b3cbd900791dbf50) is timestamped November 17 at 21:10:38 UTC and explicitly identifies the 4% to 80% prediction as AI-assisted. The [results commit](https://github.com/Mrigna01/FIN439Project2/commit/947645ac1cbe8e013a99fca9087673b6bc60be93) already contained results at 21:11:49 UTC. The [later prediction edit](https://github.com/Mrigna01/FIN439Project2/commit/af9bd3b5117bb19c18b0dd6ea792ea439ebc6e88) changed the wording at 21:34:14 UTC after the results existed. None establishes an AI-off prediction. This package does not rely on the later lab narrative as proof of a human partner run.

## Material AI uses

| Date | Tool and exposed information | Use and disposition | Check |
|---|---|---|---|
| 2026-11-17 | ChatGPT through Codex; exact model version not exposed | Adapted lab code, introduced uniform client cost, rule verdicts and common stress execution. Qualified the old pilot as paper-only. | Independent two-asset risk calculation, exact-boundary and cost tests, and app/report comparisons. |
| 2026-11-17 | ChatGPT through Codex; exact model version not exposed | Checked the prior assumption that an unchanged VT stress allocation was adequate. The earlier gross-style test left 5.51%; the modeled 10 bp base charge moves the same fixed stress to 5.41%. | Generated report and fixed-weight stress test; reviewed the original Lab 15 outputs. |
| 2026-11-17 | ChatGPT through Codex; exact model version not exposed | Adapted the lab cutoff concept to the real archived VT series, drafted supporting documents and recording scripts. Rejected later wording as proof of a timely or human-authored lab prediction. | Tested archive cutoff and checked the GitHub commit objects and date order. |
