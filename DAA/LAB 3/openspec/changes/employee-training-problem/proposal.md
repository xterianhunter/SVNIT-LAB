## Why

Lab Assignment 3 (CSDS103) requires solving Problem 2: Employee Training Planning using Dynamic Programming. A concise, well-structured, and minimal Jupyter Notebook (`employee_training_dp.ipynb`) is needed to formulate the 0/1 Knapsack model, implement bottom-up DP with module reconstruction using the PDF example, analyze complexity, benchmark execution time scaling with graphs across varying $n$ and $B$, and analyze the unbounded repetition modification without unnecessary boilerplate.

## What Changes

- Create a concise Jupyter Notebook `employee_training_dp.ipynb` implementing:
  - **DP Formulation**: State definition $DP[i][w]$, base cases $DP[0][w] = 0$, and 0/1 recurrence $DP[i][w] = \max(DP[i-1][w], DP[i-1][w-c_i] + b_i)$.
  - **Bottom-Up DP Implementation & Reconstruction**: Solver reconstructing the exact selected modules for budget $B$ on the PDF test dataset ($M_1(4, 7), M_2(6, 10), M_3(5, 8), M_4(3, 5)$).
  - **Complexity Analysis**: Time complexity $\mathcal{O}(n \cdot B)$ and auxiliary space complexity $\mathcal{O}(n \cdot B)$ (or $\mathcal{O}(B)$ for space-optimized DP).
  - **Execution Time Experimentation**: Time measurements across varying number of modules $n$ and budget $B$, plotted using `matplotlib`.
  - **Unbounded Repetition Analysis**: Problem formulation, recurrence changes ($DP[w] = \max_i(DP[w-c_i] + b_i)$), and behavioral differences when modules can be repeated.

## Capabilities

### New Capabilities
- `employee-training`: DP solver for Employee Training Planning (0/1 Knapsack), module subset reconstruction, time and space analysis, benchmark graphs, and unbounded module repetition comparison.

### Modified Capabilities
*(None)*

## Impact

- New file: `employee_training_dp.ipynb`
- Python runtime dependencies: `matplotlib`
