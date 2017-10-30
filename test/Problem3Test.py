from Problem3 import is_prime, find_all_prime_factors

__author__ = 'erlafont'

import unittest


class Problem3Test(unittest.TestCase):
    def test_is_prime(self):
        assert is_prime(1)
        assert is_prime(2)
        assert is_prime(3)
        assert not is_prime(4)
        assert is_prime(5)
        assert not is_prime(6)
        assert is_prime(7)
        assert not is_prime(8)
        assert not is_prime(9)
        assert not is_prime(10)
        assert is_prime(11)
        assert not is_prime(12)
        assert is_prime(13)
        assert not is_prime(14)
        assert not is_prime(15)
        assert not is_prime(16)
        assert is_prime(17)
        assert is_prime(19)
        assert not is_prime(21)
        assert is_prime(23)
        assert not is_prime(25)
        assert not is_prime(35)

    def test_find_all_prime_factors_of_a_number(self):
        assert find_all_prime_factors(2) == []
        assert find_all_prime_factors(3) == []
        assert find_all_prime_factors(4) == [2]
        assert find_all_prime_factors(6) == [2, 3]
        assert find_all_prime_factors(7) == []
#        assert find_all_prime_factors(600851475143)
        assert find_all_prime_factors(13195) == [5, 7, 13, 29]
        

if __name__ == '__main__':
    print(__file__, " is main!")
else:
    print(__file__, " is loaded!")