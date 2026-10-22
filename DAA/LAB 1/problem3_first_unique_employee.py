#!/usr/bin/env python3
"""
DAA Lab 1 - Problem 3: First Unique Employee
Design and Analysis of Algorithm (CSDS103)

Problem Description:
A company records the sequence in which employees access a system.
An employee is called unique if their name occurs exactly once in the complete sequence.
This program implements two solutions to find the first unique employee name:
  1. In-place repeated comparisons (Approach 1: O(n^2) time, O(1) space)
  2. Auxiliary frequency map (Approach 2: O(n) time, O(n) space)

Example:
  Input:  Amit, Neha, Amit, Rahul, Neha, Karan, Rahul
  Output: Karan
"""

from typing import Dict, List, Optional, Tuple


def find_first_unique_brute_force(names: List[str]) -> Optional[str]:
    """
    Approach 1: Using only the given list and repeated comparisons.
    
    Algorithm:
      For each name at index i, scan the entire list to check if it appears
      at any other index j != i. Return the first name that has no duplicate.
      
    Time Complexity:
      - Best Case:    O(n * L)  (First element is unique)
      - Worst Case:   O(n^2 * L) (No unique element or last element is unique)
      - Average Case: O(n^2 * L)
    
    Auxiliary Space Complexity: O(1)
    """
    n = len(names)
    for i in range(n):
        is_unique = True
        for j in range(n):
            if i != j and names[i] == names[j]:
                is_unique = False
                break
        if is_unique:
            return names[i]
    return None


def find_first_unique_hash_map(names: List[str]) -> Optional[str]:
    """
    Approach 2: Using an additional data structure (frequency map / hash table).
    
    Algorithm:
      1. First Pass: Count the frequency of each employee name in a hash map.
      2. Second Pass: Traverse the original list in access order and return the
         first name whose frequency count is exactly 1.
         
    Time Complexity:
      - Best Case:    O(n * L)
      - Worst Case:   O(n * L) (with uniform hashing)
      - Average Case: O(n * L)
      
    Auxiliary Space Complexity: O(u * L) where u <= n is the number of distinct names.
    """
    # Pass 1: Build frequency map
    freq: Dict[str, int] = {}
    for name in names:
        freq[name] = freq.get(name, 0) + 1

    # Pass 2: Find the first name with frequency 1
    for name in names:
        if freq[name] == 1:
            return name

    return None


def parse_input(raw_input: str) -> List[str]:
    """
    Parses comma-separated names into a list, stripping whitespace.
    """
    if not raw_input:
        return []
    return [name.strip() for name in raw_input.split(",") if name.strip()]


def run_comparison(names: List[str]) -> Tuple[Optional[str], Optional[str]]:
    """
    Executes both approaches and returns their results.
    """
    res1 = find_first_unique_brute_force(names)
    res2 = find_first_unique_hash_map(names)
    return res1, res2


def main() -> None:
    print("=" * 65)
    print("       DAA Lab 1 - Problem 3: First Unique Employee")
    print("=" * 65)

    # 1. Built-in Demonstration Example from PDF
    demo_input = "Amit, Neha, Amit, Rahul, Neha, Karan, Rahul"
    demo_names = parse_input(demo_input)

    print("\n--- Built-in Example (From Lab Sheet) ---")
    print(f"Access Sequence : {demo_input}")
    print(f"Parsed List     : {demo_names}")
    
    ans1, ans2 = run_comparison(demo_names)
    print(f"Approach 1 (Repeated Comparisons, O(n^2) time, O(1) space): {ans1}")
    print(f"Approach 2 (Frequency Map,        O(n)   time, O(n) space): {ans2}")

    # 2. Interactive Input
    print("\n" + "=" * 65)
    print("Custom User Input")
    print("=" * 65)
    print("Enter comma-separated employee access sequence (or press Enter to exit):")
    try:
        user_str = input("Employee names: ")
    except (EOFError, KeyboardInterrupt):
        return

    names = parse_input(user_str)
    if not names:
        print("No valid names entered.")
        return

    print("\n" + "-" * 40)
    print(f"Total Access Records (n): {len(names)}")
    print(f"Sequence: {names}")
    print("-" * 40)

    ans_brute, ans_hash = run_comparison(names)

    if ans_brute is not None:
        print(f"First Unique Employee: '{ans_brute}'")
    else:
        print("No unique employee found in the access sequence.")
    print("=" * 65)


if __name__ == "__main__":
    main()
