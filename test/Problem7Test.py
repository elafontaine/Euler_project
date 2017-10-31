from Problem7 import find_all_x_prime_numbers

__author__ = 'erlafont'
import unittest


class Problem7Test(unittest.TestCase):
    def test_find_all_x_prime_numbers(self):
        assert find_all_x_prime_numbers(6) == [2, 3, 5, 7, 11, 13]

    def test_find_the_xest_prime(self):
        assert 13 == find_all_x_prime_numbers(6)[-1]

if __name__ == '__main__':
    print(__file__, " is main!")
else:
    print(__file__, " is loaded!")