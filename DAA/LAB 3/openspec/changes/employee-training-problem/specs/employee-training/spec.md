## Purpose

Provides Dynamic Programming formulation (0/1 Knapsack), bottom-up implementation, module reconstruction, complexity analysis, execution time benchmarking with graphs, and unbounded module repetition analysis for the Employee Training Planning problem.

## ADDED Requirements

### Requirement: Bottom-Up DP Employee Training Planner with Module Reconstruction
The system SHALL compute the maximum achievable benefit for an employee given $n$ training modules with specified costs and benefits under a maximum budget $B$ (where each module can be selected at most once), and reconstruct the exact subset of selected modules.

#### Scenario: PDF Table Example with budget B = 10
- **WHEN** modules are $M_1(4, 7), M_2(6, 10), M_3(5, 8), M_4(3, 5)$ and budget $B = 10$
- **THEN** the solver returns maximum benefit $17$, total cost $10$, and selected modules `['M1', 'M2']`

#### Scenario: Budget is zero
- **WHEN** budget $B = 0$
- **THEN** the solver returns maximum benefit $0$, total cost $0$, and an empty module list `[]`

#### Scenario: All module costs exceed budget
- **WHEN** all available modules have costs greater than $B$
- **THEN** the solver returns maximum benefit $0$ and an empty list `[]`

### Requirement: Complexity Analysis
The system SHALL provide theoretical time complexity and auxiliary space complexity analysis for the 0/1 Dynamic Programming solution.

#### Scenario: Complexity documentation
- **WHEN** viewing the complexity section of the notebook
- **THEN** it explicitly details $\mathcal{O}(n \cdot B)$ time complexity and $\mathcal{O}(n \cdot B)$ / $\mathcal{O}(B)$ auxiliary space complexity

### Requirement: Execution Time Benchmarking and Graph
The system SHALL measure execution time changes as the number of modules $n$ and the budget $B$ increase, and plot the execution time curves using `matplotlib`.

#### Scenario: Execution time graph generation
- **WHEN** the benchmarking cell is executed
- **THEN** empirical execution times are measured and a clear comparative plot (Execution Time vs. Budget $B$ across varying $n$) is rendered

### Requirement: Unbounded Module Repetition Analysis
The system SHALL analyze the modification where training modules can be selected more than once (Unbounded Knapsack), defining the modified DP state, recurrence relation, and comparing its behavior and complexity to the 0/1 formulation.

#### Scenario: Unbounded DP formulation and execution
- **WHEN** running the unbounded modification analysis on the PDF example with budget $B = 10$
- **THEN** the solver shows how multiple selections of the most cost-effective module are evaluated ($DP[w] = \max_i(DP[w-c_i] + b_i)$) and explains the structural differences from the 0/1 constraint
