# Recording scripts and screen sequence

These are proposed scripts. Use the opening statements only once you have reviewed the project, can explain the calculations, and own the decision. Put a small webcam view on the recording unless your approved accommodation provides an alternative. Record three separate YouTube videos with captions. Correct the captions and save the actual transcript for each video as `docs/transcript-video-1.txt`, `docs/transcript-video-2.txt`, and `docs/transcript-video-3.txt`. Add actual timestamps to the transcripts and to the manifest. Start a new timestamp at each evidence transition. Verify captions, tickers and numbers against what you actually said.

## Video 1 — How the system changed and one AI check

**Target 2:15, limit 3:00.**

In the system-evolution segment, identify the external forward scenario as a later addition. Keep the original one-point VT calculation as the historical AI check.

- **0:00–0:18 · Open on the repository.** “I used ChatGPT through Codex to help adapt my lab code, test the portfolio logic and prepare these materials. The analysis and decision are mine. This is for education, not investment advice.”
- **0:18–0:55 · Show the old and new comparisons.** “The lab app compared two optimizer runs. That answered a stability question but left me without two transparent alternatives. The final app shows equal weight and the policy benchmark under the same inputs and rules as the optimizer.”
- **0:55–1:45 · Show the AI check against the report.** “I checked whether the original pilot still met the target after a one-point cut to VT’s estimate. The earlier test showed 5.51% before additional client costs. The final case tests a net hurdle. I verified that subtracting 10 basis points yields 5.41%. The existing mix therefore fails even though the optimizer can find a new one.”
- **1:45–2:15 · Explain the judgment change.** “That check changed my recommendation to a paper pilot with funding held. Adding equity to pass the modeled return test is a separate risk decision that needs committee review.”

## Video 2 — Code walkthrough

**Target 4:15, limit 5:00.**

In the math and reproduction segments, identify historical returns as the default and show how the forward mode replaces the means in the shared engine while retaining historical covariance. Use `python report.py --forward` for the separate exhibit. Describe the VT gate as historical.

- **0:00–0:18 · Open on the repository.** “I used ChatGPT through Codex for app implementation, test suggestions and documentation. The analysis and decision are mine. This is for education, not investment advice.”
- **0:18–1:15 · Show data flow.** Open `prices.csv`, `load_snapshot` and the archive metadata. Explain the source cross-check, 61 month-end prices, 60 returns, USD convention and the decision boundary.
- **1:15–2:30 · Show portfolio math.** In `portfolio.py`, show weighted historical arithmetic returns and the covariance-based volatility calculation. Explain how the net cost is deducted before screening and how the five-point grid gives a finite, discrete search. In `campus.py`, show how the same inputs and checks govern the two baselines and the constrained candidate.
- **2:30–3:10 · Show the signal gate.** Explain the adjusted-close ratio and October archive availability. Show where a nonpositive signal places the decision on hold without changing weights.
- **3:10–4:15 · Reproduce and stress.** Run `python report.py` and show the saved table. Run the test command from the README. Show the 30 bp stress lowering the original mix to 5.46% net and the reoptimized mix raising VT to 30%. Identify the unverified liquidity and dated payout checks.

## Video 3 — Investment committee

**Target 4:00, limit 5:00. Open with the app already running on screen.**

Keep the historical live opening and cost stress. In the risk segment, show the November 19 forward comparison. The fixed pilot falls to 4.12% net against 5.50%, and the new modeled allocation carries 75% USIG and 7.79% historical-covariance volatility. Explain that the forward case strengthens the funding hold and requires updated monitoring.

- **0:00–0:20 · Live app and opening.** “I used ChatGPT through Codex to help build and check this app. The analysis and decision are mine. This is for education, not investment advice. I’m asking for a paper pilot of 75% SGOV and 25% VT, with funding held.”
- **0:20–1:20 · Live portfolio and mandate.** Show the three portfolios and open rule verdicts. Explain that equal weight misses the return target and the benchmark lacks eligible reserves. The selected mix estimates 5.66% net and 3.82% annual volatility at 10 bp modeled cost.
- **1:20–2:20 · Move one control live.** Set additional cost to 30 bp. Show the original mix at 5.46% net and the 70/30 reoptimized mix. Explain why a qualifying new mix does not authorize a switch. The feasible sensitivity range is 70–90% SGOV and 10–30% VT.
- **2:20–3:20 · Explain the risks.** Show the 36-month comparison and the VT data card. Explain why one archived trend signal and historical arithmetic returns cannot establish forward returns or investor-level liquidity. Monitor estimated net return, costs, reserve coverage and scheduled payouts.
- **3:20–4:00 · Close with the ask.** “Approve the paper pilot only. If the mix falls below the 5.50% estimated net target or fails the reserve floor, stop and bring the mandate back to committee. Hold for review if the signal is unavailable or nonpositive. Before funding, verify execution costs, five-day liquidity, issuer exposure and turnover.”

[Decision memo](decision-memo.md) · [Generated output](../data/decision-output.md)
