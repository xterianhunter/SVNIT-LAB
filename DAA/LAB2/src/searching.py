"""Core searching algorithms: Linear Search and Binary Search.

Implemented from first principles without using standard library search helpers.
Each function returns a tuple: (found_index, comparison_count).
"""

from typing import Sequence, Tuple


def linear_search(arr: Sequence[int], target: int) -> Tuple[int, int]:
    """Perform sequential linear search on array for target element.

    Args:
        arr: Sequence of integers to search.
        target: The integer element to find.

    Returns:
        Tuple of (index, comparisons), where index is -1 if not found.
    """
    comparisons = 0
    n = len(arr)

    for i in range(n):
        comparisons += 1
        if arr[i] == target:
            return i, comparisons

    return -1, comparisons


def binary_search(arr: Sequence[int], target: int) -> Tuple[int, int]:
    """Perform iterative binary search on a sorted array for target element.

    Args:
        arr: Sorted sequence of integers to search.
        target: The integer element to find.

    Returns:
        Tuple of (index, comparisons), where index is -1 if not found.
    """
    comparisons = 0
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = low + (high - low) // 2
        comparisons += 1
        mid_val = arr[mid]

        if mid_val == target:
            return mid, comparisons
        elif mid_val < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1, comparisons
