## Context

See `proposal.md` for problem background. Problem 3 requires implementing Matrix Addition, Matrix Multiplication, and Matrix Transpose on square matrices ($10 \times 10, 50 \times 50, 100 \times 100, 200 \times 200, 500 \times 500$) generated programmatically and analyzing their time complexities.

## Goals / Non-Goals

**Goals:**
- Implement pure Python Matrix Addition ($\mathcal{O}(n^2)$), Matrix Transposition ($\mathcal{O}(n^2)$), and Matrix Multiplication ($\mathcal{O}(n^3)$) without external libraries (no NumPy).
- Programmatically generate $N \times N$ matrices with reproducible random numbers.
- Measure execution times using `time.perf_counter_ns()` with adaptive iteration counts suited for $\mathcal{O}(n^3)$ operations.
- Tabulate results and provide detailed theoretical complexity vs empirical scaling analysis.
- Provide a clean, short, single-file script `problem3_matrix.py`.

**Non-Goals:**
- Strassen's matrix multiplication or BLAS-optimized multithreaded matrix routines (focus is on standard algorithms from Problem 3).

## Decisions

### Decision 1: 2D Python List Representation
- **Choice**: Represent matrices as lists of lists: `A[i][j]`.
- **Rationale**: Keeps the implementation pure, clean, readable, and 100% compliant with standard Python academic coursework.

### Decision 2: Adaptive Benchmarking Iterations
- **Choice**: Matrix multiplication has $\mathcal{O}(n^3)$ complexity. For $N=500$, $500^3 = 125,000,000$ operations. Running $10,000$ iterations would take hours. Therefore, use adaptive iteration counts:
  - $N=10$: 500 runs
  - $N=50$: 50 runs
  - $N=100$: 10 runs
  - $N=200$: 3 runs
  - $N=500$: 1 run
- **Rationale**: Delivers rapid, accurate timing without hanging the execution.

## Risks / Trade-offs

- **[Risk]** Slow execution on $500 \times 500$ matrix multiplication in interpreted Python → **Mitigation**: Pre-allocate result matrices and use optimized inner loop indexing with adaptive run counts.
