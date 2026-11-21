# Campus Scholarship Reserve

I used ChatGPT through Codex to adapt the app, and check calculations. I am responsible for the analysis and committee decision. This is for education, not investment advice.

The app helps the investment committee of a fictional $1 million scholarship reserve decide whether to pilot a portfolio process. The recommendation is a **paper pilot of 75% SGOV and 25% VT**, with funding held until return assumptions, costs and open mandate checks are verified. [Decision memo](docs/decision-memo.md) · [Executed results](data/decision-output.md)

## Start from a fresh clone

Anyone can clone this public repository without signing in to GitHub. Use Python 3.13, Git, and a browser. On macOS or Linux, use a shell with Python 3.13 on the path. Check the version before creating the environment. On Windows, use `py -3.13` to create it and `.venv\Scripts\Activate.ps1` in PowerShell.

```sh
git clone https://github.com/Mrigna01/FIN439-Campus-Reserve.git
cd FIN439-Campus-Reserve
python3.13 --version
python3.13 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

Open the local URL printed by Streamlit. Campus opens with 60 monthly returns, 10 bp additional annual cost, a 5.50% net return target, and a 4% reserve floor. Compare equal weight, the 60/40 benchmark and the constrained mix. Open **Mandate checks by portfolio** and change **Additional annual cost (bp)** to 30 to see the original pilot and reoptimized weights side by side. The **Point-in-time signal and data card** explains when the archived VT signal can be used.

Open **Operational mandate evidence** to review scheduled scholarship cash, issuer exemptions and residual exposure, turnover, liquidity and account permissions for a selected mix. Edit the fictional payment dates, starting cash and starting ETF weights under **Illustrative operational inputs**. The report uses the checked-in defaults and runs offline. [Evidence snapshot](data/operational-evidence.json) · [Executed results](data/decision-output.md#operational-mandate-evidence)

**Opening cash for standalone payment illustration (USD)** reduces the ETF balance in the payment schedule only. The selected ETF weights apply to the remaining illustrative invested balance. The main portfolio retains its full ETF allocation, with the same return, risk, reserve dollars, turnover and liquidity results. The illustration does not establish payment readiness for that portfolio.

The app opens in **Historical** mode. Select **Forward assumptions — illustrative** in the sidebar to compare sourced annual return proxies at the same 5.50% net hurdle, with historical covariance for risk. The November 19 forward scenario keeps the November 17 signal as historical evidence. [Source record](data/forward-assumptions.json) · [Forward results](data/forward-output.md)

## Reproduce and test

With the environment activated, run these from the repository root.

```sh
python -m unittest discover -s tests -v
python report.py
python report.py --forward
```

To refresh the checked-in report from the same data, run `python report.py > data/decision-output.md`. The app and report use the same [scenario engine](campus.py) and [portfolio calculations](portfolio.py). Only the app and its smoke test require Streamlit, pinned in [requirements.txt](requirements.txt). The frozen price archive needs no API key or live download.

## Data and scope

Yahoo Finance USD adjusted closes were retrieved October 22, 2026 and cover September 2021 through September 2026. Fund expenses are already reflected in the historical fund prices. The additional cost control is an illustrative uniform annual drag. Historical estimates, a single price vintage and a five-point allocation grid support a classroom pilot. The operational review uses saved evidence and fictional inputs. Funding remains on hold pending client-specific verification. No data refresh occurs automatically. [Sources, data card and validation](docs/validation-and-ai-use.md)

## Reuse

The original [FIN439Project2 lab repository](https://github.com/Mrigna01/FIN439Project2) supplied the [portfolio math and snapshot](https://github.com/Mrigna01/FIN439Project2/tree/15a6d0a3dd1bf883e264aa1d3a0f18596ad5c03b), the [Campus mandate and grid results](https://github.com/Mrigna01/FIN439Project2/blob/15a6d0a3dd1bf883e264aa1d3a0f18596ad5c03b/lab15.md), and the [Lab 16 cutoff approach](https://github.com/Mrigna01/FIN439Project2/blob/13c235e/asof.py). The final app adds rule-level checks, costs, comparable baselines, a real archived VT signal, and a shared scenario report. The Meridian training UI, fictional Lab 16 prices, standalone investor apps, standalone mandate demo, and prior lab scripts stay in the original repository.

- [Requirements audit](docs/requirements-audit.md)
- [Submission manifest](docs/submission-manifest.md)
- [Video scripts](docs/video-scripts.md)
- [Locked prediction worksheet](docs/validation-and-ai-use.md#locked-changed-input-record)
