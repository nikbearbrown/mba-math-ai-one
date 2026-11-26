"""Recompute the fictional example; no packages or network required."""
import json
from decimal import Decimal as D
from pathlib import Path
import unittest


CASE = json.loads(Path(__file__).with_name("case.json").read_text(encoding="utf-8"))
Q = [D(s["daily_requests"]) * CASE["operating_days"] for s in CASE["scenarios"]]
P = [D(s["probability"]) for s in CASE["scenarios"]]
MARGIN = CASE["unit_revenue"] - CASE["unit_expense"]


def profit(plan, demand):
    return min(plan["capacity"], demand) * MARGIN - plan["fixed"]


def weighted(values):
    return sum(p * value for p, value in zip(P, values))


A, B = [CASE["plans"][label] for label in ("A", "B")]


class CaseChecks(unittest.TestCase):
    def test_dimensions_and_weights(self):
        self.assertEqual(Q, [90, 110, 170])
        self.assertEqual(sum(P), 1)
        self.assertEqual(weighted(Q), 120)
        self.assertEqual(MARGIN, 12)

    def test_break_even(self):
        for plan, q in [(A, 75), (B, 83)]:
            self.assertLess(profit(plan, q - 1), 0)
            self.assertGreaterEqual(profit(plan, q), 0)

    def test_scenario_rows(self):
        self.assertEqual([profit(A, q) for q in Q], [180, 420, 540])
        self.assertEqual([profit(B, q) for q in Q], [90, 330, 930])

    def test_expected_outcomes(self):
        self.assertEqual(weighted([profit(A, q) for q in Q]), 390)
        self.assertEqual(weighted([profit(B, q) for q in Q]), 420)
        self.assertEqual(weighted([min(A["capacity"], q) for q in Q]), D("107.5"))
        self.assertEqual(weighted([min(B["capacity"], q) for q in Q]), D("117.5"))

    def test_mean_substitution_reverses_ranking(self):
        self.assertEqual([profit(plan, weighted(Q)) for plan in (A, B)], [540, 450])

    def test_floor(self):
        floor = CASE["low_profit_floor"]
        self.assertEqual([profit(plan, Q[0]) >= floor for plan in (A, B)], [True, False])

    def test_sensitivity(self):
        gap = [profit(B, q) - profit(A, q) for q in Q]
        self.assertEqual(gap, [-90, -90, 390])
        h = -D(gap[0]) / (gap[2] - gap[0])
        self.assertEqual(h, D(".1875"))
        self.assertEqual((1-h) * gap[0] + h * gap[2], 0)
        self.assertEqual(D(".8") * gap[0] + D(".2") * gap[2], 6)

    def test_financing(self):
        f = CASE["financing"]
        p, r, m = f["principal"], D(f["monthly_rate"]), f["months"]
        self.assertEqual(p * (1 + m*r), D("1019.70"))
        self.assertEqual(p * (1+r)**m, D("1019.99799"))
        self.assertEqual((p * (1+r)**m).quantize(D(".01")), D("1020.00"))

    def test_counterfactual_capacity(self):
        a2 = dict(A, capacity=130)
        self.assertEqual(weighted([profit(a2, q)-profit(A, q) for q in Q]), 30)

    def test_transfer(self):
        pc = lambda q: min(q, 10)*8-80
        pd = lambda q: min(q, 16)*8-112
        self.assertEqual([pc(10), pc(18)], [0, 0])
        self.assertEqual([pd(10), pd(18)], [-32, 16])
        self.assertEqual(D(".25")*pd(10) + D(".75")*pd(18), 4)


if __name__ == "__main__":
    unittest.main()
