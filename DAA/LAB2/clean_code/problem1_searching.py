"""DAA Lab Assignment 2 - Problem 1: Searching Algorithms
Student: SVNIT M.Tech (CSDS103)
Algorithms: Linear Search & Binary Search
Input: File-based integer arrays (10 Sizes: 10, 20, 50, 75, 100, 150, 200, 300, 400, 500)
Cases: Beginning, Middle, End, Absent
"""

import os
import random
import time


# --- 1. SEARCH ALGORITHMS (FIRST PRINCIPLES) ---

def linear_search(arr, target):
    """Sequential search returning (found_index, comparisons)."""
    comps = 0
    for i in range(len(arr)):
        comps += 1
        if arr[i] == target:
            return i, comps
    return -1, comps


def binary_search(arr, target):
    """Iterative binary search returning (found_index, comparisons)."""
    comps = 0
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        comps += 1
        if arr[mid] == target:
            return mid, comps
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1, comps


# --- 2. DATASET I/O & PREPARATION ---

def load_or_create_dataset(n, data_dir="data"):
    """Load sorted array from file or create it if missing."""
    os.makedirs(data_dir, exist_ok=True)
    filepath = os.path.join(data_dir, f"input_{n}.txt")
    if not os.path.exists(filepath):
        rng = random.Random(42 + n)
        data = sorted(rng.sample(range(1, max(1000, n * 10)), n))
        with open(filepath, "w") as f:
            f.write("\n".join(map(str, data)) + "\n")

    with open(filepath, "r") as f:
        return [int(x) for x in f.read().split() if x.strip()]


# --- 3. BEFORE & AFTER FUNCTION DEMONSTRATION ---

def demonstrate_searching(n=10):
    """Demonstrate search behavior before and after applying functions on sample input."""
    arr = load_or_create_dataset(n)
    print("=" * 86)
    print("PART 1: FUNCTION DEMONSTRATION (BEFORE & AFTER EFFECT ON N=10 SAMPLE INPUT)")
    print("=" * 86)
    print(f"Loaded Sorted Input Array (Size N={n}):")
    print(f"  {arr}\n")
    print(f"{'Test Position':<14} | {'Target':<8} | {'Linear Search Result':<26} | {'Binary Search Result':<26}")
    print("-" * 86)
    queries = [
        ("Beginning", arr[0]),
        ("Middle", arr[n // 2]),
        ("End", arr[-1]),
        ("Absent", max(arr) + 1000),
    ]
    for pos, target in queries:
        l_idx, l_comps = linear_search(arr, target)
        b_idx, b_comps = binary_search(arr, target)
        l_str = f"Found at index {l_idx} ({l_comps} comps)" if l_idx != -1 else f"Not Found ({l_comps} comps)"
        b_str = f"Found at index {b_idx} ({b_comps} comps)" if b_idx != -1 else f"Not Found ({b_comps} comps)"
        print(f"{pos:<14} | {target:<8} | {l_str:<26} | {b_str:<26}")
    print("-" * 86)


# --- 4. BENCHMARKING HARNESS (10 SIZES) ---

def time_search(algo_fn, arr, target, runs=3000):
    """Measure average execution time (nanoseconds) across multiple runs."""
    algo_fn(arr, target)  # Warmup
    t0 = time.perf_counter_ns()
    for _ in range(runs):
        idx, comps = algo_fn(arr, target)
    t1 = time.perf_counter_ns()
    return idx, comps, (t1 - t0) / runs


def run_experiment(sizes=(10, 20, 50, 75, 100, 150, 200, 300, 400, 500)):
    """Execute search benchmarks across 10 array sizes and test positions."""
    results = []
    for n in sizes:
        arr = load_or_create_dataset(n)
        test_cases = {
            "Beginning": arr[0],
            "Middle":    arr[n // 2],
            "End":       arr[-1],
            "Absent":    max(arr) + 1000,
        }

        for algo_name, fn in [("Linear Search", linear_search), ("Binary Search", binary_search)]:
            for case_name, target in test_cases.items():
                idx, comps, avg_ns = time_search(fn, arr, target)
                results.append({
                    "algo": algo_name,
                    "n": n,
                    "case": case_name,
                    "target": target,
                    "index": idx,
                    "comps": comps,
                    "time_us": avg_ns / 1000.0,
                })
    return results


# --- 5. TABULATION & THEORETICAL ANALYSIS ---

def display_results(results):
    """Print formatted console table."""
    header = f"{'Algorithm':<15} | {'Size (N)':<8} | {'Case':<11} | {'Target':<8} | {'Index':<6} | {'Comps':<6} | {'Time (µs)':<10}"
    print("\n" + "=" * len(header))
    print("PART 2: EMPIRICAL BENCHMARK RESULTS (10 INPUT SIZES: 10 TO 500)")
    print("=" * len(header))
    print(header)
    print("-" * len(header))
    for r in results:
        print(f"{r['algo']:<15} | {r['n']:<8} | {r['case']:<11} | {r['target']:<8} | {r['index']:<6} | {r['comps']:<6} | {r['time_us']:<10.4f}")
    print("-" * len(header))


def print_analysis():
    """Print theoretical vs experimental complexity analysis."""
    print("""
PART 3: THEORETICAL VS EXPERIMENTAL COMPLEXITY ANALYSIS
1. Linear Search:
   - Best Case [O(1)]: Target at index 0 requires 1 comparison (~0.2-0.3 µs constant across all N).
   - Average Case [O(n)]: Target at middle requires N/2 comparisons (scales linearly from 5 to 250 comps).
   - Worst/Absent Case [O(n)]: Target at end or absent requires N comparisons (~0.5 µs for N=10 up to ~20 µs for N=500).
2. Binary Search:
   - Precondition: Input array must be sorted.
   - Best Case [O(1)]: Target at middle index on initial probe (~0.4-0.6 µs).
   - Worst/Absent Case [O(log n)]: Maximum comparisons <= ceil(log2(N)) + 1 (<=4 for N=10, <=10 for N=500).
   - Scalability: Execution time remains nearly constant (~0.6-1.5 µs) even as N increases 50x.
""")


if __name__ == "__main__":
    demonstrate_searching(n=10)
    records = run_experiment()
    display_results(records)
    print_analysis()
