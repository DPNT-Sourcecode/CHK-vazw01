from lib.solutions.CHK import checkout_solution

def test_checkout_solution():

    checkout = checkout_solution.CheckoutSolution()

    assert checkout.checkout("A") == 50
    assert checkout.checkout("B") == 30
    assert checkout.checkout("C") == 20
    assert checkout.checkout("D") == 15
    assert checkout.checkout("ABCD") == 115
    assert checkout.checkout("AAA") == 130
    assert checkout.checkout("AAABBB") == 205
    assert checkout.checkout("AAAA") == 180
    assert checkout.checkout("AAABB") == 175
    assert checkout.checkout("AAABBBCCC") == 265
    assert checkout.checkout("XYZ") == -1
    assert checkout.checkout("A1B2") == -1
    assert checkout.checkout("") == -1
    assert checkout.checkout(123) == -1
    assert checkout.checkout(None) == -1
    assert checkout.checkout("aabb") == -1
    assert checkout.checkout("AAaaBBbb") == -1
    assert checkout.checkout("AAAAAA") == 260
    assert checkout.checkout("BBBB") == 90
    assert checkout.checkout("CCCC") == 80
    assert checkout.checkout("DDDD") == 60



