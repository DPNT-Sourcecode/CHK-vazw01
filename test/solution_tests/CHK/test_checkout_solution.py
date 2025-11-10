from lib.solutions.CHK import checkout_solution
import unittest

class TestCheckoutSolution(unittest.TestCase):

    def setUp(self):
        self.checkout = checkout_solution.CheckoutSolution()

    def check_cases(self, cases):
        for skus, expected in cases:
            with self.subTest(skus=skus):
                got = self.sol.checkout(skus)
                self.assertEqual(got, expected)

    def test_validation(self):
        cases = [
            ("", 0),
            ("abc", -1),   # lowercase illegal
            ("A1", -1),    # digit illegal
            (None, -1),    # non-string
            (123, -1),     # non-string
        ]
        self.check_cases(cases)

    def test_singles(self):
        cases = [
            ("A", 50), ("B", 30), ("C", 20), ("D", 15), ("E", 40),
            ("G", 20), ("I", 35), ("J", 60), ("L", 90), ("O", 10),
            ("S", 30), ("T", 20), ("W", 20), ("X", 90), ("Y", 10), ("Z", 50),
        ]
        self.check_cases(cases)

    def test_A_bundles(self):
        cases = [
            ("AA", 100), ("AAA", 130), ("AAAA", 180), ("AAAAA", 200),
            ("AAAAAA", 250), ("AAAAAAAAAA", 400),
        ]
        self.check_cases(cases)

    def test_B_bundles(self):
        cases = [
            ("B", 30), ("BB", 45), ("BBB", 75), ("BBBB", 90), ("BBBBBB", 135),
        ]
        self.check_cases(cases)

    def test_H_bundles(self):
        cases = [
            ("H", 10),
            ("HHHHH", 45),
            ("H"*10, 80),
            ("H"*15, 125),
            ("H"*16, 135),
            ("H"*25, 205),
        ]
        self.check_cases(cases)

    def test_K_bundles(self):
        cases = [("K", 80), ("KK", 150), ("KKK", 230)]
        self.check_cases(cases)

    def test_P_bundles(self):
        cases = [("PPPP", 200), ("PPPPP", 200), ("PPPPPP", 250), ("PPPPPQQQ", 280)]
        self.check_cases(cases)

    def test_Q_bundles(self):
        cases = [("QQQ", 80), ("QQQQ", 110), ("QQQQQQ", 160)]
        self.check_cases(cases)

    def test_V_bundles(self):
        cases = [
            ("V", 50), ("VV", 90), ("VVV", 130), ("VVVV", 180),
            ("VVVVV", 220), ("VVVVVV", 260), ("V"*7, 310),
            ("V"*8, 350), ("V"*9, 390), ("V"*10, 440),
        ]
        self.check_cases(cases)

    def test_self_free_F(self):
        cases = [
            ("F", 10), ("FF", 20), ("FFF", 20), ("FFFF", 30),
            ("FFFFFF", 40), ("FFFFFFF", 50),
        ]
        self.check_cases(cases)

    def test_self_free_U(self):
        cases = [
            ("U", 40), ("UUU", 120), ("UUUU", 120),
            ("UUUUU", 160), ("UUUUUUUU", 240),
        ]
        self.check_cases(cases)
