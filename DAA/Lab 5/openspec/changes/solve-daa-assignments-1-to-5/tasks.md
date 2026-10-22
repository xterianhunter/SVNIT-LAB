## 1. Notebook Setup & Timing Utility

- [x] 1.1 Create `daa_assignments_1_to_5.ipynb` structure with clean section headers and verify valid notebook JSON.
- [x] 1.2 Implement high-resolution microsecond timing utility using `time.perf_counter_ns()` and verify correct sub-microsecond reporting on sample runs.

## 2. Assignment 1: 2D Closest Pair of Points

- [x] 2.1 Implement brute-force $O(n^2)$ closest pair algorithm and verify on standard coordinate test cases.
- [x] 2.2 Implement divide-and-conquer $O(n \log n)$ closest pair algorithm and verify that it matches brute-force distance and coordinates.
- [x] 2.3 Benchmark execution times across multiple point set sizes ($n \in [100, 500, 1000, 2000]$) and print empirical vs. theoretical comparison.

## 3. Assignment 2 & 3: Large Dataset, Duplicate Resolution, and Microsecond Timing

- [x] 3.1 Generate a dataset of $1,000,000$ positive random integers and verify array length and positive element constraints.
- [x] 3.2 Implement duplicate count detection and nearest-free-integer round-off resolution, verifying zero duplicates remain in the resolved subset.
- [x] 3.3 Benchmark duplicate removal time in microseconds and document Linux/monotonic timing methods (`clock_gettime`, `perf_counter_ns`).

## 4. Assignment 4: Order Statistics (Heap vs Quicksort Partition)

- [x] 4.1 Implement Priority Queue (Heap) based selection of element at index $i$ and verify against `sorted(arr)[i]`.
- [x] 4.2 Implement Quicksort partition (Quickselect) selection for index $i$ and verify correctness across test arrays.
- [x] 4.3 Benchmark and compare execution times of Priority Queue, Quickselect, and full sort for $i$ near $0$, $n/2$, and $n-1$.

## 5. Assignment 5: Cost of Execution & Asymptotic Loop Analysis

- [x] 5.1 Implement Code 1 ($O(n^2)$) and Code 2 ($O(n)$ with discussion of `j=n/2` vs `j=j//2`), verifying statement counter $x$ against theoretical formulas.
- [x] 5.2 Implement Code 3 ($O(n^3)$) and Code 4 ($O(n \log n)$), verifying step counts and execution timings across varying $n$.
- [x] 5.3 Tabulate and summarize empirical costs compared with asymptotic theoretical complexities.

## 6. Verification & Notebook Execution

- [x] 6.1 Execute the entire notebook `daa_assignments_1_to_5.ipynb` end-to-end to ensure all cells run cleanly without errors and produce concise output.
