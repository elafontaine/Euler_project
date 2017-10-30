from Problem5 import find_lowest_multiple, is_divisible_by_all_number_under

__author__ = 'erlafont'

import unittest


class Problem5Test(unittest.TestCase):
    def test_is_divisible_by_all_number_under(self):
        assert is_divisible_by_all_number_under(10, 2520)

    def test_find_lowest_multiple(self):
        assert 2520 == find_lowest_multiple(10)
        assert 232792560 == find_lowest_multiple(20)

if __name__ == '__main__':
    print(__file__, " is main!")
else:
    print(__file__, " is loaded!")