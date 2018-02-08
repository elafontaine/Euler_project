from Problem9 import is_pythagorian, pythagorian_numbers_for

__author__ = 'erlafont'

import unittest


class Problem9Test(unittest.TestCase):
    def test_find_pythagorian_number(self):
        self.assertTrue(not is_pythagorian(1, 1, 1))
        self.assertTrue(is_pythagorian(3, 4, 5))

    def test_return_all_pythagorian_number(self):
        self.assertTrue(pythagorian_numbers_for(12) == [[3, 4, 5]])
        self.assertTrue(pythagorian_numbers_for(24) == [[6, 8, 10]])


if __name__ == '__main__':
    print(__file__, " is main!")
else:
    print(__file__, " is loaded!")