## Purpose

Provides Dynamic Programming formulation, bottom-up implementation, coin combination reconstruction, recursive complexity comparison, execution time benchmarking with graphs, and greedy counterexample analysis for the Coin Change problem.

## ADDED Requirements

### Requirement: Bottom-Up DP Coin Change Solver with Reconstruction
The system SHALL compute the minimum number of coins needed to make a target amount using given denominations (with infinite coin supply) and reconstruct the exact combination of coins used using bottom-up Dynamic Programming.

#### Scenario: PDF Example with valid solution
- **WHEN** denominations are `[1, 3, 4]` and target amount is `6`
- **THEN** the solver returns minimum coin count `2` and combination `[3, 3]`

#### Scenario: Target amount is zero
- **WHEN** target amount is `0`
- **THEN** the solver returns minimum coin count `0` and empty combination `[]`

#### Scenario: Unreachable target amount
- **WHEN** denominations cannot form the target amount (e.g., `[2, 4]` and target `7`)
- **THEN** the solver reports no solution (e.g., returns `-1` or `None` with an empty combination)

### Requirement: Recursive Formulation and Complexity Analysis
The system SHALL implement a recursive coin change solver and provide a comparative analysis of time and auxiliary space complexity between the recursive and bottom-up DP approaches.

#### Scenario: Recursive solver correctness
- **WHEN** target amount `6` and denominations `[1, 3, 4]` are passed to the recursive solver
- **THEN** it outputs minimum coin count `2`

#### Scenario: Theoretical complexity comparison
- **WHEN** analyzing both algorithms
- **THEN** the notebook presents that DP has $O(n \cdot A)$ time and $O(A)$ auxiliary space, while naive recursion has $O(n^A)$ exponential time and $O(A)$ call-stack space

### Requirement: Empirical Execution Time Benchmarking and Graph
The system SHALL measure execution times of both recursive and DP implementations across varying target amounts and denomination configurations, and plot the resulting execution time curves using `matplotlib`.

#### Scenario: Generate execution time graph
- **WHEN** the benchmark cell is executed
- **THEN** execution times for DP and recursion are measured and a clear comparative line graph is displayed

### Requirement: Greedy Strategy Counterexample and Analysis
The system SHALL analyze the greedy strategy for coin change, demonstrate a counterexample where greedy fails to find the optimal solution, and explain why DP succeeds.

#### Scenario: Greedy counterexample demonstration
- **WHEN** greedy algorithm is run on denominations `[1, 3, 4]` with target `6`
- **THEN** greedy selects `[4, 1, 1]` (3 coins), proving suboptimality compared to DP's `[3, 3]` (2 coins)
