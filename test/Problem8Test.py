import unittest

from Problem8 import find_the_x_highest_adjacent_number

__author__ = 'erlafont'


class Problem8Test(unittest.TestCase):
    def test_find_the_x_highest_adjacent_number(self):
        assert find_the_x_highest_adjacent_number(4) == [9, 9, 8, 9]

if __name__ == '__main__':
    print(__file__, " is main!")
else:
    print(__file__, " is loaded!")