#!/usr/bin/env python3
"""
DAA Lab 1 - Problem 1: Employee Directory
Design and Analysis of Algorithm (CSDS103)

Problem Description:
An organisation maintains the names of n employees in an unsorted list.
This program arranges the names in lexicographical order without using built-in
sorting functions, and displays all names that occur more than once (or reports
that no duplicate names exist).

Input format:
Comma-separated employee names (e.g. "Amit, Neha, Amit, Rahul, Neha, Karan, Rahul")
"""

from typing import List, Tuple


def compare_strings(s1: str, s2: str) -> int:
    """
    Compares two strings lexicographically in natural dictionary order
    without using built-in sorting utilities.
    
    Case definition (Two-Tier Comparison):
    - Primary Tier: Case-insensitive alphabetical comparison ('a'/'A' < 'b'/'B' ... < 'z'/'Z').
      This groups names by alphabet regardless of capitalization (e.g., 'amit' and 'Amit'
      precede 'Neha', which precedes 'rahul' and 'Rahul').
    - Prefix Tier: If one string is a prefix of another, the shorter string comes first
      (e.g., 'Amit' < 'Amita').
    - Secondary Tier: If two strings are case-insensitively identical and have equal length,
      lowercase characters precede uppercase characters (e.g., 'amit' < 'Amit', 'rahul' < 'Rahul').
    - Exact Match: If all characters and their casings are identical, return 0.

    Returns:
        -1 if s1 < s2
         0 if s1 == s2
         1 if s1 > s2
    """
    len1 = len(s1)
    len2 = len(s2)
    min_len = len1 if len1 < len2 else len2

    # Primary Tier: Case-insensitive comparison
    for i in range(min_len):
        c1 = ord(s1[i].lower())
        c2 = ord(s2[i].lower())
        if c1 < c2:
            return -1
        elif c1 > c2:
            return 1

    # Prefix Tier: Shorter string comes first
    if len1 < len2:
        return -1
    elif len1 > len2:
        return 1

    # Secondary Tier: Case tie-breaking (lowercase precedes uppercase)
    for i in range(min_len):
        if s1[i] != s2[i]:
            if s1[i].islower() and s2[i].isupper():
                return -1
            elif s1[i].isupper() and s2[i].islower():
                return 1
            elif ord(s1[i]) < ord(s2[i]):
                return -1
            else:
                return 1

    return 0


def merge(left: List[str], right: List[str]) -> List[str]:
    """
    Merges two sorted lists of strings into a single sorted list.
    """
    result: List[str] = []
    i = 0
    j = 0
    len_left = len(left)
    len_right = len(right)

    while i < len_left and j < len_right:
        cmp = compare_strings(left[i], right[j])
        if cmp <= 0:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len_left:
        result.append(left[i])
        i += 1

    while j < len_right:
        result.append(right[j])
        j += 1

    return result


def merge_sort(arr: List[str]) -> List[str]:
    """
    Sorts a list of strings in lexicographical order using Merge Sort
    without any built-in sorting utilities.
    
    Time Complexity:
        - Best Case:    O(n * L * log n)
        - Average Case: O(n * L * log n)
        - Worst Case:   O(n * L * log n)
        where n = number of names, L = maximum length of a name.
    
    Auxiliary Space Complexity: O(n * L)
    """
    n = len(arr)
    if n <= 1:
        return list(arr)

    mid = n // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half, right_half)


def find_duplicates(sorted_arr: List[str]) -> List[Tuple[str, int]]:
    """
    Scans a sorted list of strings in a single linear pass to detect
    duplicate names and their occurrence frequencies.
    
    Time Complexity: O(n * L)
    Auxiliary Space Complexity: O(k * L) where k is the number of distinct duplicates.
    
    Returns:
        List of tuples (name, frequency) for names occurring more than once.
    """
    duplicates: List[Tuple[str, int]] = []
    n = len(sorted_arr)
    i = 0

    while i < n:
        count = 1
        while i + 1 < n and compare_strings(sorted_arr[i], sorted_arr[i + 1]) == 0:
            count += 1
            i += 1
        if count > 1:
            duplicates.append((sorted_arr[i], count))
        i += 1

    return duplicates


def parse_input(raw_input: str) -> List[str]:
    """
    Parses a comma-separated string into a list of employee names,
    trimming surrounding whitespace and filtering out empty tokens.
    """
    if not raw_input:
        return []
    
    tokens = raw_input.split(",")
    names = [name.strip() for name in tokens if name.strip()]
    return names


def process_employee_directory(raw_input: str) -> Tuple[List[str], List[str], List[Tuple[str, int]]]:
    """
    Orchestrates parsing, sorting, and duplicate detection.
    
    Returns:
        (original_names, sorted_names, duplicates)
    """
    original_names = parse_input(raw_input)
    if not original_names:
        return [], [], []

    sorted_names = merge_sort(original_names)
    duplicates = find_duplicates(sorted_names)
    return original_names, sorted_names, duplicates


def main() -> None:
    print("=" * 65)
    print("       DAA Lab 1 - Problem 1: Employee Directory Manager")
    print("=" * 65)
    print("Enter employee names separated by commas.")
    print("Example: Amit, Neha, Amit, Rahul, Neha, Karan, Rahul\n")
    
    try:
        user_input = input("Enter employee names: ")
    except (EOFError, KeyboardInterrupt):
        print("\nInput cancelled.")
        return

    original_names, sorted_names, duplicates = process_employee_directory(user_input)

    if not original_names:
        print("\n[!] No valid employee names entered. List is empty.")
        return

    print("\n" + "-" * 40)
    print(f"Total Employees (n): {len(original_names)}")
    print(f"Original Input List: {original_names}")
    print("-" * 40)
    print(f"Lexicographically Sorted Names:\n{', '.join(sorted_names)}")
    print("-" * 40)

    if duplicates:
        print(f"Duplicate Names Detected ({len(duplicates)} distinct duplicate(s)):")
        for name, count in duplicates:
            print(f"  • '{name}' appears {count} times")
    else:
        print("No duplicate names exist.")
    print("=" * 65)


if __name__ == "__main__":
    main()
