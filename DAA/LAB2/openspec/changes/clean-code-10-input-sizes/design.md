## Context

The user requested that the newly created clean scripts in `clean_code/` benchmark and display experimental results for at least 10 distinct input sizes across Searching, Sorting, and Matrix operations.

## Goals / Non-Goals

**Goals:**
- Update `clean_code/problem1_searching.py` to evaluate 10 array sizes: `(10, 20, 50, 75, 100, 150, 200, 300, 400, 500)`.
- Update `clean_code/problem2_sorting.py` to evaluate 10 array sizes: `(20, 40, 60, 80, 100, 150, 200, 300, 400, 500)`.
- Update `clean_code/problem3_matrix.py` to evaluate 10 matrix dimensions: `(10, 20, 30, 40, 50, 75, 100, 150, 200, 300)`.
- Maintain fast execution through adaptive run sizing so all benchmarks complete within a few seconds.

**Non-Goals:**
- Modifying algorithm implementations or adding heavy libraries.

## Decisions

1. **Selected Input Size Sequences**:
   - Searching: `(10, 20, 50, 75, 100, 150, 200, 300, 400, 500)` — provides granular data points up to $N=500$.
   - Sorting: `(20, 40, 60, 80, 100, 150, 200, 300, 400, 500)` — smoothly maps quadratic $\mathcal{O}(n^2)$ curve growth.
   - Matrix Operations: `(10, 20, 30, 40, 50, 75, 100, 150, 200, 300)` — maps cubic $\mathcal{O}(n^3)$ growth up to $300\times300$ while keeping execution rapid.

2. **Adaptive Benchmark Iterations**:
   - Scale iteration runs inversely with problem size so large inputs ($N=500$ or $300\times300$) do not cause latency delays.

## Risks / Trade-offs

- **[Console table length]** → Tables with 10 sizes will be longer (30 to 90 rows). Mitigation: The formatted table output is clean, organized, and easily pageable.
