from lib.solutions.CHK import checkout_solution

def test_checkout_solution():

    checkout = checkout_solution.CheckoutSolution().checkout

    assert checkout("A") == 50
    assert checkout("") == 0
    assert checkout("AAA") == 130
    assert checkout("BB") == 45
    assert checkout("ABCD") == 115
    assert checkout("EE") == 80
    assert checkout("EEB") == 80
    assert checkout("EEBBB") == 125
    assert checkout("eed") == -1
    assert checkout(123) == -1

