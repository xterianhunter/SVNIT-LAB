#!/usr/bin/env python3
"""
DAA Lab 1 - Problem 5: Nearly Ordered Employee Directory
Design and Analysis of Algorithm (CSDS103)

Problem Description:
An employee directory containing n names is expected to be in lexicographical order,
but due to data-entry errors, some names may have been placed incorrectly.
This program:
  1. Determines whether the directory is already sorted without sorting the full array.
  2. Identifies all adjacent positions where the ordering is violated (A[i] > A[i+1]).
  3. Determines whether exchanging only two names can restore the sorted order.
  4. If fixable, reports the two positions and names to be swapped.
"""

from typing import List, Optional, Tuple


def compare_strings(s1: str, s2: str) -> int:
    """
    Two-tier natural dictionary comparison:
      - Primary: Case-insensitive character comparison
      - Length: Shorter prefix comes before longer string
      - Secondary: Lowercase precedes uppercase on tie
    Returns:
      -1 if s1 < s2, 0 if s1 == s2, +1 if s1 > s2
    """
    min_len = min(len(s1), len(s2))
    for i in range(min_len):
        c1_low, c2_low = s1[i].lower(), s2[i].lower()
        if c1_low != c2_low:
            return -1 if c1_low < c2_low else 1

    if len(s1) != len(s2):
        return -1 if len(s1) < len(s2) else 1

    # Secondary tie-breaking: lowercase before uppercase
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            if s1[i].islower() and s2[i].isupper():
                return -1
            if s1[i].isupper() and s2[i].islower():
                return 1
            return -1 if s1[i] < s2[i] else 1

    return 0


def analyze_directory_ordering(
    names: List[str]
) -> Tuple[str, List[int], Optional[Tuple[int, int]], Optional[List[str]]]:
    """
    Analyzes an employee directory for sortedness and single-swap fixability.
    
    Returns:
        (status, violation_indices, swap_positions, fixed_names_list)
        where status is one of:
          - "ALREADY_SORTED"
          - "FIXABLE_BY_SWAP"
          - "UNFIXABLE_BY_ONE_SWAP"
    """
    n = len(names)
    if n <= 1:
        return "ALREADY_SORTED", [], None, names.copy()

    # Step 1: Detect all adjacent ordering violations in a single pass O(n)
    violations: List[int] = []
    for i in range(n - 1):
        if compare_strings(names[i], names[i + 1]) > 0:
            violations.append(i)

    # If no violations, the list is already sorted
    if not violations:
        return "ALREADY_SORTED", [], None, names.copy()

    # Step 2: Determine candidate swap indices (x, y)
    if len(violations) == 1:
        # Adjacent elements were swapped
        x = violations[0]
        y = violations[0] + 1
    elif len(violations) == 2:
        # Non-adjacent elements were swapped
        x = violations[0]
        y = violations[1] + 1
    else:
        # More than 2 drops cannot be resolved by a single swap
        return "UNFIXABLE_BY_ONE_SWAP", violations, None, None

    # Step 3: Verify whether swapping names[x] and names[y] makes the list sorted
    names_copy = names.copy()
    names_copy[x], names_copy[y] = names_copy[y], names_copy[x]

    is_sorted = True
    for k in range(n - 1):
        if compare_strings(names_copy[k], names_copy[k + 1]) > 0:
            is_sorted = False
            break

    if is_sorted:
        return "FIXABLE_BY_SWAP", violations, (x, y), names_copy
    else:
        return "UNFIXABLE_BY_ONE_SWAP", violations, None, None


def parse_input(raw_input: str) -> List[str]:
    """Parses comma-separated names, stripping whitespace."""
    if not raw_input:
        return []
    return [name.strip() for name in raw_input.split(",") if name.strip()]


def display_analysis_report(names: List[str], title: str = "Directory") -> None:
    """Helper to display formatted analysis output."""
    print(f"\n--- {title} ---")
    print(f"Sequence ({len(names)} names): {names}")

    status, violations, swap_pos, fixed_list = analyze_directory_ordering(names)

    if status == "ALREADY_SORTED":
        print("=> Status: Already Sorted [✓]")
        print("   No ordering violations found.")
    else:
        print("=> Status: Ordering Violations Detected [✗]")
        print(f"   • Total Violations: {len(violations)}")
        for v in violations:
            print(f"     - Violation at Index {v} (0-indexed) / Position {v+1} (1-indexed): '{names[v]}' > '{names[v+1]}'")

        if status == "FIXABLE_BY_SWAP":
            x, y = swap_pos  # type: ignore
            print(f"\n=> Single-Swap Restoration: POSSIBLE [✓]")
            print(f"   Exchange Position {x+1} ('{names[x]}') and Position {y+1} ('{names[y]}') [1-indexed]")
            print(f"   (0-indexed indices: {x} and {y})")
            print(f"   Resulting Sorted Directory: {fixed_list}")
        else:
            print(f"\n=> Single-Swap Restoration: NOT POSSIBLE [✗]")
            print("   Exchanging only two names cannot make the complete list sorted.")


def main() -> None:
    print("=" * 68)
    print("   DAA Lab 1 - Problem 5: Nearly Ordered Employee Directory")
    print("=" * 68)

    # 1. Demonstration Cases
    d1 = ["Amit", "Karan", "Neha", "Priya", "Rahul"]
    display_analysis_report(d1, "Example 1: Already Sorted Directory")

    d2 = ["Amit", "Karan", "Neha", "Rahul", "Priya"]
    display_analysis_report(d2, "Example 2: Single Adjacent Violation (Rahul > Priya)")

    d3 = ["Rahul", "Karan", "Neha", "Priya", "Amit"]
    display_analysis_report(d3, "Example 3: Non-Adjacent Swap Needed (Swap Rahul and Amit)")

    d4 = ["Amit", "Neha", "Karan", "Rahul", "Priya"]
    display_analysis_report(d4, "Example 4: From PDF (2 Inverted Pairs, Unfixable with 1 Swap)")

    # 2. Interactive Input
    print("\n" + "=" * 68)
    print("Custom User Input (Optional)")
    print("=" * 68)
    print("Enter comma-separated employee names (or press Enter to exit):")
    try:
        user_str = input("Employee names: ")
    except (EOFError, KeyboardInterrupt):
        return

    custom_names = parse_input(user_str)
    if custom_names:
        display_analysis_report(custom_names, "Custom Employee Directory")
    else:
        print("No valid names entered.")


if __name__ == "__main__":
    main()
