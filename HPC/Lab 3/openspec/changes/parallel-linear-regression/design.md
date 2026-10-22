## Context

The problem requires a parallel version of linear regression using OpenMP in C. The data space is 3-dimensional (two feature dimensions $x_1, x_2$ and one label dimension $y$). Training is performed via batch gradient descent. Parallelization is applied directly to the sample-accumulation loop of gradient descent, and runtime is compared with a sequential baseline.

See [proposal.md](file:///home/xterianhunter/LABS/HPC/Lab%203/openspec/changes/parallel-linear-regression/proposal.md) and [specs/linear-regression-openmp/spec.md](file:///home/xterianhunter/LABS/HPC/Lab%203/openspec/changes/parallel-linear-regression/specs/linear-regression-openmp/spec.md).

## Goals / Non-Goals

**Goals:**
- Implement sequential and OpenMP parallel gradient descent for 2-feature linear regression ($y = w_1 x_1 + w_2 x_2 + b$).
- Measure and print wall-clock time using `omp_get_wtime()`.
- Use a large dataset ($N = 10,000,000$ points) to overcome thread creation/synchronization overhead and obtain realistic speedup numbers.
- Deliver concise, clear C code with no unnecessary boilerplate or external dependencies.

**Non-Goals:**
- Complex optimization algorithms (e.g., Adam, RMSprop, or mini-batching with shuffling) not requested by the prompt.
- Disk I/O or file parsing (synthetic data generation in memory is faster and avoids disk bottlenecks).

## Decisions

### Decision: Memory Layout (Structure of Arrays vs Array of Structures)
- **Choice**: Separate flat arrays for $x_1$, $x_2$, and $y$ (Structure of Arrays - SoA).
- **Rationale**: Continuous memory access for vectorization and cache friendliness during parallel reduction loops.
- **Alternative**: Array of structures (AoS) with `struct { double x1, x2, y; }`. SoA was chosen because sequential reads of $x_1, x_2, y$ stream efficiently into L1/L2 caches without stride overhead.

### Decision: OpenMP Reduction Directive
- **Choice**: `#pragma omp parallel for reduction(+:dw1, dw2, db) schedule(static)`
- **Rationale**: The workload per sample is uniform. Static chunking evenly splits the iterations without runtime dynamic scheduling overhead, while `reduction(+:...)` eliminates critical sections or mutex locks.
- **Alternative**: Manual thread-local accumulator arrays. OpenMP's built-in reduction clause is cleaner, simpler, and equally optimal.

### Decision: Granularity & Epoch Count
- **Choice**: $N = 10,000,000$ data points and $20$ to $50$ epochs.
- **Rationale**: Batch gradient descent with $10^7$ points per epoch requires $3 \times 10^7$ multiply-adds per epoch, giving measurable seconds-long runtimes where OpenMP threading speedup is clearly observable.

## Risks / Trade-offs

- **[Memory footprint with large N]** → $10^7$ samples using `double` for $x_1, x_2, y$ requires $\approx 240\text{ MB}$ of RAM, well within system limits.
- **[Floating point non-associativity]** → Parallel reduction sums terms in different orders, leading to tiny rounding differences in weights ($< 10^{-10}$) compared to sequential execution; this is normal and mathematically acceptable for gradient descent.
