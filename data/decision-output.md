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
| Scholarship payment-date cash availability | Passes under stated assumptions | Fails | Passes under stated assumptions |
| Corporate issuer exposure ≤ 8% under case exemptions | Passes under stated assumptions | Passes under stated assumptions | Passes under stated assumptions |
| Illustrative rebalance turnover (approval above 25%) | Approval required | Approval required | Passes under stated assumptions |
| At least 90% redeemable within five business days | Not established | Not established | Not established |
| Account permissions | Not established | Not established | Not established |
| Annual review and cumulative turnover | Not established | Not established | Not established |

## Operational mandate evidence

### Equal weight

**Scholarship payments · Passes under stated assumptions.** Four illustrative quarters use separate cash funded from the USD 1 million reserve, with ETF weights applied to the remainder. Each sale targets USD 10,000 in pre-shock units from SGOV/SCHR pro rata, capped at remaining holdings. No automatic top-up or sale of other ETFs.

Sales are planned two weekdays early. Weekend payments roll forward to Monday. An illustrative weekday calendar omits exchange and banking holidays, cutoffs and transfer delays. Normal proceeds are usable at T+1, consistent with standard [ETF settlement](https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins/new-t1-settlement-cycle-what-investors-need-know-investor-bulletin). Delay assumes T+3; market loss assumes 5% lower sale prices for the same units throughout. No growth, dividends, account fees, execution costs or late payment catch-up are modeled. Opening cash is prior closing cash before crediting newly available proceeds.

Before funding, confirm actual dates, balances, order execution, settlement and payment cutoffs with the custodian.

**Normal · Passes under stated assumptions**

| Payment | Opening cash | Sale date | Sale at reference prices | Proceeds | Available | Newly available cash | Due | Paid | Closing cash | Shortfall |
|---|---|---|---|---|---|---|---|---|---|---|
| 2027-03-15 | \$0.00 | 2027-03-11 | SGOV \$5,000.00, SCHR \$5,000.00 | \$10,000.00 | 2027-03-12 | \$10,000.00 | \$10,000.00 | \$10,000.00 | \$0.00 | \$0.00 |
| 2027-06-15 | \$0.00 | 2027-06-11 | SGOV \$5,000.00, SCHR \$5,000.00 | \$10,000.00 | 2027-06-14 | \$10,000.00 | \$10,000.00 | \$10,000.00 | \$0.00 | \$0.00 |
| 2027-09-15 | \$0.00 | 2027-09-13 | SGOV \$5,000.00, SCHR \$5,000.00 | \$10,000.00 | 2027-09-14 | \$10,000.00 | \$10,000.00 | \$10,000.00 | \$0.00 | \$0.00 |
| 2027-12-15 | \$0.00 | 2027-12-13 | SGOV \$5,000.00, SCHR \$5,000.00 | \$10,000.00 | 2027-12-14 | \$10,000.00 | \$10,000.00 | \$10,000.00 | \$0.00 | \$0.00 |

**Delayed proceeds · Fails**

| Payment | Opening cash | Sale date | Sale at reference prices | Proceeds | Available | Newly available cash | Due | Paid | Closing cash | Shortfall |
|---|---|---|---|---|---|---|---|---|---|---|
| 2027-03-15 | \$0.00 | 2027-03-11 | SGOV \$5,000.00, SCHR \$5,000.00 | \$10,000.00 | 2027-03-16 | \$0.00 | \$10,000.00 | \$0.00 | \$0.00 | \$10,000.00 |
| 2027-06-15 | \$0.00 | 2027-06-11 | SGOV \$5,000.00, SCHR \$5,000.00 | \$10,000.00 | 2027-06-16 | \$10,000.00 | \$10,000.00 | \$10,000.00 | \$0.00 | \$0.00 |
| 2027-09-15 | \$0.00 | 2027-09-13 | SGOV \$5,000.00, SCHR \$5,000.00 | \$10,000.00 | 2027-09-16 | \$10,000.00 | \$10,000.00 | \$10,000.00 | \$0.00 | \$0.00 |
| 2027-12-15 | \$0.00 | 2027-12-13 | SGOV \$5,000.00, SCHR \$5,000.00 | \$10,000.00 | 2027-12-16 | \$10,000.00 | \$10,000.00 | \$10,000.00 | \$0.00 | \$0.00 |

