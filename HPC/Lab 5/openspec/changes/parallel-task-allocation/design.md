## Context

See [proposal.md](file:///home/xterianhunter/LABS/HPC/Lab%205/openspec/changes/parallel-task-allocation/proposal.md) for motivation and problem formulation.
In distributed task allocation, $M$ tasks are assigned to $P$ processors ($P \ll M$).
The cost function consists of:
1. **Execution cost**: $\sum_{i=0}^{M-1} X[i][assignment[i]]$
2. **Inter-task communication cost**: $\sum_{i=0}^{M-1} \sum_{j=i+1}^{M-1} C[i][j] \cdot [assignment[i] \neq assignment[j]]$

Evaluating this cost for a single candidate allocation is $O(M^2)$ due to the communication matrix pairwise checks. With large $M$ (e.g., $M = 100 \dots 500$), evaluating thousands of candidate solutions across hundreds of iterations is computationally intensive, creating an ideal workload for OpenMP thread-level parallelism.

## Goals / Non-Goals

**Goals:**
- Provide clean, simple, standalone C code without unnecessary dependencies.
- Implement cost evaluation matching Stone's model and the image reference (including exact verification for the 6-task, 2-processor sample problem).
- Implement both Sequential and OpenMP-parallel versions of Genetic Algorithm (GA).
- Implement both Sequential and OpenMP-parallel versions of Particle Swarm Optimization (PSO).
- Benchmark both algorithms at large scale ($M \gg P$), measuring execution time (via `omp_get_wtime()`), speedup ($S = T_{seq} / T_{par}$), and solution quality.

**Non-Goals:**
- Complex GUI, MPI multi-node clusters, or external optimization frameworks.
- Dynamic task migration during runtime (this is static offline allocation).

## Decisions

### 1. Unified Clean C Implementation
- **Decision**: Keep the code simple, structured, and easy to read and compile with `gcc -fopenmp -O2`.
- **Rationale**: The user specifically requested: *"give simple c code don't do anything that's unncessary avoid anything else simple give implementation code"*.
- **Alternative considered**: Multiple header files and complex build systems (Makefile, CMake). Rejected to keep execution direct and straightforward for lab evaluation.

### 2. Parallelization Strategy in OpenMP
- **Genetic Algorithm (GA)**:
  - Parallelize the fitness evaluation loop across the population using `#pragma omp parallel for`.
  - Parallelize offspring reproduction / crossover loops where candidate children are generated concurrently.
  - Thread-safe random number generation using thread-private seeds (`rand_r` or Lehmer/LCG per thread) to prevent thread contention.
- **Particle Swarm Optimization (PSO)**:
  - Parallelize the swarm particle evaluation and position/velocity update loop across particles using `#pragma omp parallel for`.
  - Maintain thread safety when updating the swarm's global best ($gbest$) using critical sections or reduction.

### 3. Discrete PSO Formulation for Task Allocation
- **Decision**: Represent each particle's position as an integer array of size $M$ where $x_{i} \in \{0, \dots, P-1\}$. Velocity is modeled as continuous influence values $v_{i} \in [-V_{max}, V_{max}]$ updated with inertia $w$, cognitive component $c_1 r_1 (pbest_i - x_i)$, and social component $c_2 r_2 (gbest_i - x_i)$, or probabilistic discrete assignment transitions.
- **Rationale**: Simple to implement, computationally lightweight, and ensures particles explore valid processor assignments $[0, P-1]$.

### 4. Verification & Benchmarking
- **Decision**: The program will run two phases:
  1. **Verification Phase**: Uses the exact $6 \times 2$ matrix from the prompt's diagram. Verifies that the Serial Assignment achieves cost 58 and Optimal Assignment achieves cost 38.
  2. **Large Scale Benchmark Phase**: Configurable $M$ tasks (e.g. $M = 200$) and $P$ nodes (e.g. $P = 8$). Runs Sequential GA, Parallel GA, Sequential PSO, and Parallel PSO, outputting timing, speedup, and solution quality.

## Risks / Trade-offs

- **[Risk] Thread contention on standard `rand()`** $\rightarrow$ **Mitigation**: Standard C `rand()` uses a global lock in glibc, killing OpenMP scaling. We will use a fast linear congruential generator (LCG) or `rand_r()` with per-thread state so threads never contend on RNG.
- **[Risk] Premature convergence in metaheuristics** $\rightarrow$ **Mitigation**: Use elitism and balanced mutation rates in GA; appropriate inertia weight damping in PSO.
