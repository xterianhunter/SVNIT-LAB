#!/usr/bin/env python3
"""
Unit and Integration Tests for Problem 1 - Employee Directory
"""

import unittest
from problem1_employee_directory import (
    compare_strings,
    merge_sort,
    find_duplicates,
    parse_input,
    process_employee_directory
)


class TestEmployeeDirectory(unittest.TestCase):

    def test_compare_strings_basic(self):
        self.assertEqual(compare_strings("Amit", "Amit"), 0)
        self.assertEqual(compare_strings("Amit", "Neha"), -1)
        self.assertEqual(compare_strings("Neha", "Amit"), 1)
        self.assertEqual(compare_strings("Amit", "Amita"), -1)
        self.assertEqual(compare_strings("Amita", "Amit"), 1)

    def test_compare_strings_natural_dictionary_case(self):
        # Primary: 'a'/'A' < 'b'/'B' ... < 'n'/'N' ... < 'r'/'R'
        self.assertEqual(compare_strings("amit", "Neha"), -1)
        self.assertEqual(compare_strings("Amit", "Neha"), -1)
        self.assertEqual(compare_strings("Neha", "rahul"), -1)
        self.assertEqual(compare_strings("Neha", "Rahul"), -1)

        # Secondary tie-break: lowercase before uppercase
        self.assertEqual(compare_strings("amit", "Amit"), -1)
        self.assertEqual(compare_strings("Amit", "amit"), 1)
        self.assertEqual(compare_strings("rahul", "Rahul"), -1)
        self.assertEqual(compare_strings("Rahul", "rahul"), 1)

    def test_merge_sort_mixed(self):
        names = ["Rahul", "Amit", "Karan", "Neha"]
        expected = ["Amit", "Karan", "Neha", "Rahul"]
        self.assertEqual(merge_sort(names), expected)

    def test_merge_sort_with_duplicates(self):
        names = ["Amit", "Neha", "Amit", "Rahul", "Neha", "Karan", "Rahul"]
        expected = ["Amit", "Amit", "Karan", "Neha", "Neha", "Rahul", "Rahul"]
        self.assertEqual(merge_sort(names), expected)

    def test_user_mixed_case_scenario(self):
        # User requested scenario:
        # ['amit', 'Amit', 'rahul', 'Neha', 'Neha', 'Rahul'] -> ['amit', 'Amit', 'Neha', 'Neha', 'rahul', 'Rahul']
        names = ["amit", "Amit", "rahul", "Neha", "Neha", "Rahul"]
        expected = ["amit", "Amit", "Neha", "Neha", "rahul", "Rahul"]
        self.assertEqual(merge_sort(names), expected)

        duplicates = find_duplicates(expected)
        self.assertEqual(duplicates, [("Neha", 2)])

    def test_merge_sort_single_and_empty(self):
        self.assertEqual(merge_sort([]), [])
        self.assertEqual(merge_sort(["Amit"]), ["Amit"])

    def test_find_duplicates_multiple(self):
        sorted_names = ["Amit", "Amit", "Karan", "Neha", "Neha", "Rahul", "Rahul"]
        duplicates = find_duplicates(sorted_names)
        expected = [("Amit", 2), ("Neha", 2), ("Rahul", 2)]
        self.assertEqual(duplicates, expected)

    def test_find_duplicates_none(self):
        sorted_names = ["Amit", "Karan", "Neha", "Rahul", "Priya"]
        duplicates = find_duplicates(sorted_names)
        self.assertEqual(duplicates, [])

    def test_find_duplicates_all_identical(self):
        sorted_names = ["Amit", "Amit", "Amit", "Amit"]
        duplicates = find_duplicates(sorted_names)
        self.assertEqual(duplicates, [("Amit", 4)])

    def test_parse_input(self):
        raw = " Amit, Neha , Amit,Rahul ,  Neha, Karan, Rahul "
        expected = ["Amit", "Neha", "Amit", "Rahul", "Neha", "Karan", "Rahul"]
        self.assertEqual(parse_input(raw), expected)

        # Empty / whitespace only
        self.assertEqual(parse_input(""), [])
        self.assertEqual(parse_input("   , ,  "), [])

    def test_end_to_end_assignment_examples(self):
        # Example 1: PDF Example with duplicates
        input1 = "Amit, Neha, Amit, Rahul, Neha, Karan, Rahul"
        orig, sorted_res, dups = process_employee_directory(input1)
        self.assertEqual(sorted_res, ["Amit", "Amit", "Karan", "Neha", "Neha", "Rahul", "Rahul"])
        self.assertEqual(dups, [("Amit", 2), ("Neha", 2), ("Rahul", 2)])

        # Example 2: List with no duplicates
        input2 = "Amit, Karan, Neha, Rahul, Priya"
        orig, sorted_res, dups = process_employee_directory(input2)
        self.assertEqual(sorted_res, ["Amit", "Karan", "Neha", "Priya", "Rahul"])
        self.assertEqual(dups, [])

        # Example 3: User interactive scenario with mixed cases
        input3 = "amit, Amit, Rahul, Neha, rahul, Neha"
        orig, sorted_res, dups = process_employee_directory(input3)
        self.assertEqual(sorted_res, ["amit", "Amit", "Neha", "Neha", "rahul", "Rahul"])
        self.assertEqual(dups, [("Neha", 2)])


if __name__ == "__main__":
    unittest.main()
