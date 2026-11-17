from pathlib import Path
import unittest

from streamlit.testing.v1 import AppTest


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
