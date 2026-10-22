## 1. Cost Model and Problem Formulation

- [x] 1.1 Implement the task allocation cost calculation function ($\text{Total Cost} = \sum \text{Execution Costs} + \sum \text{Cross-Processor Communication Costs}$) and verify against the sample $6 \times 2$ problem topology to confirm Serial Cost = 58 and Optimal Cost = 38.
- [x] 1.2 Implement dynamic problem instance generation for large $M$ tasks and $P$ processors ($P \ll M$) initializing execution matrix $X[M][P]$ and sparse communication matrix $C[M][M]$.

## 2. Genetic Algorithm Implementation

- [x] 2.1 Implement Sequential Genetic Algorithm (GA) with integer chromosome representation, population fitness evaluation, tournament selection, crossover, mutation, and elitism.
- [x] 2.2 Implement Parallel Genetic Algorithm using OpenMP (`#pragma omp parallel for` on population fitness evaluations with thread-safe pseudo-random number generation) and verify speedup over the sequential baseline.

## 3. Particle Swarm Optimization Implementation

- [x] 3.1 Implement Sequential Particle Swarm Optimization (PSO) for discrete task allocation with personal best ($pbest$) and global best ($gbest$) tracking and discrete velocity/position updates.
- [x] 3.2 Implement Parallel Particle Swarm Optimization using OpenMP (`#pragma omp parallel for` across swarm particles with thread-safe RNG) and verify speedup over the sequential baseline.

## 4. Benchmarking and Performance Evaluation

- [x] 4.1 Implement comparative driver in simple, self-contained C code that executes Sequential GA, Parallel GA, Sequential PSO, and Parallel PSO on identical problem instances.
- [x] 4.2 Compile with `gcc -fopenmp -O2`, run across different thread counts, and verify reporting of best costs, elapsed wall-clock times (via `omp_get_wtime()`), and speedup factors.
