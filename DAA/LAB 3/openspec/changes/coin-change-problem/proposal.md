## Why

Lab Assignment 3 (CSDS103) requires solving Problem 1: Coin Change using Dynamic Programming. A concise, well-structured, and minimal Jupyter Notebook (`coin_change_dp.ipynb`) is needed to demonstrate all 4 required points, verify the PDF example ({1, 3, 4} with target 6), reconstruct coin combinations, benchmark execution times with graphical plots, and explain the greedy strategy counterexample without unnecessary boilerplate.

## What Changes

- Create a concise Jupyter Notebook `coin_change_dp.ipynb` implementing:
  - **DP Formulation**: Clear state definition $DP[a]$ and recurrence relation $DP[a] = 1 + \min_{c \le a}(DP[a - c])$.
  - **Bottom-Up DP Implementation**: Iterative bottom-up algorithm returning both minimum coins and a reconstructed coin combination, handling edge cases (target 0, unreachable target).
  - **Recursive vs DP Comparison**: Theoretical comparison of time and space complexity ($O(c^A)$ vs $O(n \cdot A)$).
  - **Empirical Execution Time Experimentation**: Time measurements across varying amounts and denomination counts, plotted using `matplotlib`.
  - **Greedy Counterexample Analysis**: Discussion and demonstration of why greedy fails for $\{1, 3, 4\}$ with amount 6 ($4+1+1=3$ coins vs DP $3+3=2$ coins).

## Capabilities

### New Capabilities
- `coin-change`: Complete bottom-up DP and recursive coin change solvers, combination reconstruction, complexity analysis, execution time benchmarking with plots, and greedy counterexample evaluation.

### Modified Capabilities
*(None)*

## Impact

- New file: `coin_change_dp.ipynb`
- Python runtime dependencies: `matplotlib` (standard scientific python environment)
