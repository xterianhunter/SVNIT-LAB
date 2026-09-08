## Purpose

Provides a clean, concise, self-contained Jupyter Notebook solving CS103 Lab Assignments 1 through 5 with minimal code, strictly adhering to required algorithmic techniques, timing benchmarks, and complexity analyses.

## ADDED Requirements

### Requirement: Closest Pair of Points in 2D Plane (Assignment 1)
The notebook SHALL implement both the brute-force $O(n^2)$ and divide-and-conquer $O(n \log n)$ algorithms to find the closest pair of 2D points, generate test sets of various sizes, measure execution times, and compare their empirical performance against theoretical expectations.

#### Scenario: Valid distance computation
- **WHEN** a list of 2D points is provided to both brute-force and divide-and-conquer implementations
- **THEN** both methods MUST return the same minimum Euclidean distance and corresponding closest pair of points.

#### Scenario: Empirical timing comparison
- **WHEN** synthetic point datasets of increasing size $n$ are evaluated
- **THEN** execution times for both algorithms MUST be recorded and compared, demonstrating $O(n \log n)$ scalability overtaking $O(n^2)$.

### Requirement: Large Dataset Generation and Duplicate Resolution (Assignment 2)
The notebook SHALL generate a dataset of at least 1,000,000 positive integers, count the total number of duplicate values, resolve duplicates by rounding them off to the nearest free integer, measure duplicate removal time, and document high-resolution timing approaches.

#### Scenario: 1M positive integers dataset generation
- **WHEN** the random generation routine is invoked for $N = 1,000,000$
- **THEN** an array of $1,000,000$ strictly positive integers MUST be produced.

#### Scenario: Duplicate counting and nearest-free-integer resolution
- **WHEN** duplicate values exist in the generated dataset
- **THEN** the total count of duplicate elements MUST be reported, and each duplicate MUST be reassigned to the closest unoccupied integer value so that all values become unique.

### Requirement: Microsecond-Precision Timing (Assignment 3)
The timing framework SHALL measure execution durations with sub-microsecond timer resolution and output timing values formatted in microseconds ($\mu\text{s}$), explaining the OS/Python monotonic counter mechanism.

#### Scenario: Sub-microsecond timing output
- **WHEN** an algorithm execution is timed
- **THEN** elapsed wall-clock time MUST be reported in microseconds with sub-microsecond underlying resolution (e.g., using monotonic high-resolution counters).

### Requirement: Order Statistic Selection via Heap and Quicksort Partition (Assignment 4)
The notebook SHALL solve the problem of finding the element at index $i$ in sorted order using both a Priority Queue (Heap) method and Quicksort partition (Quickselect), comparing their theoretical and empirical time complexities against standard full sorting.

#### Scenario: Finding element at index i
- **WHEN** an unsorted array and valid target index $i$ are supplied
- **THEN** both the Priority Queue algorithm and Quicksort partition (Quickselect) algorithm MUST return the exact element that would appear at index $i$ in the sorted array.

#### Scenario: Performance comparison across indices
- **WHEN** target index $i$ varies from near $0$ to near $n-1$
- **THEN** empirical execution times for Priority Queue, Quickselect, and sorting MUST be measured and compared.

### Requirement: Empirical and Asymptotic Analysis of Iterative Constructs (Assignment 5)
The notebook SHALL implement and execute the four specified code loop constructs for varying input sizes $n$, measure operation counts / execution times, and compare empirical scaling with asymptotic theoretical bounds ($O(n^2)$, $O(n)$, $O(n^3)$, $O(n \log n)$).

#### Scenario: Loop execution and step counting
- **WHEN** Code 1, Code 2, Code 3, and Code 4 are executed for multiple values of $n$
- **THEN** the inner statement execution count $x$ and execution times MUST match the predicted theoretical growth rates.

### Requirement: Concise and Minimalist Notebook Design
The solution SHALL be contained within a single `.ipynb` notebook containing only essential, readable code without extraneous dependencies or redundant boilerplate.

#### Scenario: Self-contained execution
- **WHEN** the notebook is executed from top to bottom
- **THEN** all code cells MUST run cleanly without errors using standard Python libraries and produce concise outputs for all five assignments.
