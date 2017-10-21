from problem2 import fib, reverse_fib, even_fibonacci, sum_even_fib_of_value

__author__ = 'erlafont'

import unittest


class Problem2Test(unittest.TestCase):
    def test_fibonacci(self):
        assert fib(1) == 1
        assert fib(2) == 2
        assert fib(3) == 3
        assert fib(4) == 5
        assert fib(5) == 8
        assert fib(6) == 13
        assert fib(7) == 21
        assert fib(8) == 34

    def test_find_term_of_fibonacci_value(self):
        assert reverse_fib(1) == 1
        assert reverse_fib(2) == 2
        assert reverse_fib(3) == 3
        assert reverse_fib(4) == 3
        assert reverse_fib(5) == 4
        assert reverse_fib(6) == 4
        assert reverse_fib(7) == 4
        assert reverse_fib(8) == 5
        assert reverse_fib(9) == 5
        assert reverse_fib(10) == 5
        assert reverse_fib(11) == 5
        assert reverse_fib(13) == 6
        assert reverse_fib(34) == 8
        assert reverse_fib(36) == 8

    def test_find_all_even_fibonnaci_of_giver_index(self):
        assert even_fibonacci(1, []) == []
        assert even_fibonacci(2, []) == [2]
        assert even_fibonacci(4, []) == [2]
        assert even_fibonacci(5, []) == [2, 8]
        assert even_fibonacci(8, []) == [2, 8, 34]

    def test_find_all_even_fibonnaci_of_given_value(self):
        assert sum_even_fib_of_value(2) == 2
        assert sum_even_fib_of_value(3) == 2
        assert sum_even_fib_of_value(8) == 10
        assert sum_even_fib_of_value(34) == 44


if __name__ == '__main__':
    print(__file__, " is main!")
else:
    print(__file__, " is loaded!")