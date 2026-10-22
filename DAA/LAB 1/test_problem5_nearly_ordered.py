#!/usr/bin/env python3
"""
Unit tests for Problem 5 - Nearly Ordered Employee Directory
"""

import unittest
from problem5_nearly_ordered_directory import (
    analyze_directory_ordering,
    compare_strings,
    parse_input
)


class TestNearlyOrderedDirectory(unittest.TestCase):

    def test_already_sorted(self):
        names = ["Amit", "Karan", "Neha", "Priya", "Rahul"]
        status, violations, swap_pos, fixed = analyze_directory_ordering(names)
        self.assertEqual(status, "ALREADY_SORTED")
        self.assertEqual(violations, [])
        self.assertIsNone(swap_pos)
        self.assertEqual(fixed, names)

    def test_adjacent_swap_needed(self):
        # Rahul and Priya swapped
        names = ["Amit", "Karan", "Neha", "Rahul", "Priya"]
        status, violations, swap_pos, fixed = analyze_directory_ordering(names)
        self.assertEqual(status, "FIXABLE_BY_SWAP")
        self.assertEqual(violations, [3])
        self.assertEqual(swap_pos, (3, 4))
        self.assertEqual(fixed, ["Amit", "Karan", "Neha", "Priya", "Rahul"])

    def test_non_adjacent_swap_needed(self):
        # Amit and Rahul swapped at ends
        names = ["Rahul", "Karan", "Neha", "Priya", "Amit"]
        status, violations, swap_pos, fixed = analyze_directory_ordering(names)
        self.assertEqual(status, "FIXABLE_BY_SWAP")
        self.assertEqual(violations, [0, 3])
        self.assertEqual(swap_pos, (0, 4))
        self.assertEqual(fixed, ["Amit", "Karan", "Neha", "Priya", "Rahul"])

    def test_unfixable_two_independent_pairs_from_pdf(self):
        # Neha > Karan (drop 1) AND Rahul > Priya (drop 2)
        names = ["Amit", "Neha", "Karan", "Rahul", "Priya"]
        status, violations, swap_pos, fixed = analyze_directory_ordering(names)
        self.assertEqual(status, "UNFIXABLE_BY_ONE_SWAP")
        self.assertEqual(violations, [1, 3])
        self.assertIsNone(swap_pos)
        self.assertIsNone(fixed)

    def test_completely_reversed_unfixable(self):
        names = ["E", "D", "C", "B", "A"]
        status, violations, swap_pos, fixed = analyze_directory_ordering(names)
        self.assertEqual(status, "UNFIXABLE_BY_ONE_SWAP")
        self.assertGreater(len(violations), 2)
        self.assertIsNone(swap_pos)

    def test_single_element_and_empty(self):
        self.assertEqual(analyze_directory_ordering(["Amit"])[0], "ALREADY_SORTED")
        self.assertEqual(analyze_directory_ordering([])[0], "ALREADY_SORTED")

    def test_two_elements_swapped(self):
        status, violations, swap_pos, fixed = analyze_directory_ordering(["B", "A"])
        self.assertEqual(status, "FIXABLE_BY_SWAP")
        self.assertEqual(swap_pos, (0, 1))
        self.assertEqual(fixed, ["A", "B"])

    def test_parse_input(self):
        self.assertEqual(parse_input("Amit, Karan, Neha"), ["Amit", "Karan", "Neha"])
        self.assertEqual(parse_input(""), [])


if __name__ == "__main__":
    unittest.main()
