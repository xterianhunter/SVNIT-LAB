## Context

The assignment requires developing, timing, comparing, and analyzing Divide and Conquer solutions alongside brute force and alternative algorithms for Inversion Counting and Fast Exponentiation (CSDS103 Lab 4, SVNIT). The user requested simple, concise code with no unnecessary extras or overhead.

## Goals / Non-Goals

**Goals:**
- Provide a single, self-contained `DAA_Lab4.ipynb` notebook formatted for clear presentation and execution.
- Implement short, readable, Pythonic functions for each algorithm requirement.
- Problem 1:
  - Divide and Conquer inversion counting via Merge Sort ($O(n \log n)$).
  - Brute force inversion counting ($O(n^2)$).
  - Quick Sort and Insertion Sort baseline sorting implementations.
  - Concise timing loops and clean Matplotlib comparative plots.
- Problem 2:
  - Repeated multiplication ($O(n)$).
  - Naive recursive exponentiation with two $n/2$ subcalls ($O(n)$ work, branching recurrence).
  - Divide and Conquer exponentiation with single subproblem reuse ($O(\log n)$).
  - Timing benchmarks and Matplotlib plot.
- Theoretical Analysis:
  - Concise markdown explanations for recurrence relations, space/time complexity, subproblem re-computation effects, iterative vs recursive space, and Divide & Conquer paradigm insights.

**Non-Goals:**
- No complex OOP abstraction or class hierarchies.
- No heavy profiling packages; use standard `time.perf_counter`.
- No extraneous third-party dependencies beyond standard Python libraries and `matplotlib`.

## Decisions

### Decision 1: Direct, Idiomatic Functional Implementations
- **Approach**: Keep all algorithm implementations as standalone, pure functions (e.g., `count_inversions_bf`, `count_inversions_dc`, `power_iterative`, `power_recursive_naive`, `power_dc`).
- **Rationale**: Meets user requirement of keeping everything short, simple, and directly readable for lab evaluation.
- **Alternatives Considered**: Object-oriented benchmarking classes — rejected due to excessive boilerplate.

### Decision 2: Controlled Input Ranges for Benchmarking
- **Approach**: 
  - Problem 1 array sizes: e.g., $N \in [100, 200, 400, 800, 1600, 3200]$ to clearly illustrate the quadratic divergence of $O(n^2)$ vs $O(n \log n)$ while keeping execution within seconds.
  - Problem 2 exponent sizes: evaluate $n \in [10, 20, ..., 1000]$ for iterative and D&C, while capping naive recursion at small $n$ ($n \le 25$) to prevent exponential branching delays and recursion depth errors.
- **Rationale**: Demonstrates clear theoretical growth curves without hanging the notebook kernel.

### Decision 3: Clean Notebook Cell Structure
- **Structure**:
  1. Header & Problem 1 Algorithm Implementations (BF, D&C Merge, Quick Sort, Insertion Sort)
  2. Problem 1 Verification on sample data
  3. Problem 1 Benchmarking & Matplotlib Plot
  4. Problem 1 Complexity Analysis (Markdown)
  5. Problem 2 Algorithm Implementations (Iterative, Naive Recursive, D&C)
  6. Problem 2 Verification
  7. Problem 2 Benchmarking & Matplotlib Plot
  8. Problem 2 Recurrence & Analysis Questions (Markdown)

## Risks / Trade-offs

- **[Risk] Naive recursive exponentiation explosion** → Subproblem duplication in naive recursion causes $O(n)$ recursive calls or branch proliferation. *Mitigation*: Benchmark naive recursion on appropriate input ranges and explain the limitation in analysis.
- **[Risk] Large integer multiplication timing distortion in Python** → Python handles arbitrarily large integers, which can introduce superlinear multiplication time for huge exponents. *Mitigation*: Benchmark with modest base (e.g., $a=2$) or use modular arithmetic / fixed multiplication counts for pure algorithmic time measurement.
