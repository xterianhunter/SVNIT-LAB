#!/usr/bin/env python3
"""
DAA Lab 1 - Problem 4: Stable Matrix
Design and Analysis of Algorithm (CSDS103)

Problem Description:
An n x n integer matrix is called stable if every non-boundary element satisfies:
    A[i][j] = A[i-1][j] + A[i+1][j] + A[i][j-1] + A[i][j+1]

If the matrix is not stable, this program reports:
  1. Total number of violating elements.
  2. Exact coordinate positions of all violating elements.
  3. The position, value, neighbour sum, and maximum absolute difference:
     D(i, j) = |A[i][j] - (A[i-1][j] + A[i+1][j] + A[i][j-1] + A[i][j+1])|
"""

from typing import List, Optional, Tuple


def check_matrix_stability(
    matrix: List[List[int]]
) -> Tuple[bool, int, List[Tuple[int, int]], Optional[Tuple[Tuple[int, int], int, int, int]]]:
    """
    Evaluates stability of non-boundary elements (1 <= i <= n-2, 1 <= j <= n-2).
    
    Returns:
        (is_stable, violation_count, violating_positions, max_diff_info)
        where max_diff_info = ((row, col), val, neighbour_sum, max_diff)
    """
    n = len(matrix)
    if n < 3:
        # Matrices smaller than 3x3 have no non-boundary elements
        return True, 0, [], None

    violating_positions: List[Tuple[int, int]] = []
    max_diff = -1
    max_diff_info: Optional[Tuple[Tuple[int, int], int, int, int]] = None

    for i in range(1, n - 1):
        for j in range(1, n - 1):
            neighbour_sum = matrix[i - 1][j] + matrix[i + 1][j] + matrix[i][j - 1] + matrix[i][j + 1]
            diff = abs(matrix[i][j] - neighbour_sum)

            if diff > 0:
                violating_positions.append((i, j))
                if diff > max_diff:
                    max_diff = diff
                    max_diff_info = ((i, j), matrix[i][j], neighbour_sum, diff)

    if not violating_positions:
        return True, 0, [], None

    return False, len(violating_positions), violating_positions, max_diff_info


def display_stability_report(matrix: List[List[int]], title: str = "Matrix") -> None:
    """Prints formatted matrix and its stability analysis."""
    print(f"\n--- {title} ---")
    for row in matrix:
        print("  " + "  ".join(f"{val:4d}" for val in row))

    is_stable, count, positions, max_info = check_matrix_stability(matrix)

    if is_stable:
        print("=> Stability Status: STABLE [✓]")
        print("   All non-boundary elements satisfy A[i][j] = sum(neighbours).")
    else:
        print(f"=> Stability Status: NOT STABLE [✗]")
        print(f"   • Total Violating Non-Boundary Elements: {count}")
        print(f"   • Violating Positions (0-indexed): {positions}")
        if max_info:
            (r, c), val, n_sum, diff = max_info
            print(f"   • Maximum Absolute Difference D(i, j):")
            print(f"     Position        : (row={r}, col={c}) [0-indexed] / (row={r+1}, col={c+1}) [1-indexed]")
            print(f"     Element Value   : {val}")
            print(f"     Neighbour Sum   : {n_sum}")
            print(f"     Max |Difference|: D({r}, {c}) = |{val} - {n_sum}| = {diff}")


def main() -> None:
    print("=" * 65)
    print("         DAA Lab 1 - Problem 4: Stable Matrix Analyzer")
    print("=" * 65)

    # 1. Demonstration Matrices
    m1 = [
        [6,  1,  8],
        [5, 15,  7],
        [7,  2, 10]
    ]
    display_report_title = "Example 1: Stable 3x3 Matrix (Center: 15 = 1+2+5+7)"
    display_stability_report(m1, display_report_title)

    m2 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    display_stability_report(m2, "Example 2: Unstable 3x3 Matrix (Single Violation)")

    m3 = [
        [1,  2,  3,  4],
        [5, 20, 10,  6],
        [7,  8, 40,  9],
        [1,  2,  3,  4]
    ]
    display_stability_report(m3, "Example 3: 4x4 Matrix with Multiple Violations")

    # 2. Interactive Input Option
    print("\n" + "=" * 65)
    print("Custom User Input (Optional)")
    print("=" * 65)
    try:
        choice = input("Would you like to test your own matrix? (y/n): ").strip().lower()
    except (EOFError, KeyboardInterrupt):
        return

    if choice == 'y':
        try:
            n = int(input("Enter matrix size n (for n x n matrix): ").strip())
            print(f"Enter {n} rows with {n} space or comma-separated integers each:")
            custom_matrix: List[List[int]] = []
            for r in range(n):
                row_str = input(f"Row {r+1}: ").replace(",", " ")
                row = [int(x) for x in row_str.split()]
                if len(row) != n:
                    print(f"Error: expected {n} elements, got {len(row)}.")
                    return
                custom_matrix.append(row)
            display_stability_report(custom_matrix, f"Custom {n}x{n} Matrix")
        except Exception as e:
            print(f"Invalid input: {e}")


if __name__ == "__main__":
    main()
