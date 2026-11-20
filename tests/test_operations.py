from datetime import date
import unittest

import campus
from operations import ASSUMED, FAIL, UNKNOWN, VERIFIED, Assumptions, cash_schedule, issuer_exposure, rebalance


class OperationsTests(unittest.TestCase):
    def test_cash_exactly_covered_and_running_shortfalls(self):
        days = (date(2027, 3, 15), date(2027, 6, 15))
        first, second = cash_schedule({"SGOV": 15_000}, days, 0, 10_000)
        self.assertEqual((first["paid"], first["closing"], first["shortfall"]), (10_000, 0, 0))
        self.assertEqual((second["proceeds"], second["paid"], second["shortfall"]), (5_000, 5_000, 5_000))
        cash_only = cash_schedule({}, days, 10_000, 10_000)
        self.assertEqual([row["shortfall"] for row in cash_only], [0, 10_000])

    def test_delayed_settlement_and_sale_price_loss(self):
        days = (date(2027, 3, 14), date(2027, 6, 15))
        delayed = cash_schedule({"SGOV": 25_000}, days, 0, 10_000, lag=3)
        first, second = delayed
        self.assertEqual(first["payment"], date(2027, 3, 15))
        self.assertEqual(first["trade"], date(2027, 3, 11))
        self.assertEqual(first["available"], date(2027, 3, 16))
        self.assertEqual((first["settled"], first["shortfall"]), (0, 10_000))
        self.assertEqual((second["settled"], second["paid"], second["shortfall"]), (10_000, 10_000, 0))
        loss = cash_schedule({"SGOV": 20_000, "SCHR": 5_000}, days, 0, 10_000, loss=.05)
        self.assertEqual(loss[0]["sales"], {"SGOV": 8_000, "SCHR": 2_000})
        self.assertEqual([row["proceeds"] for row in loss], [9_500, 9_500])
        self.assertEqual([row["shortfall"] for row in loss], [500, 500])

    def test_issuer_aggregation_and_exemptions(self):
        coverage = {
            "A": {"exempt": .90, "companies": {"Same Co": .10}},
            "B": {"exempt": .80, "companies": {"Same Co": .20}},
            "Diversified": {"exempt": 1, "policy_assumption": True},
        }
        result = issuer_exposure({"A": .5, "B": .2, "Diversified": .3}, coverage)
        self.assertAlmostEqual(result["companies"]["Same Co"], .09)
        self.assertEqual(result["status"], FAIL)
        result = issuer_exposure({"A": .4, "B": .2, "Diversified": .4}, coverage)
        self.assertAlmostEqual(result["upper"], .08)
        self.assertEqual(result["status"], ASSUMED)
        result = issuer_exposure({"Treasuries": 1, "Unused": 0}, {"Treasuries": {"exempt": 1}})
        self.assertEqual(result["status"], VERIFIED)

    def test_issuer_incomplete_coverage_cannot_clear_material_unknown(self):
        weights = {"A": .5, "Missing": .5}
        result = issuer_exposure(weights, {"A": {"exempt": .9, "companies": {"Known": .1}}})
        self.assertAlmostEqual(result["unmapped"], .5)
        self.assertAlmostEqual(result["upper"], .55)
        self.assertEqual(result["status"], UNKNOWN)

    def test_turnover_below_at_and_above_approval_boundary(self):
        for target, status in ((.74, ASSUMED), (.75, ASSUMED), (.750001, "Approval required")):
            with self.subTest(target=target):
                result = rebalance({"A": target, "B": 1 - target}, (.5, .5), 1_000_000)
                self.assertAlmostEqual(result["turnover"], target - .5)
                self.assertEqual(result["status"], status)
                self.assertAlmostEqual(result["rows"][0]["buy"], (target - .5) * 1_000_000)
                self.assertEqual(result["rows"][0]["buy"], result["rows"][1]["sell"])

    def test_operational_results_follow_scenario_weights(self):
        result = campus.run()
        default = result["mixes"]["Constrained"]["operational"]
        benchmark = result["mixes"]["60/40 benchmark"]["operational"]
        self.assertEqual(default["cash"]["Normal"][0]["sales"], {"SGOV": 10_000})
        self.assertEqual(benchmark["cash"]["Normal"][0]["shortfall"], 10_000)
        self.assertGreater(default["issuer"]["upper"], benchmark["issuer"]["upper"])
        self.assertAlmostEqual(default["turnover"]["turnover"], .20)
        self.assertEqual(default["liquidity"]["status"], UNKNOWN)
        self.assertAlmostEqual(default["liquidity"]["normal"], 1)
        self.assertLess(benchmark["liquidity"]["stress"], .90)

        trial = campus.run(campus.STRESSES["Additional cost 30 bp"],
                           fixed_weights=result["mixes"]["Constrained"]["weights"],
                           assumptions=Assumptions(opening_cash=20_000))
        new = trial["mixes"]["Constrained"]["operational"]
        original = trial["mixes"]["Original weights"]["operational"]
        self.assertEqual(new["cash"]["Normal"][0]["opening"], 20_000)
        self.assertNotEqual(new["issuer"]["upper"], original["issuer"]["upper"])
        self.assertNotEqual(new["turnover"]["turnover"], original["turnover"]["turnover"])
        self.assertNotEqual(new["liquidity"]["rows"], original["liquidity"]["rows"])

    def test_payment_opening_cash_does_not_change_main_portfolio(self):
        capital = campus.STARTING_CAPITAL
        without_cash = campus.run(assumptions=Assumptions(opening_cash=0))
        all_cash = campus.run(assumptions=Assumptions(opening_cash=capital))
        base = without_cash["mixes"]["Constrained"]["operational"]
        full = all_cash["mixes"]["Constrained"]["operational"]
        self.assertEqual(base["cash_balances"], {"opening": 0, "invested": capital,
                                                 "eligible": 750_000, "total": capital})
        self.assertEqual(base["cash"]["Normal"][0]["sales"], {"SGOV": 10_000})
        self.assertEqual(full["cash_balances"], {"opening": capital, "invested": 0,
                                                 "eligible": 0, "total": capital})
        for rows in full["cash"].values():
            self.assertTrue(all(not row["sales"] and row["proceeds"] == 0 for row in rows))
            self.assertEqual(rows[-1]["closing"], 960_000)
        for name, base_mix in without_cash["mixes"].items():
            cash_mix = all_cash["mixes"][name]
            for field in ("weights", "before_cost", "net", "volatility", "reserve", "verdict"):
                self.assertEqual(base_mix[field], cash_mix[field])
            for field in ("issuer", "turnover", "liquidity"):
                self.assertEqual(base_mix["operational"][field], cash_mix["operational"][field])
        self.assertEqual(without_cash["action"], all_cash["action"])
