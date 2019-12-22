from Problem12 import return_all_factors_of_number, find_first_number_containing_x_factors

__author__ = 'erlafont'

import unittest


class Problem12Test(unittest.TestCase):
    def test_return_all_factors_of_number(self):
        self.assertEquals(return_all_factors_of_number(28), [1, 2, 4, 7, 14, 28])

    def test_find_first_number_containing_x_factors(self):
        self.assertEqual(find_first_number_containing_x_factors(1),1)
        self.assertEqual(find_first_number_containing_x_factors(5),28)
