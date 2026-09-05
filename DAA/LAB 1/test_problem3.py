#!/usr/bin/env python3
"""
Unit and Integration Tests for Problem 3 - First Unique Employee
"""

import unittest
from problem3_first_unique_employee import (
    find_first_unique_brute_force,
    find_first_unique_hash_map,
    parse_input
)


class TestFirstUniqueEmployee(unittest.TestCase):

    def test_pdf_example(self):
        names = ["Amit", "Neha", "Amit", "Rahul", "Neha", "Karan", "Rahul"]
        self.assertEqual(find_first_unique_brute_force(names), "Karan")
        self.assertEqual(find_first_unique_hash_map(names), "Karan")

    def test_all_unique(self):
        names = ["Amit", "Neha", "Karan", "Rahul"]
        self.assertEqual(find_first_unique_brute_force(names), "Amit")
        self.assertEqual(find_first_unique_hash_map(names), "Amit")

    def test_no_unique_elements(self):
        names = ["Amit", "Neha", "Amit", "Neha"]
        self.assertIsNone(find_first_unique_brute_force(names))
        self.assertIsNone(find_first_unique_hash_map(names))

    def test_single_element(self):
        names = ["Karan"]
        self.assertEqual(find_first_unique_brute_force(names), "Karan")
        self.assertEqual(find_first_unique_hash_map(names), "Karan")

    def test_empty_list(self):
        names = []
        self.assertIsNone(find_first_unique_brute_force(names))
        self.assertIsNone(find_first_unique_hash_map(names))

    def test_unique_at_end(self):
        names = ["A", "B", "A", "B", "C"]
        self.assertEqual(find_first_unique_brute_force(names), "C")
        self.assertEqual(find_first_unique_hash_map(names), "C")

    def test_unique_at_beginning(self):
        names = ["Z", "A", "B", "A", "B"]
        self.assertEqual(find_first_unique_brute_force(names), "Z")
        self.assertEqual(find_first_unique_hash_map(names), "Z")

    def test_parse_input(self):
        raw = " Amit, Neha , Amit,Rahul ,  Neha, Karan, Rahul "
        expected = ["Amit", "Neha", "Amit", "Rahul", "Neha", "Karan", "Rahul"]
        self.assertEqual(parse_input(raw), expected)
        self.assertEqual(parse_input(""), [])
        self.assertEqual(parse_input("   , , "), [])


if __name__ == "__main__":
    unittest.main()
