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

As a cross-check, the U.S. Treasury's September 30, 2026 coupon-equivalent yield for a 13-week bill was 4.13%. That is a relevant reinvestment reference for SGOV's short maturity, with a different measurement basis than its 3.72% five-year historical fund estimate. The October 14 BLS release reported September 12-month CPI-U inflation of 3.7%, above the 2.50% case input. That realized reading is not a five-year inflation expectation. The comparisons explain why the modeled hurdle and historical returns should be reviewed before allocating capital. Neither source feeds the optimizer. [Treasury September 2026 bill rates](https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?field_tdr_date_value_month=202609&type=daily_treasury_bill_rates) · [BLS September CPI release](https://www.bls.gov/news.release/archives/cpi_10142026.htm)

## Point-in-time data card

- **Feature and source.** Real VT USD adjusted-close ratio over 12 months, less one, from the same archived Yahoo snapshot. It is a total-return proxy.
- **Observation and availability.** September 30, 2025 to September 30, 2026. The archived series was verified available October 22, 2026 at 19:41:10 UTC. The date-based gate treats October 22 as an end-of-day cutoff, 22 calendar days after the last observation. No earlier availability is assumed.
- **Cutoff and missing values.** At the November 17 cutoff, the signal is 16.45%. Before archive availability, the app refuses to evaluate the price vintage; fewer than 13 observations produce no signal. Missing, malformed or misaligned data stop evaluation.
- **Decision role.** Positive trend allows the paper recommendation to proceed if modeled rules pass. A nonpositive or missing trend puts the decision on hold. This simple review gate is a case design choice. It has no role in the optimizer or return forecasts. The single vintage cannot establish how provider-adjusted history looked on earlier dates, a predictive edge, or an investable backtest.

## Stress evidence

The [generated report](../data/decision-output.md) uses the same engine as the app. One change at a time is applied to the 60-return, 10 bp, 4%-reserve case. The fixed check answers whether the original pilot survives; the fresh search answers whether a different five-point allocation qualifies. Lower VT estimates and higher costs separately fail the original mix. The 36-return window keeps the original feasible and changes the lowest-risk weights. The 80% reserve stress has no feasible result. Five-day liquidity, account permissions, and annual cumulative turnover remain unestablished across the scenarios.

## Locked Changed-Input Record
Authored at (UTC): 2026-11-19T22:23:08Z 

Input change:
Additional annual cost increases from 10 bp to 17 bp. All other default inputs remain fixed.

Expected fixed-weight net return:
I expect net return to decrease by 0.07 percentage points, from approximately 5.66% to 5.59%, because the additional annual cost increases by 7 basis points.

Expected optimized allocation and risk:
I expect the allocation to remain 75% SGOV and 25% VT, with annual volatility around 3.82%. The original minimum-volatility portfolio should still meet the return target, and the uniform cost increase does not change the risk estimates.

Decision threshold:
The net-return target is 5.50%. I expect the original portfolio to remain above it, with a smaller cushion of approximately 0.09 percentage points.

Expected committee action:
I would continue the paper pilot with funding held. The modeled return and reserve checks should still pass, but forward return assumptions and operational mandate checks still need verification.

Prediction snapshot:
https://github.com/Mrigna01/FIN439-Campus-Reserve/commit/27d745222fe4b6c37c0058303c4ae071a6f1e398

### Actual practice results and comparison

Execution timestamp recorded before run (UTC): 2026-11-19T22:41:22Z
Elapsed time: 0.073 seconds

The 17 bp report ran from the Campus Reserve repository using Python 3.13.18 in the original lab project's virtual environment (`FIN439Project2/.venv`).

Command:
`python report.py --cost-bp 17 > data/locked-cost-result.md`

Actual result:
Increasing annual cost from 10 to 17 bp reduced the
original portfolio’s estimated net return from 5.66%
to 5.59%, a decrease of 0.07 percentage points.
The optimized allocation remained 75% SGOV and 25% VT.
Annual volatility remained 3.82%, and eligible reserves
remained 75%. Feasible grid allocations decreased
from 392 to 380 out of 1,771.

Comparison with prediction:
The result matched the practice prediction. The uniform
cost increase reduced net return without changing estimated
risk. The original minimum-volatility allocation still
passed the return hurdle, so it remained the selected mix.

Decision impact:
Continue the paper pilot with funding held. The estimated
net return remains approximately 0.09 percentage points
above the 5.50% target. Operational mandate checks and
forward return assumptions still need verification.

Evidence:
[Actual experiment output](../data/locked-cost-result.md)
[Default baseline](../data/decision-output.md)

## Execution and cold run

On November 17, 2026, my partner ran an authenticated fresh clone of [the app evidence commit](https://github.com/Mrigna01/FIN439-Campus-Reserve/commit/932aab6a1d71fe7de4fd93e05a998ab4f4e66306) in a disposable folder on macOS ARM64. Python 3.13.18 and Streamlit 1.67.0 were used. The clean run found no setup failure. It tested the README procedure with the supported interpreter on PATH.

| Command or check | Result | Wall time |
|---|---|---:|
| `git clone` | New folder from the private GitHub remote | 0.59 s |
| `python3.13 -m venv .venv` | Created an independent environment | 1.75 s |
| `python -m pip install -r requirements.txt` | Installed successfully | 10.59 s |
| `python -m unittest discover -s tests -v` | 10 passed, including interactive Streamlit default, cost and reserve checks | 13.32 s |
| `python report.py` followed by `cmp` | Regenerated report matched checked-in output byte for byte | 0.06 s for regeneration |
| `python -m streamlit run app.py` headless on localhost | Health endpoint and root page returned successfully | 0.60 s to health response |
| Whole cold run | Passed | 27.53 s |

The earlier development run caught Streamlit resolving the test script path relative to the test file. Resolving the app path from the project root fixed it. The fresh run covered exact cost and reserve boundaries, the two baseline failures, weight validity, a hand-worked covariance example, bad price inputs, exclusion before vintage availability, an infeasible reserve floor, and report/app agreement on decision numbers.

## Operational mandate evidence (November 19, 2026)

The [Campus mandate](https://github.com/Mrigna01/FIN439Project2/blob/15a6d0a3dd1bf883e264aa1d3a0f18596ad5c03b/lab13.md#project-2--own-client-mandate) specifies $10,000 quarterly, cash or daily-liquid government securities for reserves, at least 90% redeemable within five business days, an 8% aggregate company cap with cash, U.S. Treasury and diversified-fund exemptions, and annual rebalancing with approval when annual turnover is above 25%. It supplies neither actual dates nor actual account holdings, orders or permissions.

The [saved evidence](../data/operational-evidence.json) records source URLs, measurement dates, collection date and fund classifications. The [generated operational report](../data/decision-output.md#operational-mandate-evidence) shows the assumptions, calculated tables and next actions using the same functions as the app. This operational review is dated after the original portfolio decision and does not enter the point-in-time signal or portfolio search. The dated facts support the screening inputs. A normal payout schedule under a weekday calendar, a diversified-fund exemption interpretation and a no-flow rebalance are conditional. A historical volume screen uses mixed measurement windows and demonstrates trade scale without establishing execution or cash access.

The standalone payment illustration deducts opening cash from its own USD 1 million balance and applies the selected ETF weights to the remainder. Initial eligible securities are a subset of that invested balance. The main portfolio remains fully invested in ETFs, and its allocation, return, risk, reserve dollars, turnover and liquidity are independent of the illustration. The schedule does not establish payment readiness for the main portfolio.

Before funding, confirm the scholarship calendar, available balances and custodian cutoffs; confirm the issuer exemption interpretation and refresh holdings; reconcile cumulative turnover and annual review with a trade and flow ledger; and obtain execution and account permission evidence. Retain the paper pilot and funding hold.

Local automated verification in the original lab virtual environment passed all 10 pre-change tests and all 17 post-change tests. The expanded suite exercised cash timing and sale losses, incomplete issuer mapping, the exact turnover boundary and changes to the Streamlit controls. The generated default report matched the saved report byte for byte.

## Forward assumptions (November 19, 2026)

The [source record](../data/forward-assumptions.json) and [separate forward report](../data/forward-output.md) distinguish the input vintages, publication information, retrieval and analysis dates. Invesco’s USD arithmetic index total returns are used as nominal before-fund-expense proxies. The inputs deduct the provider expense ratios once. SGOV and SCHR use the older nearer-term-maturity index categories, while USIG and VT use the newer broad corporate and global equity estimates. The November 18 bill yield and dated fund yields are cross-checks. The optimizer uses historical ETF covariance and retains the 2.50% case inflation assumption and 5.50% net annual screen. A modeled pass cannot demonstrate rolling five-year CPI + 3% performance.

The base retains 10 bp of recurring additional annual costs. The 0 and 30 bp scenarios bracket that assumption. Schwab’s April 2026 retail pricing guide informs the commission illustration. The separate 5–20 bp spread/slippage range is an analyst assumption per dollar traded and is excluded from annual returns. Custody, advisory fees, execution and account terms remain unverified. The November 17 signal is displayed only as historical evidence. The forward screen holds funding pending updated monitoring and resolution of operational checks.

## Material AI uses

| Date | Tool and exposed information | Use and disposition | Check |
|---|---|---|---|
| 2026-11-17 | ChatGPT through Codex (GPT-6.2-Sol, default) | Adapted lab code, introduced uniform client cost, rule verdicts and common stress execution. Qualified the old pilot as paper-only. | Independent two-asset risk calculation, exact-boundary and cost tests, and app/report comparisons. |
| 2026-11-17 | ChatGPT through Codex (GPT-6.2-Sol, default) | Checked the prior assumption that an unchanged VT stress allocation was adequate. The earlier gross-style test left 5.51%; the modeled 10 bp base charge moves the same fixed stress to 5.41%. | Generated report and fixed-weight stress test; reviewed the original Lab 15 outputs. |
| 2026-11-17 | ChatGPT through Codex (GPT-6.2-Sol, default) | Adapted the lab cutoff concept to the real archived VT series, drafted supporting documents and recording scripts. | Tested archive cutoff and checked the GitHub commit objects and date order. |
| 2026-11-19 | ChatGPT through Codex | Reviewed the original mandate and official fund and settlement sources. Implemented the operational schedule, issuer bound, turnover and liquidity screens plus their tests and documentation. Used dated fund evidence and explicit fictional starting conditions. | Baseline and expanded automated tests, saved report comparison and Streamlit control checks. This operational review was AI-assisted. |
| 2026-11-19 | ChatGPT through Codex | Researched and documented the forward return proxies and cost references, integrated the optional scenario through the existing engine, and added regression and scenario tests. | Checked publication and measurement dates and arithmetic versus geometric columns. Compared app and generated output. The forward work was AI-assisted. |
