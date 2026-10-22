## 1. Formulation and Implementation

- [x] 1.1 Create notebook `coin_change_dp.ipynb` and add Problem Formulation section with DP state $DP[a]$ and recurrence $DP[a] = 1 + \min_{c \le a}(DP[a - c])$.
- [x] 1.2 Implement bottom-up DP function `coin_change_dp(coins, amount)` with combination reconstruction and verify on PDF example `coins=[1, 3, 4]`, `amount=6` (yielding 2 coins: `[3, 3]`) and edge cases.
- [x] 1.3 Implement recursive function `coin_change_rec(coins, amount)` and add Markdown section comparing theoretical time and auxiliary space complexities of DP vs Recursion.

## 2. Benchmarking, Visualization, and Analysis

- [x] 2.1 Implement execution time benchmarking measuring runtime of DP and recursive algorithms across varying target amounts and plot the comparison graph using `matplotlib`.
- [x] 2.2 Implement Greedy strategy comparison on `coins=[1, 3, 4]`, `amount=6` and add Markdown analysis explaining why greedy produces suboptimal results while DP succeeds.
- [x] 2.3 Execute all cells in `coin_change_dp.ipynb` using `jupyter` / `nbconvert` / python runner to ensure clean, error-free execution and proper output rendering.
