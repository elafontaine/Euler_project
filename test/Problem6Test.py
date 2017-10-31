from Problem6 import sum_of_the_sqare, square_of_the_sum, difference_of_square_and_sum

__author__ = 'erlafont'

import unittest


class Problem6Test(unittest.TestCase):
    def test_sum_of_the_square(self):
        assert sum_of_the_sqare(10) == 385

    def test_square_of_the_sum(self):
        assert square_of_the_sum(10) == 3025

    def test_difference(self):
        assert difference_of_square_and_sum(10) == 2640



if __name__ == '__main__':
    print(__file__, " is main!")
else:
    print(__file__, " is loaded!")