import unittest
from dataclasses import replace
from datetime import date
from pathlib import Path

import campus
import portfolio
from report import render


class PortfolioTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.snapshot = campus.load_snapshot()
        cls.result = campus.run(snapshot=cls.snapshot)

    def test_grid_weights(self):
        grid = list(portfolio.weight_grid(4))
        self.assertEqual(len(grid), 1771)
        self.assertEqual(len(set(map(tuple, grid))), 1771)
        for weights in grid:
            self.assertAlmostEqual(sum(weights), 1.0)
            self.assertTrue(all(weight >= 0 for weight in weights))

    def test_hand_calculation(self):
        weights = [.5, .5]
        sleeves = [{"return": .04, "volatility": .10}, {"return": .08, "volatility": .20}]
        covariance = portfolio.covariance_matrix(sleeves, [[1, .5], [.5, 1]])
        self.assertAlmostEqual(covariance[0][1], .01)
        self.assertAlmostEqual(portfolio.expected_return(weights, sleeves), .06)
        self.assertAlmostEqual(portfolio.portfolio_volatility(weights, covariance), .13228756555322954)

    def test_baselines_and_winner(self):
        mixes = self.result["mixes"]
        self.assertEqual(mixes["Equal weight"]["checks"]["Net objective ≥ 5.50%"], "Fail")
        self.assertEqual(mixes["60/40 benchmark"]["checks"]["Eligible reserve ≥ 4%"], "Fail")
        self.assertEqual(mixes["Constrained"]["weights"], [.75, 0, 0, .25])
        self.assertAlmostEqual(mixes["Constrained"]["net"], .05660112201760271)
        self.assertIn("Not established", mixes["Constrained"]["checks"].values())

    def test_exact_boundaries(self):
        sleeves = [{"name": str(i), "return": .06, "volatility": .1,
                    "reserve_eligible": i == 0} for i in range(3)]
        corr = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
        self.assertEqual(portfolio.search_portfolio(sleeves, corr, .055, 1, .005)["weights"], [1, 0, 0])
        self.assertIsNone(portfolio.search_portfolio(sleeves, corr, .05501, 1, .005))

    def test_cost_and_no_feasible_mix(self):
        fixed = self.result["mixes"]["Constrained"]
        stress = campus.stress_results(self.snapshot, self.result)
        cost = stress["Additional cost 30 bp"]["mixes"]["Original weights"]
        self.assertAlmostEqual(fixed["net"] - cost["net"], .002)
        self.assertEqual(fixed["volatility"], cost["volatility"])
        self.assertEqual(cost["verdict"], "Fails modeled checks")
        self.assertIsNone(stress["Reserve floor 80%"]["candidate"])
        self.assertEqual(stress["Trailing 36 months"]["estimate"]["observations"], 36)

    def test_what_if_cannot_waive_case_threshold(self):
        trial = campus.run(replace(campus.DEFAULT, net_target_pct=0), snapshot=self.snapshot)
        mix = trial["mixes"]["Constrained"]
        self.assertEqual(mix["checks"]["Case net objective ≥ 5.50%"], "Fail")
        self.assertTrue(trial["action"].startswith("Stop"))

    def test_point_in_time_gate(self):
        _, _, dates, prices = self.snapshot
        series = [row[3] for row in prices]
        available = date(2026, 10, 22)
        self.assertIsNone(campus.trend_signal(dates, series, available, date(2026, 10, 21)))
        self.assertIsNone(campus.trend_signal(dates[:12], series[:12], available, available))
        signal = campus.trend_signal(dates, series, available, available)
        self.assertAlmostEqual(signal["return"], .1645, places=4)
        self.assertEqual(signal["lag_days"], 22)
        with self.assertRaisesRegex(ValueError, "not available"):
            campus.run(cutoff=date(2026, 9, 30), snapshot=self.snapshot)
        self.assertTrue(campus.recommendation(self.result["mixes"]["Constrained"], {"return": -.01})
                        .startswith("Hold"))

    def test_bad_csv_and_inputs(self):
        with self.assertRaisesRegex(ValueError, "numeric prices"):
            portfolio.read_monthly_prices(b"Date,A,B,C\n2024-01-31,2,,3\n")
        with self.assertRaisesRegex(ValueError, "consecutive month"):
            portfolio.read_monthly_prices(b"Date,A,B,C\n2024-01-31,1,2,3\n2024-03-29,2,2,3\n")
        with self.assertRaises(ValueError):
            campus.Inputs(cost_bp=-1)

    def test_saved_output_matches_engine(self):
        self.assertEqual(render(), Path("data/decision-output.md").read_text())
