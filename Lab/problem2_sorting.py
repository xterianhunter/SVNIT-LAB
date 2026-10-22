import random
import time


# --- 1. SORTING ALGORITHMS (FIRST PRINCIPLES) ---

def bubble_sort(arr):
    # """Bubble sort with early-termination optimization."""
    a = arr.copy()
    n = len(a)
    comps = 0
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            comps += 1
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:
            break
    return a, comps


def selection_sort(arr):
    # """Selection sort: repeatedly finds minimum element."""
    a = arr.copy()
    n = len(a)
    comps = 0
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            comps += 1
            if a[j] < a[min_idx]:
                min_idx = j
        if min_idx != i:
            a[i], a[min_idx] = a[min_idx], a[i]
    return a, comps


def insertion_sort(arr):
    # """Insertion sort: inserts elements into sorted sub-array."""
    a = arr.copy()
    n = len(a)
    comps = 0
    for i in range(1, n):
        key = a[i]
        j = i - 1
        while j >= 0:
            comps += 1
            if a[j] > key:
                a[j + 1] = a[j]
                j -= 1
            else:
                break
        a[j + 1] = key
    return a, comps


# --- 2. DATASET GENERATION ---

def generate_data(n, input_type, seed=42):
    # """Generate array of size n for given input distribution."""
    rng = random.Random(seed + n)
    if input_type == "Random":
        return rng.sample(range(1, max(1000, n * 10)), n)
    elif input_type == "Sorted":
        return list(range(1, n + 1))
    elif input_type == "Reverse":
        return list(range(n, 0, -1))
    raise ValueError(f"Unknown input type: {input_type}")


# --- 3. BEFORE & AFTER FUNCTION DEMONSTRATION ---

def demonstrate_sorting(n=10):
    # """Demonstrate array state Before and After sorting on sample inputs across distributions."""
    print("=" * 86)
    print("PART 1: FUNCTION DEMONSTRATION (BEFORE & AFTER EFFECT ON N=10 SAMPLE INPUTS)")
    print("=" * 86)
    for input_type in ["Random", "Sorted", "Reverse"]:
        arr = generate_data(n, input_type, seed=42)
        print(f"\n--- Input Distribution: {input_type.upper()} (N={n}) ---")
        print(f"  BEFORE SORTING: {arr}")
        for algo_name, fn in [("Bubble Sort", bubble_sort), ("Selection Sort", selection_sort), ("Insertion Sort", insertion_sort)]:
            sorted_arr, comps = fn(arr)
            print(f"  AFTER {algo_name.upper():<14}: {sorted_arr} (Comparisons: {comps})")
    print("\n" + "-" * 86)


# --- 4. BENCHMARKING HARNESS (10 SIZES) ---

def time_sort(algo_fn, arr, runs=20):
    # """Measure average execution time (nanoseconds) across multiple runs."""
    sorted_arr, comps = algo_fn(arr)
    assert sorted_arr == sorted(arr), "Algorithm failed correctness check!"

    t0 = time.perf_counter_ns()
    for _ in range(runs):
        algo_fn(arr)
    t1 = time.perf_counter_ns()
    return comps, (t1 - t0) / runs


def run_experiment(sizes=(20, 40, 60, 80, 100, 150, 200, 300, 400, 500)):
    # """Execute sorting benchmarks across algorithms, 10 sizes, and distributions."""
    algorithms = [
        ("Bubble Sort", bubble_sort),
        ("Selection Sort", selection_sort),
        ("Insertion Sort", insertion_sort),
    ]
    input_types = ["Random", "Sorted", "Reverse"]
    results = []

    for n in sizes:
        runs = 30 if n <= 100 else (15 if n <= 200 else 5)
        for input_type in input_types:
            arr = generate_data(n, input_type)
            for algo_name, fn in algorithms:
                comps, avg_ns = time_sort(fn, arr, runs=runs)
                results.append({
                    "algo": algo_name,
                    "n": n,
                    "type": input_type,
                    "comps": comps,
                    "time_us": avg_ns / 1000.0,
                    "time_ms": avg_ns / 1_000_000.0,
                })
    return results


# --- 5. TABULATION & THEORETICAL ANALYSIS ---

def display_results(results):
    # """Print formatted console table."""
    header = f"{'Algorithm':<16} | {'Size (N)':<8} | {'Input Type':<12} | {'Comparisons':<12} | {'Time (µs)':<12} | {'Time (ms)':<10}"
    print("\n" + "=" * len(header))
    print("PART 2: EMPIRICAL BENCHMARK RESULTS (10 INPUT SIZES: 20 TO 500)")
    print("=" * len(header))
    print(header)
    print("-" * len(header))
    for r in results:
        print(f"{r['algo']:<16} | {r['n']:<8} | {r['type']:<12} | {r['comps']:<12} | {r['time_us']:<12.2f} | {r['time_ms']:<10.4f}")
    print("-" * len(header))


# def print_analysis():
#     # """Print theoretical vs experimental complexity analysis."""
#     print("""
# PART 3: THEORETICAL VS EXPERIMENTAL COMPLEXITY ANALYSIS
# 1. Bubble Sort (Early Exit):
#    - Best Case (Already Sorted): O(n) -> exactly n - 1 comparisons, 0 swaps (~2-4 µs across all N).
#    - Worst Case (Reverse Sorted): O(n^2) -> n(n-1)/2 comparisons, max swaps (~0.04 ms for N=20 up to ~22 ms for N=500).
#    - Average Case (Random): O(n^2) quadratic scaling.
# 2. Selection Sort:
#    - Best / Average / Worst Case: Theta(n^2) -> always executes exactly n(n-1)/2 comparisons across all inputs.
#    - Swap Efficiency: At most n - 1 swaps across all input permutations.
# 3. Insertion Sort:
#    - Best Case (Already Sorted): O(n) -> exactly n - 1 comparisons, 0 shifts (< 1 µs to ~0.07 ms).
#    - Worst Case (Reverse Sorted): O(n^2) -> n(n-1)/2 comparisons and maximum element shifts.
#    - Average Case (Random): O(n^2), typically 2-3x faster than Bubble Sort due to low constant factors.
# """)


if __name__ == "__main__":
    demonstrate_sorting(n=10)
    records = run_experiment()
    display_results(records)
    # print_analysis()
