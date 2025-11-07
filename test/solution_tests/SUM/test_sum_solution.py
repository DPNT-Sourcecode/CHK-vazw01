from solutions.SUM.sum_solution import SumSolution


class TestSum():
    def test_sum(self):
        assert SumSolution().compute(1, 2) == 3

def test_add_two_numbers():
    from challenges.SUM_R1 import add_two_numbers

    assert add_two_numbers(1, 2) == 3
