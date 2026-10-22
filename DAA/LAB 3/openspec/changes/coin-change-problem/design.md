## Context

See `proposal.md` for motivation and background. The objective is to create a clean, short, and self-contained Jupyter notebook (`coin_change_dp.ipynb`) solving Problem 1 (Coin Change) from Lab Assignment 3.

## Goals / Non-Goals

**Goals:**
- Implement bottom-up DP with back-tracking/parent-pointer reconstruction to output the coin combination.
- Implement naive recursive solver for empirical and theoretical comparison.
- Benchmark and plot execution time curves using `matplotlib`.
- Address all 4 problem statements and the greedy counterexample cleanly and concisely.
- Keep code minimal, avoiding unnecessary utility bloat.

**Non-Goals:**
- Problem 2 (Employee Training Planning) from the assignment PDF is excluded.
- External web or GUI frameworks.

## Decisions

### 1. Notebook Architecture and Structure
- Structure the notebook into concise markdown and executable Python cells:
  1. **Problem Formulation**: Markdown cell specifying state $DP[a]$, base case $DP[0]=0$, and transition $DP[a] = 1 + \min_{c \le a}(DP[a - c])$.
  2. **Core Algorithms**:
     - `coin_change_dp(coins, amount)`: Bottom-up DP filling `dp` array and `last_coin` array for $O(K)$ combination reconstruction.
     - `coin_change_rec(coins, amount)`: Naive recursive implementation.
  3. **Verification & Edge Cases**: Verification on $\{1, 3, 4\}$ with amount $6$, plus amount $0$ and unreachable amount.
  4. **Empirical Benchmarking & Graph**: Time measurement using `time.perf_counter()`, plotting Execution Time vs Amount with `matplotlib`.
  5. **Greedy Strategy Counterexample**: Code + Markdown demonstrating $\{1, 3, 4\}$ with amount $6$ producing suboptimal greedy result.

### 2. State & Combination Reconstruction Choice
- Instead of storing subproblem lists inside DP tables ($O(A^2)$ memory), use a 1D `last_coin` array tracking the coin chosen for amount `a`, allowing $O(A)$ auxiliary space and $O(K)$ trace-back for $K$ coins.

### 3. Benchmarking Bounds
- Because recursive coin change has exponential complexity $O(n^A)$, benchmark recursion only up to moderate amounts ($A \le 25..30$) to prevent kernel hangs, while demonstrating DP scalability to larger amounts.

## Risks / Trade-offs

- **[Recursion hanging on large amounts]** → Cap recursion benchmark inputs to $A \le 25$, while running DP across both small and large amounts ($A \le 500$).
- **[Notebook clutter]** → Write only concise, readable functions without redundant helper classes.
