#!/usr/bin/env python3
"""
Unit tests for Problem 4 - Stable Matrix Analyzer
"""

import unittest
from problem4_stable_matrix import check_matrix_stability


class TestStableMatrix(unittest.TestCase):

    def test_stable_3x3_matrix(self):
        # Center element: 15 = 1 + 2 + 5 + 7
        m = [
            [6,  1,  8],
            [5, 15,  7],
            [7,  2, 10]
        ]
        is_stable, count, positions, max_info = check_matrix_stability(m)
        self.assertTrue(is_stable)
        self.assertEqual(count, 0)
        self.assertEqual(positions, [])
        self.assertIsNone(max_info)

    def test_unstable_3x3_matrix_single_violation(self):
        m = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        # At (1, 1): val = 5, neighbours = 2+8+4+6 = 20, diff = |5 - 20| = 15
        is_stable, count, positions, max_info = check_matrix_stability(m)
        self.assertFalse(is_stable)
        self.assertEqual(count, 1)
        self.assertEqual(positions, [(1, 1)])
        self.assertIsNotNone(max_info)
        pos, val, n_sum, diff = max_info  # type: ignore
        self.assertEqual(pos, (1, 1))
        self.assertEqual(val, 5)
        self.assertEqual(n_sum, 20)
        self.assertEqual(diff, 15)

    def test_unstable_4x4_multiple_violations(self):
        # 4x4 matrix with interior elements at (1,1), (1,2), (2,1), (2,2)
        m = [
            [1,  2,  3,  4],
            [5, 20, 10,  6],
            [7,  8, 40,  9],
            [1,  2,  3,  4]
        ]
        # (1, 1): val=20, nSum=2(up)+8(down)+5(left)+10(right)=25, diff=|20-25|=5
        # (1, 2): val=10, nSum=3+40+20+6=69, diff=|10-69|=59
        # (2, 1): val=8,  nSum=20+2+7+40=69, diff=|8-69|=61
        # (2, 2): val=40, nSum=10+3+8+9=30,  diff=|40-30|=10
        # Max diff is at (2, 1) with diff = 61
        is_stable, count, positions, max_info = check_matrix_stability(m)
        self.assertFalse(is_stable)
        self.assertEqual(count, 4)
        self.assertEqual(positions, [(1, 1), (1, 2), (2, 1), (2, 2)])
        self.assertIsNotNone(max_info)
        pos, val, n_sum, diff = max_info  # type: ignore
        self.assertEqual(pos, (2, 1))
        self.assertEqual(val, 8)
        self.assertEqual(n_sum, 69)
        self.assertEqual(diff, 61)

    def test_small_matrices_no_interior(self):
        # 2x2 matrix
        self.assertEqual(check_matrix_stability([[1, 2], [3, 4]]), (True, 0, [], None))
        # 1x1 matrix
        self.assertEqual(check_matrix_stability([[5]]), (True, 0, [], None))
        # Empty matrix
        self.assertEqual(check_matrix_stability([]), (True, 0, [], None))


if __name__ == "__main__":
    unittest.main()
