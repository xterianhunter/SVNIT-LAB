#!/usr/bin/env python3
"""
DAA Lab 1 - Problem 2: Locally Balanced Matrix
Design and Analysis of Algorithm (CSDS103)

Problem Description:
An n x n integer matrix is locally balanced if every non-boundary element
(where all 4 neighbours: up, down, left, right are present and valid) equals
the sum of its four orthogonal neighbours:
A[i][j] = A[i-1][j] + A[i+1][j] + A[i][j-1] + A[i][j+1]

Boundary elements (first row, last row, first column, last column) are ignored
since not all 4 neighbours exist for them.
"""

from typing import List, Optional, Tuple


def is_locally_balanced(matrix: List[List[int]]) -> Tuple[bool, Optional[Tuple[int, int]], Optional[int], Optional[int]]:
    """
    Checks if an n x n matrix is locally balanced for all elements having all 4 neighbours
    (i.e. leaving first row, last row, first column, and last column).

    Returns:
        (is_balanced, (row, col), element_value, neighbour_sum)
        If balanced, returns (True, None, None, None).
        If not balanced, returns (False, (row, col), value, neighbour_sum) for first violation.
    """
    n = len(matrix)
    if n < 3:
        # Matrices smaller than 3x3 have no interior elements where all 4 neighbours exist
        return True, None, None, None

    for i in range(1, n - 1):
        for j in range(1, n - 1):
            neighbour_sum = matrix[i - 1][j] + matrix[i + 1][j] + matrix[i][j - 1] + matrix[i][j + 1]
            if matrix[i][j] != neighbour_sum:
                return False, (i, j), matrix[i][j], neighbour_sum

    return True, None, None, None


def display_result(matrix: List[List[int]], title: str = "Matrix") -> None:
    """Helper to display matrix and its balance verification."""
    print(f"\n--- {title} ---")
    for row in matrix:
        print("  " + "  ".join(f"{val:4d}" for val in row))
    
    balanced, pos, val, n_sum = is_locally_balanced(matrix)
    if balanced:
        print("=> Status: Locally Balanced Matrix [✓]")
    else:
        r, c = pos  # type: ignore
        print(f"=> Status: NOT Balanced [✗]")
        print(f"   First Violation at Position (row={r}, col={c}) [0-indexed] / (row={r+1}, col={c+1}) [1-indexed]")
        print(f"   Element Value = {val}, 4-Neighbour Sum = {n_sum}")


def main() -> None:
    print("=" * 60)
    print("      DAA Lab 1 - Problem 2: Locally Balanced Matrix")
    print(" (Checking elements with all 4 valid neighbours present)")
    print("=" * 60)

    # 1. Relevant Demonstration Matrices
    m1 = [
        [6,  1,  8],
        [5, 15,  7],
        [7,  2, 10]
    ]
    display_result(m1, "Example 1: Balanced 3x3 Matrix (Center: 15 = 1+2+5+7)")

    m2 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    display_result(m2, "Example 2: Unbalanced 3x3 Matrix (Center: 5 != 2+8+4+6=20)")

    m3 = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    display_result(m3, "Example 3: Balanced 3x3 Zero Matrix")

    # 2. Interactive Input Option
    print("\n" + "=" * 60)
    print("Custom User Input (Optional)")
    print("=" * 60)
    try:
        choice = input("Would you like to test your own matrix? (y/n): ").strip().lower()
    except (EOFError, KeyboardInterrupt):
        return

    if choice == 'y':
        try:
            n = int(input("Enter matrix size n (for n x n matrix): ").strip())
            print(f"Enter {n} rows with {n} comma or space-separated integers each:")
            custom_matrix: List[List[int]] = []
            for r in range(n):
                row_str = input(f"Row {r+1}: ").replace(",", " ")
                row = [int(x) for x in row_str.split()]
                if len(row) != n:
                    print(f"Error: expected {n} elements, got {len(row)}.")
                    return
                custom_matrix.append(row)
            display_result(custom_matrix, f"Custom {n}x{n} Matrix")
        except Exception as e:
            print(f"Invalid input: {e}")


if __name__ == "__main__":
    main()
