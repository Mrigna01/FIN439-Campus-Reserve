from copy import deepcopy
from dataclasses import replace
from datetime import date
from pathlib import Path
from unittest.mock import patch
import unittest

from campus import DEFAULT, ROOT, TICKERS, run
from forward import FORWARD_LABEL, forward_stresses, load_forward, run_forward, selected_returns
from report import render
from streamlit.testing.v1 import AppTest


class ForwardTests(unittest.TestCase):
    def setUp(self):
        self.record = load_forward()
        self.cutoff = date.fromisoformat(self.record["analysis_date"])
        self.historical = run()
        self.fixed = self.historical["mixes"]["Constrained"]["weights"]

    def test_return_and_cost_units_are_consistent_across_mixes(self):
        rates = selected_returns(self.record, self.cutoff)
        for ticker, expected in zip(TICKERS, (.0311, .0397, .0556, .0754), strict=True):
            self.assertAlmostEqual(rates[ticker], expected)
        baseline = run_forward(self.record, fixed_weights=self.fixed)
        high_cost = run_forward(self.record, replace(DEFAULT, cost_bp=30), fixed_weights=self.fixed)
        for mix in baseline["mixes"].values():
            gross = sum(weight * rates[ticker] for ticker, weight in zip(TICKERS, mix["weights"], strict=True))
            self.assertAlmostEqual(mix["before_cost"], gross)
            self.assertAlmostEqual(mix["net"], gross - .001)
        original = baseline["mixes"]["Original weights"]
        self.assertAlmostEqual(original["net"] - high_cost["mixes"]["Original weights"]["net"], .002)
        self.assertAlmostEqual(original["volatility"], self.historical["mixes"]["Constrained"]["volatility"])
        self.assertIsNone(baseline["signal"])

    def test_fixed_weights_reoptimization_and_infeasibility(self):
        result = run_forward(self.record, fixed_weights=self.fixed)
        original, candidate = (result["mixes"][name] for name in ("Original weights", "Constrained"))
        self.assertEqual(original["weights"], self.fixed)
        self.assertEqual(original["verdict"], "Fails modeled checks")
        self.assertEqual(candidate["weights"], [.10, 0, .75, .15])
        self.assertEqual(candidate["verdict"], "Passes modeled checks")
        self.assertEqual(candidate["operational"]["turnover"]["status"], "Approval required")
        self.assertTrue(result["action"].startswith("Hold funding"))
        stressed = forward_stresses(self.record, fixed_weights=self.fixed)["VT return -2 percentage points"]
        self.assertIsNone(stressed["candidate"])
        self.assertTrue(stressed["action"].startswith("Stop"))
        self.assertEqual(stressed["mixes"]["Original weights"]["weights"], self.fixed)

    def test_date_and_missing_evidence_gates(self):
        with self.assertRaisesRegex(ValueError, "not available"):
            selected_returns(self.record, date(2026, 11, 17))
        future_source = deepcopy(self.record)
        future_source["sources"]["q3"]["available_by"] = "2026-11-20"
        with self.assertRaisesRegex(ValueError, "q3: evidence was unavailable"):
            run_forward(future_source)
        future_measurement = deepcopy(self.record)
        future_measurement["funds"]["VT"]["fund_as_of"] = "2026-11-20"
        with self.assertRaisesRegex(ValueError, "VT: evidence was unavailable"):
            run_forward(future_measurement)
        missing = deepcopy(self.record)
        del missing["funds"]["USIG"]["arithmetic_pct"]
        with self.assertRaisesRegex(ValueError, "USIG: .*unresolved"):
            run_forward(missing)

    def test_separate_reports_reproduce_without_network(self):
        with patch("socket.socket.connect", side_effect=AssertionError("Network access is unexpected")):
            historical = render()
            forward = render(forward=True)
        self.assertEqual(historical, (ROOT / "data/decision-output.md").read_text())
        self.assertEqual(forward, (ROOT / "data/forward-output.md").read_text())
        self.assertIn("Analysis date 2026-11-19", forward)
        self.assertIn("Historical VT signal: 16.45%", forward)
        self.assertIn("| Portfolio payment readiness | Not established", forward)

    def test_app_switches_and_matches_forward_report_offline(self):
        with patch("socket.socket.connect", side_effect=AssertionError("Network access is unexpected")):
            app = AppTest.from_file(str(Path(ROOT) / "app.py"), default_timeout=15).run()
            default_comparison = app.table[0].value.copy()
            app.radio[0].set_value(FORWARD_LABEL).run()
            self.assertFalse(app.exception)
            self.assertFalse(app.error)
            self.assertEqual(app.table[0].value["Net return"].tolist(), ["4.94%", "6.65%", "5.51%", "4.12%"])
            detail = next(item.value for item in app.markdown if item.value.startswith("**Forward source record.**"))
            self.assertIn(detail, render(forward=True))
            self.assertTrue(any("Current monitoring readiness is not established" in item.value for item in app.markdown))
            shift = next(widget for widget in app.number_input if widget.label.startswith("VT annual return shift"))
            shift.set_value(-2.0).run()
            self.assertIn("No feasible mix", app.warning[0].value)
            next(widget for widget in app.number_input if widget.label.startswith("VT annual return shift")).set_value(0.0)
            app.radio[0].set_value("Historical").run()
            self.assertFalse(app.exception)
            self.assertTrue(default_comparison.equals(app.table[0].value))