**Market loss · Fails**

| Payment | Opening cash | Sale date | Sale at reference prices | Proceeds | Available | Newly available cash | Due | Paid | Closing cash | Shortfall |
|---|---|---|---|---|---|---|---|---|---|---|
| 2027-03-15 | \$0.00 | 2027-03-11 | SGOV \$5,000.00, SCHR \$5,000.00 | \$9,500.00 | 2027-03-12 | \$9,500.00 | \$10,000.00 | \$9,500.00 | \$0.00 | \$500.00 |
| 2027-06-15 | \$0.00 | 2027-06-11 | SGOV \$5,000.00, SCHR \$5,000.00 | \$9,500.00 | 2027-06-14 | \$9,500.00 | \$10,000.00 | \$9,500.00 | \$0.00 | \$500.00 |
| 2027-09-15 | \$0.00 | 2027-09-13 | SGOV \$5,000.00, SCHR \$5,000.00 | \$9,500.00 | 2027-09-14 | \$9,500.00 | \$10,000.00 | \$9,500.00 | \$0.00 | \$500.00 |
| 2027-12-15 | \$0.00 | 2027-12-13 | SGOV \$5,000.00, SCHR \$5,000.00 | \$9,500.00 | 2027-12-14 | \$9,500.00 | \$10,000.00 | \$9,500.00 | \$0.00 | \$500.00 |

**Issuer cap · Passes under stated assumptions.** Mapped company exposure: none mapped. Unmapped portfolio share 0.177%; conservative single-company upper bound 0.177% versus 8%.

