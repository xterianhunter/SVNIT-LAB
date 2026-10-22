## 1. Formulation and Core Implementation

- [x] 1.1 Create notebook `employee_training_dp.ipynb` and add Problem Formulation section with 0/1 DP state $DP[i][w]$, base cases, and recurrence relation $DP[i][w] = \max(DP[i-1][w], DP[i-1][w-c_i] + b_i)$.
- [x] 1.2 Implement bottom-up DP function `employee_training_01_dp(modules, budget)` with module subset reconstruction and test on PDF dataset $M_1(4, 7), M_2(6, 10), M_3(5, 8), M_4(3, 5)$ with budget $B = 10$ and edge cases ($B=0$, budget too small).
- [x] 1.3 Add Markdown section analyzing time complexity $\mathcal{O}(n \cdot B)$ and auxiliary space complexity $\mathcal{O}(n \cdot B)$ (with note on $\mathcal{O}(B)$ 1D space optimization).

## 2. Benchmarking, Visualization, and Modification Analysis

- [x] 2.1 Implement execution time benchmarking measuring runtime across increasing module counts $n$ and budgets $B$, and plot the scaling graph using `matplotlib`.
- [x] 2.2 Implement the Unbounded Module Repetition variant `employee_training_unbounded_dp(modules, budget)` and document the recurrence, complexity, and behavioral comparison against 0/1 selection.
- [x] 2.3 Execute all cells in `employee_training_dp.ipynb` using `.venv/bin/python` / `nbclient` to verify error-free execution, tables, and rendered plots.
