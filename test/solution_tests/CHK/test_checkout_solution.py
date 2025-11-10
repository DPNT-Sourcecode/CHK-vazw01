from lib.solutions.CHK import checkout_solution
import unittest

class TestCheckoutSolution(unittest.TestCase):

    def setUp(self):
        self.checkout = checkout_solution.CheckoutSolution()

    def check_cases(self, cases):
        for skus, expected in cases:
            with self.subTest(skus=skus):
                got = self.checkout.checkout(skus)
                self.assertEqual(got, expected)

    def test_validation(self):
        cases = [
            ("", 0),
            ("abc", -1),
            ("A1", -1),
            (None, -1),
            (123, -1),
        ]
        self.check_cases(cases)

    def test_singles(self):
        cases = [
            ("A", 50), ("B", 30), ("C", 20), ("D", 15), ("E", 40),
            ("G", 20), ("I", 35), ("J", 60), ("L", 90), ("O", 10),
            ("S", 30), ("T", 20), ("W", 20), ("X", 90), ("Y", 10), ("Z", 50),
        ]
        self.check_cases(cases)

    def test_bundles_updated(self):
        self.check_cases([
            ("AAA", 130), ("AAAAA", 200), ("AAAAAA", 250),
            ("BB", 45), ("BBBB", 90),
            ("H" * 5, 45), ("H" * 10, 80), ("H" * 15, 125),
            ("KK", 120), ("KKK", 190),
            ("PPPPP", 200),
            ("QQQ", 80), ("QQQQQQ", 160),
            ("VV", 90), ("VVV", 130), ("VVVVV", 220),
        ])


    def test_self_free(self):
        self.check_cases([
            ("FFF", 20), ("FFFFFF", 40),
            ("UUUU", 120), ("UUUUUUUU", 240),
        ])

    def test_cross_free_E_to_B(self):
        self.check_cases([
            ("EEB", 80),
            ("EEBBB", 125),
            ("NNNM", 120),
            ("RRRQ", 150),
            ("RRRQQQQQQ", 290),
        ])

    def test_group_offer_basic(self):
        self.check_cases([
            ("STX", 45),
            ("XYZ", 45),
            ("SSS", 45),
            ("ZZZ", 45),
            ("STXZ", 62),
            ("XXXY", 62),
            ("STXV", 95),
        ])

    def test_group_offer_multi_groups(self):
        basket = "SSTTXXYYZZ"
        self.check_cases([
            (basket, 3*45 + 17),
        ])

    def test_mixed_totals(self):
        self.check_cases([
            ("GJTZ", 121),
            ("ABCDXYZ", 160),
            ("EEBBSTX", 45 + 80 + 30),
        ])

if __name__ == "__main__":
    unittest.main()