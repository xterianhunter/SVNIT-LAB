## Context

Linear regression with two independent variables ($X_1, X_2$) and one dependent variable ($Y$) constitutes a 3-dimensional data space ($x_{i,1}, x_{i,2}, y_i$). Training the model $\hat{y} = w_0 + w_1 x_1 + w_2 x_2$ via Batch Gradient Descent requires evaluating error residuals and aggregating partial derivatives across all $N$ training samples per epoch:

$$\frac{\partial J}{\partial w_0} = \frac{1}{N} \sum_{i=1}^N (\hat{y}_i - y_i)$$
$$\frac{\partial J}{\partial w_1} = \frac{1}{N} \sum_{i=1}^N (\hat{y}_i - y_i) x_{i,1}$$
$$\frac{\partial J}{\partial w_2} = \frac{1}{N} \sum_{i=1}^N (\hat{y}_i - y_i) x_{i,2}$$

For large datasets ($N \ge 10^6$), gradient computation is heavily memory- and compute-bound, making it ideal for shared-memory OpenMP parallel reduction.

## Goals / Non-Goals

**Goals:**
- Implement both sequential and OpenMP-parallelized batch gradient descent in C.
- Utilize OpenMP reduction clauses (`#pragma omp parallel for reduction(+:...) schedule(static)`) to parallelize the gradient updates across sample iterations.
- Benchmark and compare running time, speedup ($S = T_{\text{seq}} / T_{\text{par}}$), and efficiency across thread counts (e.g., 1, 2, 4, 8 threads).
- Keep all implementation files minimal, concise, and self-contained inside the `Lab2/` directory.

**Non-Goals:**
- External ML libraries or complex dependencies (use pure C with OpenMP and standard math library).
- Mini-batch or stochastic gradient descent with fine-grained locks (Batch GD provides clean data parallelism with minimal synchronization).

## Decisions

### Decision 1: Contiguous Structure-of-Arrays (SoA) Data Layout
- **Choice**: Store features and labels in separate contiguous `double` arrays (`x1`, `x2`, `y`) allocated dynamically with `malloc`.
- **Rationale**: Contiguous 1D buffers maximize L1/L2 cache locality, enable compiler auto-vectorization (SIMD), and prevent false sharing across OpenMP threads.
- **Alternatives Considered**: Array-of-Structures (`struct Point { double x1, x2, y; }`), which introduces strided memory access during feature-specific multiplications.

### Decision 2: OpenMP Parallel Reduction with Static Scheduling
- **Choice**: Parallelize the outer sample loop per epoch using `#pragma omp parallel for reduction(+:dw0, dw1, dw2) schedule(static)`.
- **Rationale**: The computation per sample is homogeneous ($O(1)$ arithmetic operations). Static scheduling divides the $N$ samples into contiguous equal chunks with zero runtime scheduling overhead. The reduction clause accumulates thread-private partial sums and combines them at the loop boundary without mutual exclusion locks.
- **Alternatives Considered**: OpenMP critical sections inside the loop (severe lock contention that destroys parallelism) or manual chunk indexing (more complex and error-prone).

### Decision 3: Granularity and Iteration Synchronization
- **Choice**: Parallelize at the sample loop level inside each epoch; update shared weights $w_0, w_1, w_2$ sequentially at the end of each epoch after thread reduction completes.
- **Rationale**: Synchronizing once per epoch after processing $N$ samples provides coarse-grained parallelism with minimal OpenMP fork-join and barrier overhead.

### Decision 4: File and Build Structure in `Lab2/`
- **Choice**:
  - `Lab2/linear_regression.c`: Complete, standalone C implementation with synthetic 3D data generation, sequential solver, parallel OpenMP solver, and automated performance comparison benchmark.
  - `Lab2/Makefile`: Simple build target compiling with `gcc -fopenmp -O3 -lm`.
- **Rationale**: Adheres to the requirement of keeping everything short, simple, and self-contained within `Lab2/`.

## Risks / Trade-offs

- **[Memory Bandwidth Saturation]** → Evaluating simple dot-products over large memory arrays can saturate memory bandwidth at high thread counts.
  - *Mitigation*: Ensure $O(1)$ compute instructions are streamlined, using compiler optimization `-O3` and sequential contiguous traversal.
- **[Floating-point Non-Associativity]** → Parallel reduction sums terms in different orders compared to sequential addition.
  - *Mitigation*: Use 64-bit `double` precision; minor numerical differences ($< 10^{-6}$) are far below gradient descent convergence thresholds.
