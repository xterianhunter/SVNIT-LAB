#!/usr/bin/env python3
"""
Unit tests for Problem 2 - Locally Balanced Matrix (Interior elements with 4 valid neighbours)
"""

import unittest
from problem2_locally_balanced_matrix import is_locally_balanced


class TestLocallyBalancedMatrix(unittest.TestCase):

    def test_user_balanced_3x3_matrix(self):
        # User example: center 15 = 1 (up) + 2 (down) + 5 (left) + 7 (right)
        m = [
            [6,  1,  8],
            [5, 15,  7],
            [7,  2, 10]
        ]
        self.assertEqual(is_locally_balanced(m), (True, None, None, None))

    def test_unbalanced_3x3_matrix(self):
        m = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        # At (1, 1): value = 5, neighbours = 2 (up) + 8 (down) + 4 (left) + 6 (right) = 20
        is_bal, pos, val, n_sum = is_locally_balanced(m)
        self.assertFalse(is_bal)
        self.assertEqual(pos, (1, 1))
        self.assertEqual(val, 5)
        self.assertEqual(n_sum, 20)

    def test_balanced_zero_matrix(self):
        m = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        self.assertEqual(is_locally_balanced(m), (True, None, None, None))

    def test_small_matrices_no_interior(self):
        # n < 3 matrices have no elements with 4 neighbours
        self.assertEqual(is_locally_balanced([[0, 0], [0, 0]]), (True, None, None, None))
        self.assertEqual(is_locally_balanced([[5]]), (True, None, None, None))
        self.assertEqual(is_locally_balanced([]), (True, None, None, None))

    def test_4x4_matrix_first_violation(self):
        # 4x4 matrix with interior elements at (1,1), (1,2), (2,1), (2,2)
        m = [
            [1,  2,  3, 4],
            [5, 10,  6, 7],
            [8,  9, 11, 12],
            [13, 14, 15, 16]
        ]
        # At (1, 1): val = 10, neighbours = 2(up) + 9(down) + 5(left) + 6(right) = 22 != 10
        is_bal, pos, val, n_sum = is_locally_balanced(m)
        self.assertFalse(is_bal)
        self.assertEqual(pos, (1, 1))
        self.assertEqual(val, 10)
        self.assertEqual(n_sum, 22)


if __name__ == "__main__":
    unittest.main()
