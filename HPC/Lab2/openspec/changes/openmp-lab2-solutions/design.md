## Context

See proposal.md for background and motivations. The objective is to provide minimal, clean, and direct C implementations for three core OpenMP topics without unnecessary boilerplate or extraneous libraries.

## Goals / Non-Goals

**Goals:**
- Provide short, concise, and standard C implementations (< 60 lines per program).
- Demonstrate clear contrast between unsynchronized concurrent shared-memory updates and synchronization via `#pragma omp critical`.
- Demonstrate coarse-grained decomposition (outer loop parallelization) vs. fine-grained decomposition (inner loop parallelization) in matrix multiplication, measuring elapsed time using `omp_get_wtime()`.
- Provide a clean Makefile for compilation with OpenMP flags.

**Non-Goals:**
- Complex CLI argument parsing or interactive prompts (sensible default constants will be used).
- Complex BLAS/LAPACK optimizations or cache-tiling (the focus is purely on OpenMP loop decomposition semantics).

## Decisions

- **Decision: Separate standalone source files for each topic**
  - *Rationale*: Isolating `race_condition.c`, `critical_section.c`, and `matrix_mult.c` produces compact, readable code tailored for lab submission and direct demonstration.
  - *Alternative considered*: A single monolithic CLI program. Rejected because separate programs are cleaner, simpler to inspect, and align directly with lab exercises.

- **Decision: Race condition setup with shared counter increment**
  - *Rationale*: A loop of $10^6$ iterations with `counter++` executed concurrently across OpenMP threads reliably triggers race conditions due to non-atomic read-modify-write cycles.
  - *Alternative considered*: Random delays or sleep. Rejected as counter increment is deterministic, fast, and simple.

- **Decision: Definition of Coarse vs Fine Decomposition in Matrix Multiplication**
  - *Coarse-Grained*: `#pragma omp parallel for` applied to the outermost loop (`for (int i = 0; i < N; i++)`), dividing blocks of matrix rows among threads. This minimizes thread coordination overhead.
  - *Fine-Grained*: `#pragma omp parallel for` applied to the inner loop (`for (int j = 0; j < N; j++)`) inside the outer loop, repeatedly distributing fine work units across threads and demonstrating thread dispatch/barrier overhead.
  - *Rationale*: Clearly reflects the standard textbook HPC definition of coarse vs fine decomposition in nested loops.

## Risks / Trade-offs

- [Very small loop counts may not show race condition] → Use sufficient iteration count ($10^6$) to ensure thread preemption and concurrent writes consistently reproduce the race condition.
- [Excessive matrix dimensions leading to long benchmark execution] → Keep $N$ around 300 to 500 so execution completes within a few seconds while still demonstrating timing differences.
