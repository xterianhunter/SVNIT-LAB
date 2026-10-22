#!/usr/bin/env python3
"""
Unit tests for Problem 5 - Peak Inventory in a Warehouse
"""

import unittest
from problem5_peak_inventory import find_all_peaks


class TestPeakInventory(unittest.TestCase):

    def test_single_central_peak(self):
        m = [
            [1,  2,  1],
            [2, 10,  2],
            [1,  2,  1]
        ]
        peaks = find_all_peaks(m)
        self.assertEqual(len(peaks), 1)
        self.assertEqual(peaks[0], ((1, 1), 10))

    def test_multiple_corner_peaks(self):
        m = [
            [10,  5, 15],
            [ 2,  1,  3],
            [ 8,  4, 12]
        ]
        peaks = find_all_peaks(m)
        expected_positions = {(0, 0): 10, (0, 2): 15, (2, 0): 8, (2, 2): 12}
        self.assertEqual(len(peaks), 4)
        for pos, val in peaks:
            self.assertIn(pos, expected_positions)
            self.assertEqual(val, expected_positions[pos])

    def test_uniform_constant_matrix(self):
        m = [
            [7, 7],
            [7, 7]
        ]
        peaks = find_all_peaks(m)
        self.assertEqual(len(peaks), 4)

    def test_single_element_matrix(self):
        m = [[42]]
        peaks = find_all_peaks(m)
        self.assertEqual(peaks, [((0, 0), 42)])

    def test_1d_row_matrix(self):
        m = [[1, 5, 2, 8, 3]]
        peaks = find_all_peaks(m)
        self.assertEqual(peaks, [((0, 1), 5), ((0, 3), 8)])

    def test_1d_column_matrix(self):
        m = [[2], [9], [4]]
        peaks = find_all_peaks(m)
        self.assertEqual(peaks, [((1, 0), 9)])

    def test_empty_matrix(self):
        self.assertEqual(find_all_peaks([]), [])
        self.assertEqual(find_all_peaks([[]]), [])


if __name__ == "__main__":
    unittest.main()
