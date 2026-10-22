## Purpose

Provides sequential and parallel metaheuristic algorithms (Genetic Algorithm and Particle Swarm Optimization) using OpenMP to compute optimal or near-optimal task-to-processor mappings in distributed systems.

## ADDED Requirements

### Requirement: Task Allocation Cost Model Evaluation
The system SHALL calculate the total assignment cost as the sum of execution costs of all tasks on their assigned processors plus the inter-task communication costs between pairs of communicating tasks that are assigned to different processors.

#### Scenario: Verification against sample topology
- **WHEN** evaluating a test assignment of 6 tasks to 2 processors with known execution and communication matrices
- **THEN** the system calculates execution cost, inter-processor communication cost, and verifies total cost matching ground truth (e.g. Total cost = 58 for serial assignment and 38 for optimal assignment in sample test case)

#### Scenario: Scalable problem dimensions
- **WHEN** $M$ tasks ($M \gg P$) and $P$ processing nodes are configured with generated or input execution matrix $X[M][P]$ and communication matrix $C[M][M]$
- **THEN** the fitness evaluation correctly aggregates individual task execution costs and cross-processor communication penalties

### Requirement: Sequential and Parallel Genetic Algorithm
The system SHALL provide both a sequential Genetic Algorithm and an OpenMP-parallelized Genetic Algorithm to optimize task allocation.

#### Scenario: Genetic algorithm convergence
- **WHEN** executing GA with population size $N_{pop}$ and $G$ generations
- **THEN** the algorithm iteratively evaluates fitness, performs selection, crossover, and mutation, and returns the best valid task-to-processor mapping

#### Scenario: Parallel GA acceleration
- **WHEN** OpenMP is enabled with multiple threads during GA execution
- **THEN** population fitness evaluations and offspring generation are computed concurrently across OpenMP threads, yielding equivalent or superior solution quality with reduced elapsed time compared to sequential execution

### Requirement: Sequential and Parallel Particle Swarm Optimization
The system SHALL provide both a sequential Particle Swarm Optimization algorithm and an OpenMP-parallelized Particle Swarm Optimization algorithm for discrete task allocation.

#### Scenario: PSO swarm optimization
- **WHEN** executing PSO with swarm size $S$ and iterations $I$
- **THEN** each particle updates its discrete position mapping and velocity vector based on cognitive personal best ($pbest$) and social global best ($gbest$) to find minimal cost allocations

#### Scenario: Parallel PSO acceleration
- **WHEN** OpenMP is enabled with multiple threads during PSO execution
- **THEN** particle position evaluations and updates are executed concurrently across threads, achieving faster wall-clock execution than the sequential PSO

### Requirement: Benchmark Reporting and Solution Comparison
The system SHALL output the best task allocation mapping, minimal cost achieved, wall-clock execution time, and speedup achieved by the parallel implementations compared to their sequential counterparts.

#### Scenario: Performance and speedup comparison
- **WHEN** running benchmarks for large $M$ and $P$ across sequential GA, parallel GA, sequential PSO, and parallel PSO
- **THEN** the system prints execution times for each variant, computes the parallel speedup factor ($T_{seq} / T_{par}$), and displays the resulting optimal costs and task assignments