The [Campus mandate](https://github.com/Mrigna01/FIN439Project2/blob/15a6d0a3dd1bf883e264aa1d3a0f18596ad5c03b/lab13.md#project-2--own-client-mandate) exempts cash, U.S. Treasury securities and diversified funds. For other holdings, multiply fund weight by each mapped company weight and sum by company across funds. The ETF sponsor is not substituted for underlying issuers. The upper bound assigns all unmapped weight to the largest mapped company (or one new company). Before funding, confirm exemption interpretation and refresh holdings and company mappings for nonexempt positions.

| Fund | Holdings / policy as of | Dated evidence |
|---|---|---|
| SGOV | 2026-11-18 | [Provider](https://www.ishares.com/us/products/314116/sgov) · Provider sector breakdown: 99.47% U.S. Treasury debt and 0.53% investment company. Keep 0.54% unmapped (rounded-up allowance). Corporate issuer identities for that residual were unavailable. |
| SCHR | 2026-09-30 | [Provider](https://www.schwabassetmanagement.com/products/schr?page=0) · Tracks the U.S. Treasury 3–10 Year Index. September security types show 99.84% U.S. government securities and 0.16% other investment companies. November 16 holdings show Treasury notes and a USD line; the calculation uses the older allocation and conservatively leaves 0.17% unclassified. |
| USIG | 2026-11-18 | [Provider](https://www.ishares.com/us/products/239460/ishares-credit-bond-etf) · Broad investment-grade corporate bond index; provider reported 11,696 holdings and describes diversified credit exposure. Treat as a diversified fund under the case exemption. Holding count is a diversification indicator, not an issuer count. |
| VT | 2026-09-30 | [Provider](https://fund-docs.vanguard.com/F3141.pdf) · FTSE Global All Cap exposure with 10,185 stocks across developed and emerging markets. Apply the case diversified-fund exemption. |

**Rebalance turnover · Approval required.** 35.00% one-way turnover (half the sum of absolute weight changes), on USD 1 million with no external flows. Approval applies strictly above 25%. The starting weights are illustrative. Initial funding and scholarship sales are outside this rebalance. Annual review and cumulative turnover: Not established. Obtain beginning holdings, dated trade and flow records, an agreed annual turnover convention, annual review evidence and any required approval.

| Fund | Starting | Proposed | Buy | Sell |
|---|---|---|---|---|
| SGOV | \$600,000.00 | \$250,000.00 | \$0.00 | \$350,000.00 |
| SCHR | \$100,000.00 | \$250,000.00 | \$150,000.00 | \$0.00 |
| USIG | \$100,000.00 | \$250,000.00 | \$150,000.00 | \$0.00 |
| VT | \$200,000.00 | \$250,000.00 | \$50,000.00 | \$0.00 |

**Five-business-day liquidity · Not established.** The dated volume proxy covers 100.0% of portfolio value in the normal case and 93.7% in the stress case, versus the 90% requirement.

Compare full sleeve sales on the USD 1 million portfolio. Normal uses 1% of observed daily share volume over four trading sessions with T+1. Stress uses 10% of observed volume, the same 1% participation and two trading sessions with T+3. Capacity is capped at each sleeve. Missing volume contributes no capacity to this evidence screen. SCHR uses a historical single-day observation, and VT uses a historical provider view. Share estimates for funds without a provider price use the 2026-09-30 adjusted-price archive as a scale proxy. Capacity uses reference prices and excludes market impact and price gaps. Historical volume and a displayed spread cannot establish depth, fills, execution costs, access to proceeds or reliable stressed liquidity. ETF holders generally sell in the secondary market. Before funding, obtain fresh multi-session volume, quotes, depth and broker execution and cash-release confirmation for the full portfolio.

Provider spreads are 30-day median quoted spreads relative to the midpoint ([measurement definition](https://www.ecfr.gov/current/title-17/chapter-II/part-270/section-270.6c-11)). Evidence retrieved 2026-11-19 for this operational review, after the original investment decision date.

| Fund | Liquidation USD | Reference price | Approx. shares | % daily shares | Volume evidence | Median spread | Normal capacity | Stress capacity |
|---|---|---|---|---|---|---|---|---|
| SGOV | \$250,000.00 | \$100.60 | 2,485 | 0.01% | [2026-11-18](https://www.ishares.com/us/products/314116/sgov) · 24,331,732 shares · 30-day average | 0.01% (2026-11-18) | \$250,000.00 | \$250,000.00 |
| SCHR | \$250,000.00 | \$24.08 | 10,382 | 0.18% | [2026-09-10](https://www.schwabassetmanagement.com/products/schr?page=0) · 5,621,956 shares · single-day volume; opening price; historical | 0.04% (2026-08-10 to 2026-09-09) | \$250,000.00 | \$250,000.00 |
| USIG | \$250,000.00 | \$49.05 | 5,097 | 0.27% | [2026-11-18](https://www.ishares.com/us/products/239460/ishares-credit-bond-etf) · 1,902,857 shares · 30-day average | 0.02% (2026-11-18) | \$250,000.00 | \$186,670.27 |
| VT | \$250,000.00 | \$158.73 | 1,575 | 0.06% | [2026-10-08](https://advisors.vanguard.com/investments/products/vt/vanguard-total-world-stock-etf) · 2,597,924.93 shares · 25-day average shown with October 8 close; historical cached provider view | 0.01% (2026-10-08) | \$250,000.00 | \$250,000.00 |

**Account permissions · Not established.** No actual account documentation exists in the case. Before funding, obtain custodian confirmation of the permitted instruments, authorized traders and disbursement signatories, approval limits, and cash transfer rules. Keep credentials and account identifiers out of the repository.

### 60/40 benchmark

**Scholarship payments · Fails.** Four illustrative quarters use separate cash funded from the USD 1 million reserve, with ETF weights applied to the remainder. Each sale targets USD 10,000 in pre-shock units from SGOV/SCHR pro rata, capped at remaining holdings. No automatic top-up or sale of other ETFs.

Sales are planned two weekdays early. Weekend payments roll forward to Monday. An illustrative weekday calendar omits exchange and banking holidays, cutoffs and transfer delays. Normal proceeds are usable at T+1, consistent with standard [ETF settlement](https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins/new-t1-settlement-cycle-what-investors-need-know-investor-bulletin). Delay assumes T+3; market loss assumes 5% lower sale prices for the same units throughout. No growth, dividends, account fees, execution costs or late payment catch-up are modeled. Opening cash is prior closing cash before crediting newly available proceeds.

Before funding, confirm actual dates, balances, order execution, settlement and payment cutoffs with the custodian.

**Normal · Fails**

| Payment | Opening cash | Sale date | Sale at reference prices | Proceeds | Available | Newly available cash | Due | Paid | Closing cash | Shortfall |
|---|---|---|---|---|---|---|---|---|---|---|
| 2027-03-15 | \$0.00 | 2027-03-11 | — | \$0.00 | — | \$0.00 | \$10,000.00 | \$0.00 | \$0.00 | \$10,000.00 |
| 2027-06-15 | \$0.00 | 2027-06-11 | — | \$0.00 | — | \$0.00 | \$10,000.00 | \$0.00 | \$0.00 | \$10,000.00 |
| 2027-09-15 | \$0.00 | 2027-09-13 | — | \$0.00 | — | \$0.00 | \$10,000.00 | \$0.00 | \$0.00 | \$10,000.00 |
| 2027-12-15 | \$0.00 | 2027-12-13 | — | \$0.00 | — | \$0.00 | \$10,000.00 | \$0.00 | \$0.00 | \$10,000.00 |

**Delayed proceeds · Fails**

| Payment | Opening cash | Sale date | Sale at reference prices | Proceeds | Available | Newly available cash | Due | Paid | Closing cash | Shortfall |
|---|---|---|---|---|---|---|---|---|---|---|
| 2027-03-15 | \$0.00 | 2027-03-11 | — | \$0.00 | — | \$0.00 | \$10,000.00 | \$0.00 | \$0.00 | \$10,000.00 |
| 2027-06-15 | \$0.00 | 2027-06-11 | — | \$0.00 | — | \$0.00 | \$10,000.00 | \$0.00 | \$0.00 | \$10,000.00 |
| 2027-09-15 | \$0.00 | 2027-09-13 | — | \$0.00 | — | \$0.00 | \$10,000.00 | \$0.00 | \$0.00 | \$10,000.00 |
| 2027-12-15 | \$0.00 | 2027-12-13 | — | \$0.00 | — | \$0.00 | \$10,000.00 | \$0.00 | \$0.00 | \$10,000.00 |

**Market loss · Fails**

| Payment | Opening cash | Sale date | Sale at reference prices | Proceeds | Available | Newly available cash | Due | Paid | Closing cash | Shortfall |
|---|---|---|---|---|---|---|---|---|---|---|
| 2027-03-15 | \$0.00 | 2027-03-11 | — | \$0.00 | — | \$0.00 | \$10,000.00 | \$0.00 | \$0.00 | \$10,000.00 |
| 2027-06-15 | \$0.00 | 2027-06-11 | — | \$0.00 | — | \$0.00 | \$10,000.00 | \$0.00 | \$0.00 | \$10,000.00 |
| 2027-09-15 | \$0.00 | 2027-09-13 | — | \$0.00 | — | \$0.00 | \$10,000.00 | \$0.00 | \$0.00 | \$10,000.00 |
| 2027-12-15 | \$0.00 | 2027-12-13 | — | \$0.00 | — | \$0.00 | \$10,000.00 | \$0.00 | \$0.00 | \$10,000.00 |

**Issuer cap · Passes under stated assumptions.** Mapped company exposure: none mapped. Unmapped portfolio share 0.000%; conservative single-company upper bound 0.000% versus 8%.

The [Campus mandate](https://github.com/Mrigna01/FIN439Project2/blob/15a6d0a3dd1bf883e264aa1d3a0f18596ad5c03b/lab13.md#project-2--own-client-mandate) exempts cash, U.S. Treasury securities and diversified funds. For other holdings, multiply fund weight by each mapped company weight and sum by company across funds. The ETF sponsor is not substituted for underlying issuers. The upper bound assigns all unmapped weight to the largest mapped company (or one new company). Before funding, confirm exemption interpretation and refresh holdings and company mappings for nonexempt positions.

| Fund | Holdings / policy as of | Dated evidence |
|---|---|---|
| USIG | 2026-11-18 | [Provider](https://www.ishares.com/us/products/239460/ishares-credit-bond-etf) · Broad investment-grade corporate bond index; provider reported 11,696 holdings and describes diversified credit exposure. Treat as a diversified fund under the case exemption. Holding count is a diversification indicator, not an issuer count. |
| VT | 2026-09-30 | [Provider](https://fund-docs.vanguard.com/F3141.pdf) · FTSE Global All Cap exposure with 10,185 stocks across developed and emerging markets. Apply the case diversified-fund exemption. |

**Rebalance turnover · Approval required.** 70.00% one-way turnover (half the sum of absolute weight changes), on USD 1 million with no external flows. Approval applies strictly above 25%. The starting weights are illustrative. Initial funding and scholarship sales are outside this rebalance. Annual review and cumulative turnover: Not established. Obtain beginning holdings, dated trade and flow records, an agreed annual turnover convention, annual review evidence and any required approval.

| Fund | Starting | Proposed | Buy | Sell |
|---|---|---|---|---|
| SGOV | \$600,000.00 | \$0.00 | \$0.00 | \$600,000.00 |
| SCHR | \$100,000.00 | \$0.00 | \$0.00 | \$100,000.00 |
| USIG | \$100,000.00 | \$400,000.00 | \$300,000.00 | \$0.00 |
| VT | \$200,000.00 | \$600,000.00 | \$400,000.00 | \$0.00 |

**Five-business-day liquidity · Not established.** The dated volume proxy covers 100.0% of portfolio value in the normal case and 78.7% in the stress case, versus the 90% requirement.

Compare full sleeve sales on the USD 1 million portfolio. Normal uses 1% of observed daily share volume over four trading sessions with T+1. Stress uses 10% of observed volume, the same 1% participation and two trading sessions with T+3. Capacity is capped at each sleeve. Missing volume contributes no capacity to this evidence screen. SCHR uses a historical single-day observation, and VT uses a historical provider view. Share estimates for funds without a provider price use the 2026-09-30 adjusted-price archive as a scale proxy. Capacity uses reference prices and excludes market impact and price gaps. Historical volume and a displayed spread cannot establish depth, fills, execution costs, access to proceeds or reliable stressed liquidity. ETF holders generally sell in the secondary market. Before funding, obtain fresh multi-session volume, quotes, depth and broker execution and cash-release confirmation for the full portfolio.

Provider spreads are 30-day median quoted spreads relative to the midpoint ([measurement definition](https://www.ecfr.gov/current/title-17/chapter-II/part-270/section-270.6c-11)). Evidence retrieved 2026-11-19 for this operational review, after the original investment decision date.

| Fund | Liquidation USD | Reference price | Approx. shares | % daily shares | Volume evidence | Median spread | Normal capacity | Stress capacity |
|---|---|---|---|---|---|---|---|---|
| USIG | \$400,000.00 | \$49.05 | 8,155 | 0.43% | [2026-11-18](https://www.ishares.com/us/products/239460/ishares-credit-bond-etf) · 1,902,857 shares · 30-day average | 0.02% (2026-11-18) | \$400,000.00 | \$186,670.27 |
| VT | \$600,000.00 | \$158.73 | 3,780 | 0.15% | [2026-10-08](https://advisors.vanguard.com/investments/products/vt/vanguard-total-world-stock-etf) · 2,597,924.93 shares · 25-day average shown with October 8 close; historical cached provider view | 0.01% (2026-10-08) | \$600,000.00 | \$600,000.00 |

**Account permissions · Not established.** No actual account documentation exists in the case. Before funding, obtain custodian confirmation of the permitted instruments, authorized traders and disbursement signatories, approval limits, and cash transfer rules. Keep credentials and account identifiers out of the repository.

### Constrained

**Scholarship payments · Passes under stated assumptions.** Four illustrative quarters use separate cash funded from the USD 1 million reserve, with ETF weights applied to the remainder. Each sale targets USD 10,000 in pre-shock units from SGOV/SCHR pro rata, capped at remaining holdings. No automatic top-up or sale of other ETFs.

Sales are planned two weekdays early. Weekend payments roll forward to Monday. An illustrative weekday calendar omits exchange and banking holidays, cutoffs and transfer delays. Normal proceeds are usable at T+1, consistent with standard [ETF settlement](https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins/new-t1-settlement-cycle-what-investors-need-know-investor-bulletin). Delay assumes T+3; market loss assumes 5% lower sale prices for the same units throughout. No growth, dividends, account fees, execution costs or late payment catch-up are modeled. Opening cash is prior closing cash before crediting newly available proceeds.

Before funding, confirm actual dates, balances, order execution, settlement and payment cutoffs with the custodian.

**Normal · Passes under stated assumptions**

| Payment | Opening cash | Sale date | Sale at reference prices | Proceeds | Available | Newly available cash | Due | Paid | Closing cash | Shortfall |
|---|---|---|---|---|---|---|---|---|---|---|
| 2027-03-15 | \$0.00 | 2027-03-11 | SGOV \$10,000.00 | \$10,000.00 | 2027-03-12 | \$10,000.00 | \$10,000.00 | \$10,000.00 | \$0.00 | \$0.00 |
| 2027-06-15 | \$0.00 | 2027-06-11 | SGOV \$10,000.00 | \$10,000.00 | 2027-06-14 | \$10,000.00 | \$10,000.00 | \$10,000.00 | \$0.00 | \$0.00 |
| 2027-09-15 | \$0.00 | 2027-09-13 | SGOV \$10,000.00 | \$10,000.00 | 2027-09-14 | \$10,000.00 | \$10,000.00 | \$10,000.00 | \$0.00 | \$0.00 |
| 2027-12-15 | \$0.00 | 2027-12-13 | SGOV \$10,000.00 | \$10,000.00 | 2027-12-14 | \$10,000.00 | \$10,000.00 | \$10,000.00 | \$0.00 | \$0.00 |

**Delayed proceeds · Fails**

| Payment | Opening cash | Sale date | Sale at reference prices | Proceeds | Available | Newly available cash | Due | Paid | Closing cash | Shortfall |
|---|---|---|---|---|---|---|---|---|---|---|
| 2027-03-15 | \$0.00 | 2027-03-11 | SGOV \$10,000.00 | \$10,000.00 | 2027-03-16 | \$0.00 | \$10,000.00 | \$0.00 | \$0.00 | \$10,000.00 |
| 2027-06-15 | \$0.00 | 2027-06-11 | SGOV \$10,000.00 | \$10,000.00 | 2027-06-16 | \$10,000.00 | \$10,000.00 | \$10,000.00 | \$0.00 | \$0.00 |
| 2027-09-15 | \$0.00 | 2027-09-13 | SGOV \$10,000.00 | \$10,000.00 | 2027-09-16 | \$10,000.00 | \$10,000.00 | \$10,000.00 | \$0.00 | \$0.00 |
| 2027-12-15 | \$0.00 | 2027-12-13 | SGOV \$10,000.00 | \$10,000.00 | 2027-12-16 | \$10,000.00 | \$10,000.00 | \$10,000.00 | \$0.00 | \$0.00 |

**Market loss · Fails**

| Payment | Opening cash | Sale date | Sale at reference prices | Proceeds | Available | Newly available cash | Due | Paid | Closing cash | Shortfall |
|---|---|---|---|---|---|---|---|---|---|---|
| 2027-03-15 | \$0.00 | 2027-03-11 | SGOV \$10,000.00 | \$9,500.00 | 2027-03-12 | \$9,500.00 | \$10,000.00 | \$9,500.00 | \$0.00 | \$500.00 |
| 2027-06-15 | \$0.00 | 2027-06-11 | SGOV \$10,000.00 | \$9,500.00 | 2027-06-14 | \$9,500.00 | \$10,000.00 | \$9,500.00 | \$0.00 | \$500.00 |
| 2027-09-15 | \$0.00 | 2027-09-13 | SGOV \$10,000.00 | \$9,500.00 | 2027-09-14 | \$9,500.00 | \$10,000.00 | \$9,500.00 | \$0.00 | \$500.00 |
| 2027-12-15 | \$0.00 | 2027-12-13 | SGOV \$10,000.00 | \$9,500.00 | 2027-12-14 | \$9,500.00 | \$10,000.00 | \$9,500.00 | \$0.00 | \$500.00 |

**Issuer cap · Passes under stated assumptions.** Mapped company exposure: none mapped. Unmapped portfolio share 0.405%; conservative single-company upper bound 0.405% versus 8%.

The [Campus mandate](https://github.com/Mrigna01/FIN439Project2/blob/15a6d0a3dd1bf883e264aa1d3a0f18596ad5c03b/lab13.md#project-2--own-client-mandate) exempts cash, U.S. Treasury securities and diversified funds. For other holdings, multiply fund weight by each mapped company weight and sum by company across funds. The ETF sponsor is not substituted for underlying issuers. The upper bound assigns all unmapped weight to the largest mapped company (or one new company). Before funding, confirm exemption interpretation and refresh holdings and company mappings for nonexempt positions.

| Fund | Holdings / policy as of | Dated evidence |
|---|---|---|
| SGOV | 2026-11-18 | [Provider](https://www.ishares.com/us/products/314116/sgov) · Provider sector breakdown: 99.47% U.S. Treasury debt and 0.53% investment company. Keep 0.54% unmapped (rounded-up allowance). Corporate issuer identities for that residual were unavailable. |
| VT | 2026-09-30 | [Provider](https://fund-docs.vanguard.com/F3141.pdf) · FTSE Global All Cap exposure with 10,185 stocks across developed and emerging markets. Apply the case diversified-fund exemption. |

**Rebalance turnover · Passes under stated assumptions.** 20.00% one-way turnover (half the sum of absolute weight changes), on USD 1 million with no external flows. Approval applies strictly above 25%. The starting weights are illustrative. Initial funding and scholarship sales are outside this rebalance. Annual review and cumulative turnover: Not established. Obtain beginning holdings, dated trade and flow records, an agreed annual turnover convention, annual review evidence and any required approval.

| Fund | Starting | Proposed | Buy | Sell |
|---|---|---|---|---|
| SGOV | \$600,000.00 | \$750,000.00 | \$150,000.00 | \$0.00 |
| SCHR | \$100,000.00 | \$0.00 | \$0.00 | \$100,000.00 |
| USIG | \$100,000.00 | \$0.00 | \$0.00 | \$100,000.00 |
| VT | \$200,000.00 | \$250,000.00 | \$50,000.00 | \$0.00 |

**Five-business-day liquidity · Not established.** The dated volume proxy covers 100.0% of portfolio value in the normal case and 100.0% in the stress case, versus the 90% requirement.

Compare full sleeve sales on the USD 1 million portfolio. Normal uses 1% of observed daily share volume over four trading sessions with T+1. Stress uses 10% of observed volume, the same 1% participation and two trading sessions with T+3. Capacity is capped at each sleeve. Missing volume contributes no capacity to this evidence screen. SCHR uses a historical single-day observation, and VT uses a historical provider view. Share estimates for funds without a provider price use the 2026-09-30 adjusted-price archive as a scale proxy. Capacity uses reference prices and excludes market impact and price gaps. Historical volume and a displayed spread cannot establish depth, fills, execution costs, access to proceeds or reliable stressed liquidity. ETF holders generally sell in the secondary market. Before funding, obtain fresh multi-session volume, quotes, depth and broker execution and cash-release confirmation for the full portfolio.

Provider spreads are 30-day median quoted spreads relative to the midpoint ([measurement definition](https://www.ecfr.gov/current/title-17/chapter-II/part-270/section-270.6c-11)). Evidence retrieved 2026-11-19 for this operational review, after the original investment decision date.

| Fund | Liquidation USD | Reference price | Approx. shares | % daily shares | Volume evidence | Median spread | Normal capacity | Stress capacity |
|---|---|---|---|---|---|---|---|---|
| SGOV | \$750,000.00 | \$100.60 | 7,455 | 0.03% | [2026-11-18](https://www.ishares.com/us/products/314116/sgov) · 24,331,732 shares · 30-day average | 0.01% (2026-11-18) | \$750,000.00 | \$750,000.00 |
| VT | \$250,000.00 | \$158.73 | 1,575 | 0.06% | [2026-10-08](https://advisors.vanguard.com/investments/products/vt/vanguard-total-world-stock-etf) · 2,597,924.93 shares · 25-day average shown with October 8 close; historical cached provider view | 0.01% (2026-10-08) | \$250,000.00 | \$250,000.00 |

**Account permissions · Not established.** No actual account documentation exists in the case. Before funding, obtain custodian confirmation of the permitted instruments, authorized traders and disbursement signatories, approval limits, and cash transfer rules. Keep credentials and account identifiers out of the repository.


## One-at-a-time stresses

The fixed column holds the original constrained weights. Risk uses each scenario's inputs.

| Input | Original weights | Reoptimized | New weights (SGOV/SCHR/USIG/VT) | Largest change | Action |
|---|---|---|---|---|---|
| VT estimate −1 percentage point | 5.41% net / 3.82% risk / 75% reserve · Fails modeled checks | 5.77% net / 4.55% risk / 70% reserve · Passes modeled checks | 70%/0%/0%/30% | 5 points | Review original weights before proceeding |
| Trailing 36 months | 8.29% net / 2.95% risk / 75% reserve · Passes modeled checks | 5.92% net / 1.21% risk / 90% reserve · Passes modeled checks | 90%/0%/0%/10% | 15 points | Paper pilot remains conditional |
| Additional cost 30 bp | 5.46% net / 3.82% risk / 75% reserve · Fails modeled checks | 5.87% net / 4.55% risk / 70% reserve · Passes modeled checks | 70%/0%/0%/30% | 5 points | Review original weights before proceeding |
| Reserve floor 80% | 5.66% net / 3.82% risk / 75% reserve · Fails modeled checks | No feasible grid allocation | — | — | Stop: no allocation passes the active constraints on the grid. |

### Operational checks by stress and allocation

Liquidity percentages are volume proxies. Account permissions are not established in every scenario.

| Scenario | Mix | Cash (normal) | Issuer cap | Turnover | Normal liquidity proxy |
|---|---|---|---|---|---|
| VT estimate −1 percentage point | Constrained | Passes under stated assumptions | Passes under stated assumptions | 20.00% · Passes under stated assumptions | 100.0% · Not established |
| VT estimate −1 percentage point | Original weights | Passes under stated assumptions | Passes under stated assumptions | 20.00% · Passes under stated assumptions | 100.0% · Not established |
| Trailing 36 months | Constrained | Passes under stated assumptions | Passes under stated assumptions | 30.00% · Approval required | 100.0% · Not established |
| Trailing 36 months | Original weights | Passes under stated assumptions | Passes under stated assumptions | 20.00% · Passes under stated assumptions | 100.0% · Not established |
| Additional cost 30 bp | Constrained | Passes under stated assumptions | Passes under stated assumptions | 20.00% · Passes under stated assumptions | 100.0% · Not established |
| Additional cost 30 bp | Original weights | Passes under stated assumptions | Passes under stated assumptions | 20.00% · Passes under stated assumptions | 100.0% · Not established |
| Reserve floor 80% | Original weights | Passes under stated assumptions | Passes under stated assumptions | 20.00% · Passes under stated assumptions | 100.0% · Not established |

Before funding, verify forward-looking assumptions, all open mandate rules and dated payouts. Hold if the VT signal is unavailable or nonpositive. Stop if the pilot mix misses the 5.50% estimated net target or the reserve floor.
