# Project 2 requirements and evidence

Reviewed the [assignment](https://github.com/CinderZhang/FIN43900-Fall2026/blob/main/projects/project-2-investment-management-application.md), [student checklist](https://github.com/CinderZhang/FIN43900-Fall2026/blob/main/projects/major-project-student-checklist.md), [submission architecture](https://github.com/CinderZhang/FIN43900-Fall2026/blob/main/PROJECT-SUBMISSION-ARCHITECTURE.md) and [Lab 20](https://github.com/CinderZhang/FIN43900-Fall2026/blob/main/lessons/week-13/lab-20-project2-readiness.md). Project 2 uses Markdown, has no Edition A/B or research-evolution submission, and retains the locked prediction and three video requirements.

| Requirement | Original evidence and gap | Final evidence |
|---|---|---|
| Runnable app | Lab 15 Streamlit worked; Meridian default and setup assumed an environment | Campus default, fresh-clone steps in [README](../README.md), [app smoke check](../tests/test_app.py) |
| Mandate | Lab 13 described the fictional client; Meridian checker used different rules | [Memo](decision-memo.md), app rule table and [engine](../campus.py) |
| Two baselines plus constrained | Lab 14 baseline functions existed; Lab 15 showed two optimized mixes | Equal weight and 60/40 under the same active model as the constrained mix in [app](../app.py) and [output](../data/decision-output.md) |
| Point-in-time signal | Lab 16 handled vintages for fictional rows | Real VT signal with archival availability gate, app data card and cutoff test |
| Stress and stopping | Lab 15 window and estimates, Lab 20 stand-alone reserve scenario | Four common engine scenarios, fixed versus reoptimized, and [rule-level output](../data/decision-output.md) |
| Locked experiment | Existing prediction AI-assisted; later wording edited after results | Immutable links and [pending AI-off worksheet](locked-prediction-template.md) |
| Recommendation | Lab 15 proposed pilot without additional client costs | Cost-aware paper pilot, range and committee ask in [memo](decision-memo.md) |
| Opening statements and video evidence | Prior README had a generic disclosure; no verified videos | README and memo disclosures; [scripts](video-scripts.md) prepared; recordings and transcripts pending |
| Submission and access | Lab checkout links only | [Manifest](submission-manifest.md), with pending personal evidence and access verification |
