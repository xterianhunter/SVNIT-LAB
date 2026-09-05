## Context

See `proposal.md` for motivation. The goal is to build a minimal, clean Jupyter Notebook (`employee_training_dp.ipynb`) solving Problem 2 (Employee Training Planning) from Lab Assignment 3.

## Goals / Non-Goals

**Goals:**
- Implement 0/1 Knapsack Dynamic Programming with 2D table state $DP[i][w]$ and module reconstruction.
- Test and verify on the PDF module dataset ($M_1: (4, 7), M_2: (6, 10), M_3: (5, 8), M_4: (3, 5)$).
- Provide theoretical time ($\mathcal{O}(n \cdot B)$) and auxiliary space ($\mathcal{O}(n \cdot B)$ / $\mathcal{O}(B)$) analysis.
- Empirical execution time benchmarking studying the effect of increasing $n$ and $B$, plotted with `matplotlib`.
- Formulate, implement, and compare the Unbounded module repetition variant.

**Non-Goals:**
- Problem 1 (Coin change) is excluded.
- External dependencies beyond standard library and `matplotlib`.

## Decisions

### 1. 2D DP Table Representation for 0/1 Knapsack
- A 2D array `dp[i][w]` of size $(n+1) \times (B+1)$ is used:
  - Row $i$ corresponds to the first $i$ modules.
  - Column $w$ corresponds to the current budget capacity.
  - Backtracking is done by checking if `dp[i][w] != dp[i-1][w]`, which indicates module $i$ was selected, allowing exact subset reconstruction in $\mathcal{O}(n)$ time.

### 2. Empirical Benchmarking Plan
- Test scaling with budget $B \in [100, 2000]$ across multiple module counts $n \in [20, 50, 100]$.
- Plot multiple lines (one per $n$) showing the linear growth with respect to both $B$ and $n$, matching $\mathcal{O}(n \cdot B)$.

### 3. Unbounded Module Repetition Analysis
- Formulate the 1D recurrence $DP[w] = \max_i(DP[w-c_i] + b_i)$ where modules can be picked multiple times.
- Show how the optimal benefit changes when repetition is allowed for the PDF example.

## Risks / Trade-offs

- **[Large Memory for huge B and n]** → Standard assignment ranges ($n \le 100, B \le 2000$) use $< 2\,\text{MB}$ memory, which is well within standard limits.
