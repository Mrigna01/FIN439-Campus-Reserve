from datetime import date
from pathlib import Path
import unittest

from streamlit.testing.v1 import AppTest
from operations import PAYMENT_ILLUSTRATION_NOTE, PAYMENT_READINESS
from report import render


class AppTests(unittest.TestCase):
    def test_campus_default_and_interactive_stops(self):
        app = AppTest.from_file(str(Path(__file__).resolve().parents[1] / "app.py"), default_timeout=15).run()
        self.assertFalse(app.exception)
        self.assertFalse(app.error)
        table = app.table[0].value
        self.assertEqual(table["Portfolio"].tolist(), ["Equal weight", "60/40 benchmark", "Constrained"])
        self.assertEqual(table["Net return"].tolist(), ["3.76%", "7.08%", "5.66%"])
        app.number_input[1].set_value(30).run()
        self.assertFalse(app.exception)
        table = app.table[0].value
        self.assertEqual(table["Net return"].tolist()[-2:], ["5.87%", "5.46%"])
        self.assertIn("Original pilot fails", app.warning[0].value)
        app.number_input[2].set_value(80).run()
        self.assertFalse(app.exception)
        self.assertIn("No feasible mix", app.warning[0].value)

    def test_operational_detail_matches_report_and_reacts_to_controls(self):
        app = AppTest.from_file(str(Path(__file__).resolve().parents[1] / "app.py"), default_timeout=15).run()
        self.assertFalse(app.exception)
        detail = next(item.value for item in app.markdown if item.value.startswith("**Standalone scholarship payment illustration"))
        self.assertIn(detail, render())
        self.assertIn("20.00% one-way turnover", detail)
        mandate = app.table[1].value.set_index("Rule")
        self.assertEqual(mandate.loc[PAYMENT_READINESS, "Constrained"], "Not established")
        self.assertEqual(mandate.loc["Standalone scholarship payment illustration", "Constrained"],
                         "Passes under stated assumptions")

        chooser = next(widget for widget in app.selectbox if widget.label == "Portfolio for operational review")
        chooser.set_value("60/40 benchmark").run()
        detail = next(item.value for item in app.markdown if item.value.startswith("**Standalone scholarship payment illustration"))
        self.assertIn("**Standalone scholarship payment illustration · Fails.**", detail)
        self.assertIn("70.00% one-way turnover", detail)

        opening = next(widget for widget in app.number_input
                       if widget.label == "Opening cash for standalone payment illustration (USD)")
        comparison = app.table[0].value.copy()
        opening.set_value(1_000_000.0).run()
        detail = next(item.value for item in app.markdown if item.value.startswith("**Standalone scholarship payment illustration"))
        self.assertIn(PAYMENT_ILLUSTRATION_NOTE, detail)
        self.assertIn(PAYMENT_ILLUSTRATION_NOTE, [caption.value for caption in app.caption])
        self.assertIn(r"invested balance \$0.00", detail)
        self.assertIn(r"Initial eligible-security balance \$0.00", detail)
        self.assertTrue(comparison.equals(app.table[0].value))
        self.assertEqual(app.table[1].value.set_index("Rule").loc[PAYMENT_READINESS, "Constrained"],
                         "Not established")

        opening = next(widget for widget in app.number_input
                       if widget.label == "Opening cash for standalone payment illustration (USD)")
        opening.set_value(40_000.0).run()
        detail = next(item.value for item in app.markdown if item.value.startswith("**Standalone scholarship payment illustration"))
        self.assertIn("**Standalone scholarship payment illustration · Passes under stated assumptions.**", detail)

        payment = next(widget for widget in app.date_input if widget.label == "Illustrative payment 1")
        payment.set_value(date(2027, 3, 16)).run()
        detail = next(item.value for item in app.markdown if item.value.startswith("**Standalone scholarship payment illustration"))
        self.assertIn("| 2027-03-16 |", detail)

        for label, value in (("Starting SGOV (%)", 50.0), ("Starting VT (%)", 30.0)):
            next(widget for widget in app.number_input if widget.label == label).set_value(value)
        chooser = next(widget for widget in app.selectbox if widget.label == "Portfolio for operational review")
        chooser.set_value("Constrained").run()
        detail = next(item.value for item in app.markdown if item.value.startswith("**Standalone scholarship payment illustration"))
        self.assertIn("25.00% one-way turnover", detail)

        lookback = next(widget for widget in app.selectbox if widget.label == "Lookback")
        lookback.set_value("36 monthly returns").run()
        shift = next(widget for widget in app.number_input if widget.label.startswith("VT annual return shift"))
        shift.set_value(-1.0).run()
        self.assertFalse(app.exception)
        self.assertFalse(app.error)
        self.assertIn("Original weights", app.table[0].value["Portfolio"].tolist())
