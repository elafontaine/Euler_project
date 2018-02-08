__author__ = 'erlafont'

import unittest
from Problem10 import find_all_prime_under_x

class Problem10Test(unittest.TestCase):
    def test_find_all_prime_under_x(self):
        assert find_all_prime_under_x(0) == []
        assert find_all_prime_under_x(1) == []
        assert find_all_prime_under_x(2) == []
        assert find_all_prime_under_x(3) == [2]
        assert find_all_prime_under_x(4) == [2, 3]
        assert find_all_prime_under_x(5) == [2, 3]
        assert find_all_prime_under_x(6) == [2, 3, 5]



if __name__ == '__main__':
    print(__file__, " is main!")
else:
    print(__file__, " is loaded!")