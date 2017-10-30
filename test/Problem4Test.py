from Problem4 import find_largest_palindrome, is_palindrome

__author__ = 'erlafont'

import unittest


class Problem4Test(unittest.TestCase):
    def test_is_palindrome(self):
        assert is_palindrome(1)
        assert is_palindrome(2)
        assert not is_palindrome(10)
        assert is_palindrome(11)
        assert is_palindrome(99)
        assert is_palindrome(989)
        assert is_palindrome(1234567890987654321)

    def test_find_largest_palindrome(self):
        assert (99,91) == find_largest_palindrome(2)

if __name__ == '__main__':
    print(__file__, " is main!")
else:
    print(__file__, " is loaded!")