from Problem11 import *
from Problem11 import finding_the_x_highest_adjacent_number

__author__ = 'erlafont'

import unittest


class Problem11Test(unittest.TestCase):
    def test_loading_data_grid_string_into_array(self):
        assert self.grid_array[19][19] == 48
        assert self.grid_array[0][19] == 8
        assert self.grid_array[19][0] == 1

    def test_finding_the_x_highest_adjacent_number_in_specific_direction(self):
        assert finding_the_x_highest_adjacent_number_0_degree(1, self.grid_array) == [99]
        assert finding_the_x_highest_adjacent_number_0_degree(2, self.grid_array) == [83, 97]
        assert finding_the_x_highest_adjacent_number_0_degree(3, self.grid_array) == [78, 96, 83]
        assert finding_the_x_highest_adjacent_number_0_degree(4, self.grid_array) == [78, 78, 96, 83]
        assert finding_the_x_highest_adjacent_number_90_degree(1, self.grid_array) == [99]
        assert finding_the_x_highest_adjacent_number_90_degree(2, self.grid_array) == [95, 97]
        assert finding_the_x_highest_adjacent_number_90_degree(3, self.grid_array) == [91, 88, 97]
        assert finding_the_x_highest_adjacent_number_90_degree(4, self.grid_array) == [66, 91, 88, 97]
        assert finding_the_x_highest_adjacent_number_45_degree(1, self.grid_array) == [99]
        assert finding_the_x_highest_adjacent_number_45_degree(2, self.grid_array) == [94, 99]
        assert finding_the_x_highest_adjacent_number_45_degree(3, self.grid_array) == [94, 99, 72]
        assert finding_the_x_highest_adjacent_number_45_degree(4, self.grid_array) == [94, 99, 71, 61]
        assert finding_the_x_highest_adjacent_number_135_degree(1, self.grid_array) == [99]
        assert finding_the_x_highest_adjacent_number_135_degree(2, self.grid_array) == [97, 99]
        assert finding_the_x_highest_adjacent_number_135_degree(3, self.grid_array) == [89, 94, 97]
        assert finding_the_x_highest_adjacent_number_135_degree(4, self.grid_array) == [89, 94, 97, 87]

    def setUp(self):
        self.grid_array = generate_grid(grid_data=grid_data)

    def test_finding_the_x_highest_adjacent_number(self):
        assert finding_the_x_highest_adjacent_number(1, self.grid_array) == [99]
        assert finding_the_x_highest_adjacent_number(2, self.grid_array) == [97, 99]
        assert finding_the_x_highest_adjacent_number(3, self.grid_array) == [89, 94, 97]
        assert finding_the_x_highest_adjacent_number(4, self.grid_array) == [89, 94, 97, 87]




if __name__ == '__main__':
    print(__file__, " is main!")
else:
    print(__file__, " is loaded!")
