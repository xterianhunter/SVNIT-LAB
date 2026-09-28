## Why

The Task Allocation Problem (TAP) in distributed systems maps $M$ tasks to $P$ processing nodes ($P \ll M$) to minimize total system cost, which consists of task execution costs on assigned nodes plus inter-task communication costs incurred when interacting tasks are placed on distinct nodes. Because this problem is NP-hard, heuristic and metaheuristic approaches like Genetic Algorithms (GA) and Particle Swarm Optimization (PSO) are used. For large values of $M$ and $P$, sequential evaluations become a computational bottleneck. Parallelizing GA and PSO using OpenMP enables accelerated convergence and scalable task mapping while providing comparative benchmarking between sequential and parallel implementations.

## What Changes

- **Cost Model Implementation**: Formulate the total cost objective function based on execution cost matrix $X[M][P]$ and inter-task communication cost matrix $C[M][M]$, charging communication costs strictly when communicating tasks are assigned to different processors.
- **Sequential and Parallel Genetic Algorithm (GA)**: Implement chromosome representation (integer vector of size $M$), population fitness evaluation, selection, single-point/uniform crossover, mutation, and elitism, accelerated with OpenMP parallel loops across population evaluations.
- **Sequential and Parallel Particle Swarm Optimization (PSO)**: Implement discrete particle representation, position and velocity updates adapted for discrete node assignment, particle best ($pbest$) and global best ($gbest$) tracking, accelerated with OpenMP parallel loops across swarm evaluations.
- **Benchmarking & Comparison Framework**: Provide benchmarking logic measuring wall-clock execution time, speedup, and solution quality (total cost) across varying scales of $M$ and $P$ comparing sequential vs. parallel GA and PSO.

## Capabilities

### New Capabilities
- `task-allocation`: Implements sequential and OpenMP-parallelized Genetic Algorithm (GA) and Particle Swarm Optimization (PSO) algorithms for distributed task allocation based on execution and inter-task communication costs, along with comparative benchmarking.

### Modified Capabilities
<!-- No existing capabilities modified -->

## Impact

- Standalone simple C files for GA (`ga_task_alloc.c` or modular `task_alloc_ga.c`) and PSO (`pso_task_alloc.c`), or combined comparative runner.
- Compiler requirements: GCC with OpenMP support (`-fopenmp -O2`).
- No external heavy dependencies; utilizes standard C libraries (`stdlib.h`, `stdio.h`, `time.h`, `omp.h`, `math.h`).
