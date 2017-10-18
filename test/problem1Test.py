import unittest

from problem1 import is_multiple_of_3, is_multiple_of_5, find_all_multiples_of_3_and_5_of, \
    sum_all_multiple_for_a_given_number


class Problem1(unittest.TestCase):
    def test_multiple_of_3(self):
        assert is_multiple_of_3(0)
        assert not is_multiple_of_3(2)
        assert is_multiple_of_3(3)

    def test_multiple_of_5(self):
        assert is_multiple_of_5(5)
        assert is_multiple_of_5(10)
        assert is_multiple_of_5(20)
        assert not is_multiple_of_5(1)
        assert not is_multiple_of_5(2)
        assert not is_multiple_of_5(3)
        assert not is_multiple_of_5(4)
        assert not is_multiple_of_5(6)

    def test_find_all_multiplier_for_a_given_range(self):
        assert find_all_multiples_of_3_and_5_of(10) == [3, 5, 6, 9]

    def test_sum_all_multiple_for_a_given_number(self):
        assert sum_all_multiple_for_a_given_number(10) == 23


if __name__ == '__main__':
    print(__file__, " is main!")
else:
    print(__file__, " is loaded!")