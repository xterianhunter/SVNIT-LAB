#!/usr/bin/env python3
"""
Unit tests for Problem 6 - Dominant Element Finder
"""

import unittest
from problem6_dominant_element import (
    find_dominant_brute_force,
    find_dominant_boyer_moore,
    parse_input
)


class TestDominantElement(unittest.TestCase):

    def test_lab_sheet_example(self):
        arr = [2, 2, 1, 2, 3, 2, 2]
        self.assertEqual(find_dominant_brute_force(arr), (2, 5))
        self.assertEqual(find_dominant_boyer_moore(arr), (2, 5))

    def test_no_dominant_element(self):
        arr = [1, 2, 3, 4, 2, 2]  # 2 occurs 3 times, n=6, threshold=3 (needs > 3)
        self.assertIsNone(find_dominant_brute_force(arr))
        self.assertIsNone(find_dominant_boyer_moore(arr))

    def test_all_identical(self):
        arr = [7, 7, 7, 7]
        self.assertEqual(find_dominant_brute_force(arr), (7, 4))
        self.assertEqual(find_dominant_boyer_moore(arr), (7, 4))

    def test_exact_half_not_dominant(self):
        arr = [1, 1, 2, 2]  # n=4, threshold=2 (2 is not > 2)
        self.assertIsNone(find_dominant_brute_force(arr))
        self.assertIsNone(find_dominant_boyer_moore(arr))

    def test_single_element(self):
        arr = [42]
        self.assertEqual(find_dominant_brute_force(arr), (42, 1))
        self.assertEqual(find_dominant_boyer_moore(arr), (42, 1))

    def test_negative_integers(self):
        arr = [-5, -5, 2, -5]
        self.assertEqual(find_dominant_brute_force(arr), (-5, 3))
        self.assertEqual(find_dominant_boyer_moore(arr), (-5, 3))

    def test_empty_array(self):
        self.assertIsNone(find_dominant_brute_force([]))
        self.assertIsNone(find_dominant_boyer_moore([]))

    def test_parse_input(self):
        self.assertEqual(parse_input("2, 2, 1, 2, 3, 2, 2"), [2, 2, 1, 2, 3, 2, 2])
        self.assertEqual(parse_input(" -5,  10, -20 "), [-5, 10, -20])
        self.assertEqual(parse_input(""), [])


if __name__ == "__main__":
    unittest.main()
