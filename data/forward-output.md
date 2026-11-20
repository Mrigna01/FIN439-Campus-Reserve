# Forward assumptions — illustrative

Analysis date 2026-11-19. Historical price vintage retrieved 2026-10-22T19:41:10.270903+00:00.
60 USD monthly returns from 2021-10-29 to 2026-09-30.
Net target 5.50%, reserve floor 4%, additional annual cost 10 bp, VT return shift +0 points.

November 17 historical pilot: 5.66% net / 3.82% risk / 75% reserve · Passes modeled checks. The forward Original weights row holds that mix fixed.
Historical VT signal: 16.45% from 2025-09-30 to 2026-09-30, archive available 2026-10-22.

**Forward source record.** Retrieved 2026-11-19 for the 2026-11-19 analysis.

Nominal USD annual arithmetic index total returns over a 10-year projection. Treat index returns as before ETF expenses. Fund-level inputs deduct each published expense ratio once.

Use the arithmetic column directly and convert percent to decimal. The geometric column is shown for context. The source forecasts are index-level proxies. Subtract the fund expense in basis points once and then deduct the portfolio-level recurring cost once. The arithmetic stress control is in percentage points.

| ETF | Index proxy | Arithmetic / geometric | Fund expense | Selected annual rate | Capital-market source | Fund source | Rationale and limitations |
|---|---|---|---|---|---|---|---|
| SGOV | Bloomberg U.S. short Treasuries | 3.20% / 3.20% | 9 bp | 3.11% | [Invesco 2026 Capital Market Assumptions — USD Q1 Update, Figure 6](https://www.invesco.com/content/dam/invesco/apac/en/pdf/insights/2026/april/2026-invesco-capital-market-assumptions-usd-q1-2026.pdf) · observed 2025-12-31 · published April 2026 edition; exact day unavailable | [iShares 0–3 Month Treasury Bond ETF product brief](https://www.blackrock.com/us/financial-professionals/literature/product-brief/ishares-us-treasury-bond-etfs-product-brief-en-us.pdf) · reference date 2026-09-30 · Exact publication day unavailable | Start with the 4.26% 13-week Treasury yield as a spot reference. Use the short-Treasury index projection for the base because rolling bills reinvest at future rates. The proxy need not match SGOV’s precise maturity range or seven-year horizon. |
| SCHR | Bloomberg intermediate U.S. Treasuries | 4.00% / 4.00% | 3 bp | 3.97% | [Invesco 2026 Capital Market Assumptions — USD Q1 Update, Figure 6](https://www.invesco.com/content/dam/invesco/apac/en/pdf/insights/2026/april/2026-invesco-capital-market-assumptions-usd-q1-2026.pdf) · observed 2025-12-31 · published April 2026 edition; exact day unavailable | [Schwab Intermediate-Term U.S. Treasury ETF fund profile](https://www.schwabassetmanagement.com/products/schr) · reference date 2026-09-30 · Live profile; separate publication date unavailable | Use the older, closer intermediate Treasury index proxy. Schwab reported 5.11% average yield to maturity on September 30 and 4.8 years effective duration on October 31, 2026. Yield to maturity describes the bonds at observed prices under yield assumptions. Rate moves, roll and reinvestment affect ETF total return. |
| USIG | Bloomberg U.S. investment-grade corporate bonds | 5.60% / 5.40% | 4 bp | 5.56% | [Invesco 2026 Capital Market Assumptions — USD Q3 Update, Figure 6](https://www.invesco.com/content/dam/invesco/emea/en/pdf/invesco-capital-market-assumption-usd.pdf) · observed 2026-06-30 · published 2026-10-12 | [iShares Broad USD Investment Grade Corporate Bond ETF fund profile](https://www.ishares.com/us/products/239460/ishares-credit-bond-etf) · reference date 2026-11-18 · Live profile; separate publication date unavailable | Use a broad investment-grade total-return index proxy. iShares reported 5.95% average yield to maturity and 6.09 years effective duration on November 18. Yield and distribution measures do not capture future rate or spread moves, credit defaults and recoveries, or reinvestment. Bloomberg and USIG’s ICE index differ. |
| VT | MSCI ACWI | 7.60% / 6.40% | 6 bp | 7.54% | [Invesco 2026 Capital Market Assumptions — USD Q3 Update, Figure 6](https://www.invesco.com/content/dam/invesco/emea/en/pdf/invesco-capital-market-assumption-usd.pdf) · observed 2026-06-30 · published 2026-10-12 | [Vanguard Total World Stock ETF fact sheet](https://fund-docs.vanguard.com/F3141.pdf) · reference date 2026-09-30 · September 2026 edition; exact publication day unavailable | Use the broad developed/emerging USD equity projection. MSCI ACWI covers large and mid caps, while VT follows FTSE Global All Cap and includes small caps. Currency, valuation, earnings, tracking and the 10-year versus seven-year horizon remain uncertain. |

The Treasury’s 2026-11-18 13-week reference is 4.26%. Annualized nominal USD 13-week bill quotation before fund expenses; neither an arithmetic total-return forecast nor a compound return. [U.S. Treasury Daily Treasury Bill Rates — 13-week coupon equivalent](https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?field_tdr_date_value_month=202611&type=daily_treasury_bill_rates)

Schwab lists USD 0 per eligible online trade. Source edition: April 2026 edition; exact day unavailable. Online commission per executed trade in eligible U.S. exchange-listed securities, subject to the guide’s conditions. Zero commission still leaves spread, slippage and possible account charges. [Charles Schwab Pricing Guide for Individual Investors](https://www.schwab.com/legal/schwab-pricing-guide-for-individual-investors)

The base inherits 10 bp per year of additional portfolio-level cost. The 0–30 bp sensitivity is a recurring cost budget, with custody/advisory charges unverified. A separate 5–20 bp one-time spread/slippage illustration per dollar traded is excluded from annual returns. No executable quote, account terms or trade pattern are assumed.

The case keeps 2.50% illustrative inflation plus 3 percentage points, for a 5.50% annual net screen. This arithmetic screening hurdle approximates the objective and cannot establish rolling five-year CPI + 3% achievement.

Volatility uses historical ETF covariance from the selected lookback. It is a historical risk proxy, not a forward volatility forecast.

The archived VT signal applies to the November 17 historical case. Current monitoring readiness is not established for the forward scenario. Refresh the signal and verify operational evidence before funding.

**Hold funding. Review the forward screen and refresh monitoring evidence before acting on any allocation.**

| Annual estimate | SGOV | SCHR | USIG | VT |
|---|---:|---:|---:|---:|
| Return before additional cost | 3.11% | 3.97% | 5.56% | 7.54% |
| Volatility | 0.50% | 5.41% | 7.86% | 14.92% |

| Mix | SGOV | SCHR | USIG | VT | Return before extra cost | Net return | Volatility | Eligible reserve | Verdict |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| Equal weight | 25% | 25% | 25% | 25% | 5.04% | 4.94% | 6.51% | 50.00% | Fails modeled checks |
| 60/40 benchmark | 0% | 0% | 40% | 60% | 6.75% | 6.65% | 11.59% | 0.00% | Fails modeled checks |
| Constrained | 10% | 0% | 75% | 15% | 5.61% | 5.51% | 7.79% | 10.00% | Passes modeled checks |
| Original weights | 75% | 0% | 0% | 25% | 4.22% | 4.12% | 3.82% | 75.00% | Fails modeled checks |

Feasible grid mixes: 424 / 1,771.

## Rule-level verdicts

| Rule | Equal weight | 60/40 benchmark | Constrained | Original weights |
|---|---|---|---|---|
| Weights total 100% | Pass | Pass | Pass | Pass |
| Long-only within the ETF universe | Pass | Pass | Pass | Pass |
| Net objective ≥ 5.50% | Fail | Pass | Pass | Fail |
| Eligible reserve ≥ 4% | Pass | Fail | Pass | Pass |
| Standalone scholarship payment illustration | Passes under stated assumptions | Fails | Passes under stated assumptions | Passes under stated assumptions |
| Corporate issuer exposure ≤ 8% under case exemptions | Passes under stated assumptions | Passes under stated assumptions | Passes under stated assumptions | Passes under stated assumptions |
| Illustrative rebalance turnover (approval above 25%) | Approval required | Approval required | Approval required | Passes under stated assumptions |
| At least 90% redeemable within five business days | Not established | Not established | Not established | Not established |
| Account permissions | Not established | Not established | Not established | Not established |
| Annual review and cumulative turnover | Not established | Not established | Not established | Not established |
| Portfolio payment readiness | Not established | Not established | Not established | Not established |

## Operational mandate evidence

### Equal weight

**Standalone scholarship payment illustration · Passes under stated assumptions.**

**Portfolio payment readiness · Not established.**

This is a standalone payment-planning illustration. Opening cash is deducted from the illustrative ETF holdings used in this schedule only. It does not update the main portfolio’s allocation, return, risk, reserve dollars, turnover, or liquidity assessment. These outputs describe separate scenarios and must not be combined.

Illustrative opening cash \$0.00 + invested balance \$1,000,000.00 = total \$1,000,000.00. Initial eligible-security balance \$500,000.00 is part of the invested balance. The selected mix’s ETF weights apply to the remaining illustrative invested balance.

Each sale targets USD 10,000 in pre-shock units from SGOV/SCHR pro rata, capped at remaining holdings. No automatic top-up or sale of other ETFs.

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

**Standalone scholarship payment illustration · Fails.**

**Portfolio payment readiness · Not established.**

This is a standalone payment-planning illustration. Opening cash is deducted from the illustrative ETF holdings used in this schedule only. It does not update the main portfolio’s allocation, return, risk, reserve dollars, turnover, or liquidity assessment. These outputs describe separate scenarios and must not be combined.

Illustrative opening cash \$0.00 + invested balance \$1,000,000.00 = total \$1,000,000.00. Initial eligible-security balance \$0.00 is part of the invested balance. The selected mix’s ETF weights apply to the remaining illustrative invested balance.

Each sale targets USD 10,000 in pre-shock units from SGOV/SCHR pro rata, capped at remaining holdings. No automatic top-up or sale of other ETFs.

Sales are planned two weekdays early. Weekend payments roll forward to Monday. An illustrative weekday calendar omits exchange and banking holidays, cutoffs and transfer delays. Normal proceeds are usable at T+1, consistent with standard [ETF settlement](https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins/new-t1-settlement-cycle-what-investors-need-know-investor-bulletin). Delay assumes T+3; market loss assumes 5% lower sale prices for the same units throughout. No growth, dividends, account fees, execution costs or late payment catch-up are modeled. Opening cash is prior closing cash before crediting newly available proceeds.

Before funding, confirm actual dates, balances, order execution, settlement and payment cutoffs with the custodian.

**Normal · Fails**

| Payment | Opening cash | Sale date | Sale at reference prices | Proceeds | Available | Newly available cash | Due | Paid | Closing cash | Shortfall |
|---|---|---|---|---|---|---|---|---|---|---|
| 2027-03-15 | \$0.00 | — | — | \$0.00 | — | \$0.00 | \$10,000.00 | \$0.00 | \$0.00 | \$10,000.00 |
| 2027-06-15 | \$0.00 | — | — | \$0.00 | — | \$0.00 | \$10,000.00 | \$0.00 | \$0.00 | \$10,000.00 |
| 2027-09-15 | \$0.00 | — | — | \$0.00 | — | \$0.00 | \$10,000.00 | \$0.00 | \$0.00 | \$10,000.00 |
| 2027-12-15 | \$0.00 | — | — | \$0.00 | — | \$0.00 | \$10,000.00 | \$0.00 | \$0.00 | \$10,000.00 |

**Delayed proceeds · Fails**

| Payment | Opening cash | Sale date | Sale at reference prices | Proceeds | Available | Newly available cash | Due | Paid | Closing cash | Shortfall |
|---|---|---|---|---|---|---|---|---|---|---|
| 2027-03-15 | \$0.00 | — | — | \$0.00 | — | \$0.00 | \$10,000.00 | \$0.00 | \$0.00 | \$10,000.00 |
| 2027-06-15 | \$0.00 | — | — | \$0.00 | — | \$0.00 | \$10,000.00 | \$0.00 | \$0.00 | \$10,000.00 |
| 2027-09-15 | \$0.00 | — | — | \$0.00 | — | \$0.00 | \$10,000.00 | \$0.00 | \$0.00 | \$10,000.00 |
| 2027-12-15 | \$0.00 | — | — | \$0.00 | — | \$0.00 | \$10,000.00 | \$0.00 | \$0.00 | \$10,000.00 |

**Market loss · Fails**

| Payment | Opening cash | Sale date | Sale at reference prices | Proceeds | Available | Newly available cash | Due | Paid | Closing cash | Shortfall |
|---|---|---|---|---|---|---|---|---|---|---|
| 2027-03-15 | \$0.00 | — | — | \$0.00 | — | \$0.00 | \$10,000.00 | \$0.00 | \$0.00 | \$10,000.00 |
| 2027-06-15 | \$0.00 | — | — | \$0.00 | — | \$0.00 | \$10,000.00 | \$0.00 | \$0.00 | \$10,000.00 |
| 2027-09-15 | \$0.00 | — | — | \$0.00 | — | \$0.00 | \$10,000.00 | \$0.00 | \$0.00 | \$10,000.00 |
| 2027-12-15 | \$0.00 | — | — | \$0.00 | — | \$0.00 | \$10,000.00 | \$0.00 | \$0.00 | \$10,000.00 |

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

**Standalone scholarship payment illustration · Passes under stated assumptions.**

**Portfolio payment readiness · Not established.**

This is a standalone payment-planning illustration. Opening cash is deducted from the illustrative ETF holdings used in this schedule only. It does not update the main portfolio’s allocation, return, risk, reserve dollars, turnover, or liquidity assessment. These outputs describe separate scenarios and must not be combined.

Illustrative opening cash \$0.00 + invested balance \$1,000,000.00 = total \$1,000,000.00. Initial eligible-security balance \$100,000.00 is part of the invested balance. The selected mix’s ETF weights apply to the remaining illustrative invested balance.

Each sale targets USD 10,000 in pre-shock units from SGOV/SCHR pro rata, capped at remaining holdings. No automatic top-up or sale of other ETFs.

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

**Issuer cap · Passes under stated assumptions.** Mapped company exposure: none mapped. Unmapped portfolio share 0.054%; conservative single-company upper bound 0.054% versus 8%.

The [Campus mandate](https://github.com/Mrigna01/FIN439Project2/blob/15a6d0a3dd1bf883e264aa1d3a0f18596ad5c03b/lab13.md#project-2--own-client-mandate) exempts cash, U.S. Treasury securities and diversified funds. For other holdings, multiply fund weight by each mapped company weight and sum by company across funds. The ETF sponsor is not substituted for underlying issuers. The upper bound assigns all unmapped weight to the largest mapped company (or one new company). Before funding, confirm exemption interpretation and refresh holdings and company mappings for nonexempt positions.

| Fund | Holdings / policy as of | Dated evidence |
|---|---|---|
| SGOV | 2026-11-18 | [Provider](https://www.ishares.com/us/products/314116/sgov) · Provider sector breakdown: 99.47% U.S. Treasury debt and 0.53% investment company. Keep 0.54% unmapped (rounded-up allowance). Corporate issuer identities for that residual were unavailable. |
| USIG | 2026-11-18 | [Provider](https://www.ishares.com/us/products/239460/ishares-credit-bond-etf) · Broad investment-grade corporate bond index; provider reported 11,696 holdings and describes diversified credit exposure. Treat as a diversified fund under the case exemption. Holding count is a diversification indicator, not an issuer count. |
| VT | 2026-09-30 | [Provider](https://fund-docs.vanguard.com/F3141.pdf) · FTSE Global All Cap exposure with 10,185 stocks across developed and emerging markets. Apply the case diversified-fund exemption. |

**Rebalance turnover · Approval required.** 65.00% one-way turnover (half the sum of absolute weight changes), on USD 1 million with no external flows. Approval applies strictly above 25%. The starting weights are illustrative. Initial funding and scholarship sales are outside this rebalance. Annual review and cumulative turnover: Not established. Obtain beginning holdings, dated trade and flow records, an agreed annual turnover convention, annual review evidence and any required approval.

| Fund | Starting | Proposed | Buy | Sell |
|---|---|---|---|---|
| SGOV | \$600,000.00 | \$100,000.00 | \$0.00 | \$500,000.00 |
| SCHR | \$100,000.00 | \$0.00 | \$0.00 | \$100,000.00 |
| USIG | \$100,000.00 | \$750,000.00 | \$650,000.00 | \$0.00 |
| VT | \$200,000.00 | \$150,000.00 | \$0.00 | \$50,000.00 |

**Five-business-day liquidity · Not established.** The dated volume proxy covers 100.0% of portfolio value in the normal case and 43.7% in the stress case, versus the 90% requirement.

Compare full sleeve sales on the USD 1 million portfolio. Normal uses 1% of observed daily share volume over four trading sessions with T+1. Stress uses 10% of observed volume, the same 1% participation and two trading sessions with T+3. Capacity is capped at each sleeve. Missing volume contributes no capacity to this evidence screen. SCHR uses a historical single-day observation, and VT uses a historical provider view. Share estimates for funds without a provider price use the 2026-09-30 adjusted-price archive as a scale proxy. Capacity uses reference prices and excludes market impact and price gaps. Historical volume and a displayed spread cannot establish depth, fills, execution costs, access to proceeds or reliable stressed liquidity. ETF holders generally sell in the secondary market. Before funding, obtain fresh multi-session volume, quotes, depth and broker execution and cash-release confirmation for the full portfolio.

Provider spreads are 30-day median quoted spreads relative to the midpoint ([measurement definition](https://www.ecfr.gov/current/title-17/chapter-II/part-270/section-270.6c-11)). Evidence retrieved 2026-11-19 for this operational review, after the original investment decision date.

| Fund | Liquidation USD | Reference price | Approx. shares | % daily shares | Volume evidence | Median spread | Normal capacity | Stress capacity |
|---|---|---|---|---|---|---|---|---|
| SGOV | \$100,000.00 | \$100.60 | 994 | 0.00% | [2026-11-18](https://www.ishares.com/us/products/314116/sgov) · 24,331,732 shares · 30-day average | 0.01% (2026-11-18) | \$100,000.00 | \$100,000.00 |
| USIG | \$750,000.00 | \$49.05 | 15,291 | 0.80% | [2026-11-18](https://www.ishares.com/us/products/239460/ishares-credit-bond-etf) · 1,902,857 shares · 30-day average | 0.02% (2026-11-18) | \$750,000.00 | \$186,670.27 |
| VT | \$150,000.00 | \$158.73 | 945 | 0.04% | [2026-10-08](https://advisors.vanguard.com/investments/products/vt/vanguard-total-world-stock-etf) · 2,597,924.93 shares · 25-day average shown with October 8 close; historical cached provider view | 0.01% (2026-10-08) | \$150,000.00 | \$150,000.00 |

**Account permissions · Not established.** No actual account documentation exists in the case. Before funding, obtain custodian confirmation of the permitted instruments, authorized traders and disbursement signatories, approval limits, and cash transfer rules. Keep credentials and account identifiers out of the repository.

### Original weights

**Standalone scholarship payment illustration · Passes under stated assumptions.**

**Portfolio payment readiness · Not established.**

This is a standalone payment-planning illustration. Opening cash is deducted from the illustrative ETF holdings used in this schedule only. It does not update the main portfolio’s allocation, return, risk, reserve dollars, turnover, or liquidity assessment. These outputs describe separate scenarios and must not be combined.

Illustrative opening cash \$0.00 + invested balance \$1,000,000.00 = total \$1,000,000.00. Initial eligible-security balance \$750,000.00 is part of the invested balance. The selected mix’s ETF weights apply to the remaining illustrative invested balance.

Each sale targets USD 10,000 in pre-shock units from SGOV/SCHR pro rata, capped at remaining holdings. No automatic top-up or sale of other ETFs.

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
| VT return -2 percentage points | 3.62% net / 3.82% risk / 75% reserve · Fails modeled checks | No feasible grid allocation | — | — | Stop: no allocation passes the active constraints on the grid. |
| Recurring cost 0 bp | 4.22% net / 3.82% risk / 75% reserve · Fails modeled checks | 5.51% net / 7.53% risk / 10% reserve · Passes modeled checks | 10%/0%/80%/10% | 80 points | Hold funding. Review the forward screen and refresh monitoring evidence before acting on any allocation. |
| Recurring cost 30 bp | 3.92% net / 3.82% risk / 75% reserve · Fails modeled checks | 5.51% net / 8.38% risk / 10% reserve · Passes modeled checks | 10%/0%/65%/25% | 65 points | Hold funding. Review the forward screen and refresh monitoring evidence before acting on any allocation. |

### Operational checks by stress and allocation

Liquidity percentages are volume proxies. Account permissions are not established in every scenario.

| Scenario | Mix | Payment illustration (normal) | Issuer cap | Turnover | Normal liquidity proxy |
|---|---|---|---|---|---|
| VT return -2 percentage points | Original weights | Passes under stated assumptions | Passes under stated assumptions | 20.00% · Passes under stated assumptions | 100.0% · Not established |
| Recurring cost 0 bp | Constrained | Passes under stated assumptions | Passes under stated assumptions | 70.00% · Approval required | 100.0% · Not established |
| Recurring cost 0 bp | Original weights | Passes under stated assumptions | Passes under stated assumptions | 20.00% · Passes under stated assumptions | 100.0% · Not established |
| Recurring cost 30 bp | Constrained | Passes under stated assumptions | Passes under stated assumptions | 60.00% · Approval required | 100.0% · Not established |
| Recurring cost 30 bp | Original weights | Passes under stated assumptions | Passes under stated assumptions | 20.00% · Passes under stated assumptions | 100.0% · Not established |

Stop the current mix if it misses the 5.50% net screen or the reserve floor. Review any reoptimized allocation and verify a current signal, account terms and open mandate checks before reconsidering funding.
