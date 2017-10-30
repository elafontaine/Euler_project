__author__ = 'erlafont'

import unittest


def is_palindrome(number):
    return False


class Problem4Test(unittest.TestCase):
    def test_is_palindrome(self):
        assert not is_palindrome(1);

if __name__ == '__main__':
    print(__file__, " is main!")
else:
    print(__file__, " is loaded!")