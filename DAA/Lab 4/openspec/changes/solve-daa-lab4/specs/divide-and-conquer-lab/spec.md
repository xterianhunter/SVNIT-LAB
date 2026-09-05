## Purpose

Provides a clean, verified Jupyter Notebook implementing Divide and Conquer solutions and empirical benchmarking for Inversion Counting and Fast Exponentiation as specified in DAA Lab Assignment 4.

## ADDED Requirements

### Requirement: Counting Inversions using Divide and Conquer
The system SHALL provide a Divide and Conquer function based on merge sort that simultaneously sorts an input array and counts the total number of inversions $(i, j)$ where $i < j$ and $A[i] > A[j]$.

#### Scenario: Correct inversion count and sorted output
- **WHEN** the input array $[8, 4, 2, 1]$ is passed to the Divide and Conquer function
- **THEN** the function returns an inversion count of 6 and sorts the array to $[1, 2, 4, 8]$

#### Scenario: Array with zero inversions
- **WHEN** an already sorted array $[1, 2, 3, 4, 5]$ is provided
- **THEN** the function returns an inversion count of 0

### Requirement: Counting Inversions using Brute Force
The system SHALL provide a straightforward brute-force function that examines all pairs of elements $(i, j)$ with $i < j$ to count inversions.

#### Scenario: Accurate count matching Divide and Conquer
- **WHEN** any test array is passed to both the brute-force and Divide and Conquer functions
- **THEN** both functions return identical inversion counts

### Requirement: Comparison with Baseline Sorting Algorithms
The system SHALL provide implementations of at least two baseline sorting algorithms (Quick Sort and Insertion Sort) to compare sorting execution times against the Divide and Conquer merge-sort approach.

#### Scenario: Successful execution of baseline sorting
- **WHEN** generated random arrays are sorted using Quick Sort, Insertion Sort, and the Divide and Conquer sort
- **THEN** each algorithm produces a correctly sorted array and records valid execution time

### Requirement: Fast Exponentiation via Repeated Multiplication
The system SHALL implement an iterative function computing $a^n$ by performing $n$ repeated multiplications.

#### Scenario: Accurate exponentiation
- **WHEN** $a = 2$ and $n = 10$ are passed
- **THEN** the function returns $1024$

### Requirement: Fast Exponentiation via Naive Recursion
The system SHALL implement a recursive exponentiation function following the exact piecewise relation:
$$a^n = \begin{cases} 1 & n = 0 \\ a^{n/2} \times a^{n/2} & n \text{ is even} \\ a \times a^{n-1} & n \text{ is odd} \end{cases}$$
evaluating both branches separately when $n$ is even.

#### Scenario: Accurate computation with branching
- **WHEN** computing $a^n$ for small to moderate values of $n$
- **THEN** the returned value matches $a^n$

### Requirement: Fast Exponentiation via Divide and Conquer
The system SHALL implement an optimal Divide and Conquer exponentiation function that computes $a^{\lfloor n/2 \rfloor}$ exactly once and reuses the result.

#### Scenario: Efficient computation of large exponents
- **WHEN** computing $a^n$ for large values of $n$
- **THEN** the function runs in logarithmic steps $O(\log n)$ and returns the exact value

### Requirement: Empirical Benchmarking and Performance Plots
The system SHALL measure execution times across multiple input sizes for both Problem 1 and Problem 2 and display performance graphs comparing input sizes versus execution times.

#### Scenario: Generation of performance graphs
- **WHEN** the notebook cells for benchmarking are executed
- **THEN** distinct curves for each algorithm are plotted using matplotlib illustrating their asymptotic behavior

### Requirement: Theoretical and Paradigm Analysis
The system SHALL include clear markdown explanations addressing recurrence derivations, theoretical time/space complexities, the impact of repeated subproblems, iterative versus recursive implementations, and the Divide and Conquer paradigm.

#### Scenario: Complete Lab 4 analysis coverage
- **WHEN** the notebook is reviewed
- **THEN** all analysis questions posed in `DAA_Lab4.pdf` are explicitly answered in designated markdown sections
