#!/usr/bin/env python3
"""
DAA Lab 1 - Problem 6: Dominant Element (Majority Element)
Design and Analysis of Algorithm (CSDS103)

Problem Description:
Given an integer array of size n, determine whether there exists an element
that occurs strictly more than half of the time (i.e. count > floor(n / 2)).

This program implements and compares two solutions:
  1. Approach 1: Repeated Counting / Comparisons (O(n^2) time, O(1) space)
  2. Approach 2: Boyer-Moore Voting Algorithm (O(n) time, O(1) space)

Example:
  Input:  2, 2, 1, 2, 3, 2, 2
  Output: Dominant Element = 2 (Count: 5 > 7/2)
"""

from typing import List, Optional, Tuple


def find_dominant_brute_force(arr: List[int]) -> Optional[Tuple[int, int]]:
    """
    Approach 1: Repeated Counting / Comparison.
    
    Algorithm:
      For each element arr[i], count its total occurrences across the array.
      If count > floor(n / 2), return (arr[i], count).
      
    Time Complexity:
      - Best Case:    O(n)   (First element tested is dominant)
      - Worst Case:   O(n^2) (No dominant element or dominant element is last)
      - Average Case: O(n^2)
      
    Auxiliary Space Complexity: O(1)
    """
    n = len(arr)
    if n == 0:
        return None

    threshold = n // 2

    for i in range(n):
        count = 0
        for j in range(n):
            if arr[j] == arr[i]:
                count += 1
        if count > threshold:
            return arr[i], count

    return None


def find_dominant_boyer_moore(arr: List[int]) -> Optional[Tuple[int, int]]:
    """
    Approach 2: Boyer-Moore Voting Algorithm (Optimal O(n) Time, O(1) Space).
    
    Algorithm:
      Phase 1 (Candidate Selection):
        Maintain a candidate and a counter. Increment when encountering the candidate,
        decrement when encountering a different element. When count reaches 0, select
        the current element as the new candidate.
      
      Phase 2 (Verification):
        Verify the candidate by counting its actual occurrences across the array.
        If actual count > floor(n / 2), return (candidate, count).
        
    Time Complexity:
      - Phase 1: O(n)
      - Phase 2: O(n)
      - Total:   O(n) in all cases (Best, Worst, Average)
      
    Auxiliary Space Complexity: O(1) (requires only 2 scalar variables: candidate & count)
    """
    n = len(arr)
    if n == 0:
        return None

    threshold = n // 2

    # Phase 1: Find candidate
    candidate: Optional[int] = None
    count = 0
    for num in arr:
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate:
            count += 1
        else:
            count -= 1

    if candidate is None:
        return None

    # Phase 2: Verify candidate
    actual_count = 0
    for num in arr:
        if num == candidate:
            actual_count += 1

    if actual_count > threshold:
        return candidate, actual_count

    return None


def parse_input(raw_input: str) -> List[int]:
    """Parses comma or space-separated integers into a list."""
    if not raw_input:
        return []
    clean_str = raw_input.replace(",", " ")
    return [int(x) for x in clean_str.split()]


def display_comparison_report(arr: List[int], title: str = "Array") -> None:
    """Helper to display the array, majority threshold, and comparative results."""
    n = len(arr)
    threshold = n // 2
    print(f"\n--- {title} ---")
    print(f"Array Elements ({n} items) : {arr}")
    print(f"Majority Threshold (> n/2): > {threshold} occurrences")

    res1 = find_dominant_brute_force(arr)
    res2 = find_dominant_boyer_moore(arr)

    print(f"\nApproach 1 (Repeated Counting, O(n^2) time, O(1) space):")
    if res1:
        elem, cnt = res1
        print(f"  => Dominant Element Found: {elem} (Occurs {cnt} times > {threshold}) [✓]")
    else:
        print("  => No dominant element exists. [✗]")

    print(f"Approach 2 (Boyer-Moore Voting, O(n)   time, O(1) space):")
    if res2:
        elem, cnt = res2
        print(f"  => Dominant Element Found: {elem} (Occurs {cnt} times > {threshold}) [✓]")
    else:
        print("  => No dominant element exists. [✗]")


def main() -> None:
    print("=" * 68)
    print("        DAA Lab 1 - Problem 6: Dominant Element Finder")
    print("=" * 68)

    # 1. Demonstration Cases
    d1 = [2, 2, 1, 2, 3, 2, 2]
    display_comparison_report(d1, "Example 1: Lab Sheet Example (Dominant = 2)")

    d2 = [1, 2, 3, 4, 2, 2]
    display_comparison_report(d2, "Example 2: No Dominant Element (2 occurs 3 times, need > 3)")

    d3 = [42]
    display_comparison_report(d3, "Example 3: Single-Element Array (Dominant = 42)")

    d4 = [-5, -5, 2, -5]
    display_comparison_report(d4, "Example 4: Negative Integers (Dominant = -5)")

    # 2. Interactive User Input
    print("\n" + "=" * 68)
    print("Custom User Input (Optional)")
    print("=" * 68)
    print("Enter comma-separated integers (or press Enter to exit):")
    try:
        user_str = input("Integer array: ")
    except (EOFError, KeyboardInterrupt):
        return

    try:
        custom_arr = parse_input(user_str)
        if custom_arr:
            display_comparison_report(custom_arr, "Custom Array")
        else:
            print("No valid integers entered.")
    except Exception as e:
        print(f"Invalid input: {e}")


if __name__ == "__main__":
    main()
