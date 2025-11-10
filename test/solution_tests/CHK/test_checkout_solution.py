from lib.solutions.CHK import checkout_solution

def test_checkout_solution():

    checkout = checkout_solution.CheckoutSolution().checkout

    assert checkout("A") == 50
    assert checkout("") == 0
    assert checkout("AAA") == 130
