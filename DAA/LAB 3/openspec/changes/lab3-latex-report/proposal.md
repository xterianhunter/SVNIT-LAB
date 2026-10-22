## Why

A complete, formally structured LaTeX document `Lab3.tex` is required for Lab Assignment 3 (Dynamic Programming), replicating the exact visual layout, header, typography, and listing styles from `main.tex`. It must encapsulate the full solutions for Problem 1 (Coin Change) and Problem 2 (Employee Training Planning) from `DAA_Lab3.pdf`, including state formulations, formal algorithm pseudocodes, Python code listings, verified terminal outputs, margin-safe complexity comparison tables, execution time benchmark plots, and in-depth analysis answers.

## What Changes

- Export high-resolution execution time benchmark plots (`plot_coin_change.png` and `plot_employee_training.png`) from the notebook workflows.
- Create `Lab3.tex` with:
  - Matching preamble, 1in margins, Times font, `fancyhdr` header (Name: Kishan Sahu, Enrollment No.: P26DS017), and department title banner for Lab Assignment 3.
  - **Problem Statement 1: Coin Change**:
    - Problem formulation (state $DP[a]$, base cases, recurrence).
    - Algorithm pseudocode: `CoinChangeDP` (with combination reconstruction).
    - Python implementation and verified execution output block.
    - Margin-safe complexity table (DP vs. Recursion).
    - Embedded execution time benchmark graph figure.
    - Analysis answer: Detailed explanation and counterexample on why greedy fails on $\{1, 3, 4\}$ for amount $6$ while DP succeeds.
  - **Problem Statement 2: Employee Training Planning**:
    - Problem formulation (0/1 Knapsack state $DP[i][w]$, base cases, recurrence).
    - Algorithm pseudocode: `EmployeeTrainingDP` (with module reconstruction).
    - Python implementation and verified execution output block on the PDF dataset.
    - Margin-safe complexity table.
    - Embedded execution time scaling graph figure.
    - Analysis answer: Detailed explanation and formulation changes for the Unbounded module repetition modification.

## Capabilities

### New Capabilities
- `lab3-report`: Unified LaTeX lab report (`Lab3.tex`) and associated benchmark graph artifacts covering Problem 1 and Problem 2.

### Modified Capabilities
*(None)*

## Impact

- New files: `Lab3.tex`, `plot_coin_change.png`, `plot_employee_training.png`.
