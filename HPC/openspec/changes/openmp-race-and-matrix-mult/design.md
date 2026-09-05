## Context

Shared-memory parallel programming with OpenMP on modern multi-core architectures presents fundamental trade-offs between synchronization overhead, concurrency correctness, and decomposition granularity. This design specifies the architecture and technical approach for demonstrating data race hazards, critical section synchronization, and comparing coarse-grained versus fine-grained decomposition in parallel matrix-matrix multiplication on large input matrices.

## Goals / Non-Goals

**Goals:**
- Provide clear, self-contained C programs demonstrating race conditions and mutual exclusion via `#pragma omp critical`.
- Implement both coarse-grained (row-level chunking) and fine-grained (element-level / fine dynamic scheduling) data decomposition algorithms for dense matrix-matrix multiplication.
- Support configurable matrix sizes ($N \ge 1000$) and thread counts ($1, 2, 4, 8, \dots$) to benchmark execution time, speedup ($S = T_1 / T_p$), and efficiency ($E = S / p$).
- Provide automated build configuration (`Makefile`) and benchmarking scripts to generate comparative execution tables.

**Non-Goals:**
- Distributed memory parallelism (MPI) or GPU offloading (CUDA / OpenMP target offload).
- Hardware-specific micro-kernel SIMD intrinsics (AVX-512 assembly) beyond standard compiler vectorization.
- Strassen's or sub-cubic matrix multiplication algorithms (standard $O(N^3)$ dense multiplication is used to compare decomposition granularity).

## Decisions

### 1. Language and Toolchain Selection
- **Decision**: Implement in standard C (C99/C11) with GCC/Clang and OpenMP flags (`-fopenmp -O3`).
- **Rationale**: C provides low-level control over memory layouts, deterministic cache interaction, minimal runtime abstraction overhead, and portable OpenMP support across Linux HPC environments.
- **Alternative Considered**: C++ with `std::vector`; rejected to avoid potential heap abstraction overhead and ensure clean pointer-based contiguous 1D memory buffers.

### 2. Project Directory Structure
```
HPC/
├── Makefile
├── bin/                              # Compiled executables
├── src/
│   ├── race_condition.c             # Unsynchronized shared resource update
│   ├── critical_section.c           # Synchronized update using omp critical
│   ├── matrix_mult.c                # Matrix multiplication implementations & benchmarking
│   └── common.h                     # Matrix utilities, timer helpers, and verification
└── scripts/
    └── run_benchmarks.sh            # Automated multi-thread / multi-size benchmark runner
```

### 3. Concurrency Control Design
- **Race Condition Implementation**:
  - Multiple threads concurrently execute $M = 10,000,000$ iterations incrementing a global shared integer variable `counter++`.
  - Because `counter++` compiles into non-atomic read-modify-write instructions (load, add, store), thread interleaving causes lost updates, illustrating the race condition.
- **Critical Section Implementation**:
  - Encapsulates the critical section using `#pragma omp critical (counter_lock)`.
  - Ensures mutual exclusion so that each read-modify-write completes atomically.
  - Final value is verified against expected $T \times M$.

### 4. Matrix Multiplication Decomposition Strategy
- **Memory Representation**:
  - Matrices $A, B, C \in \mathbb{R}^{N \times N}$ allocated as contiguous 1D arrays of `double` (size $N \times N \times \text{sizeof(double)}$) to ensure cache locality and prevent memory fragmentation.
- **Coarse-Grained Decomposition (Row-Level)**:
  - Parallelize the outermost loop $i \in [0, N-1]$ using `#pragma omp parallel for schedule(static)`.
  - Thread $t$ computes an entire slice of $N/T$ rows in output matrix $C$.
  - Thread creation/join happens once; zero inter-thread communication or synchronization during computation.
- **Fine-Grained Decomposition (Element-Level / Inner Loop)**:
  - Parallelize across individual matrix elements or inner loops using `#pragma omp parallel for collapse(2) schedule(dynamic, 1)` or nested fine-grained tasking.
  - Generates $N^2$ finely scheduled work units, exposing scheduling overhead, thread communication latency, and cache misses.
- **Performance Metrics**:
  - Wall-clock time measured via `omp_get_wtime()`.
  - Floating point operations: $2 N^3$ FLOPs.
  - Throughput: GFLOPS $= \frac{2 N^3}{t \times 10^9}$.
  - Speedup and parallel efficiency recorded across thread counts $T \in \{1, 2, 4, 8, \dots\}$.

## Risks / Trade-offs

- **[Risk] High Overhead in Fine-Grained Decomposition causing excessive runtime**:
  - *Mitigation*: Ensure benchmark driver allows configurable matrix sizes and thread chunk sizes so fine-grained benchmarking remains responsive.
- **[Risk] Compiler Optimization Masking Race Conditions**:
  - *Mitigation*: Declare the shared counter with `volatile` keyword or pass optimization flags (`-O2` / `-O3` with proper memory reads) to prevent compiler from optimizing the loop into a single register addition.
- **[Risk] Memory allocation failure for large matrices ($N \ge 2000$)**:
  - *Mitigation*: For $N=2000$, three double matrices require $\approx 3 \times 2000 \times 2000 \times 8 \text{ bytes} \approx 96 \text{ MB}$, well within standard host RAM limits. Check `malloc` return pointers.
