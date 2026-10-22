## Context

See `proposal.md` for motivation. The reference template is `main.tex`. All algorithm implementations, benchmark routines, and outputs are established in `coin_change_dp.ipynb` and `employee_training_dp.ipynb`.

## Goals / Non-Goals

**Goals:**
- Generate PNG plot images `plot_coin_change.png` and `plot_employee_training.png` at 300 DPI.
- Create `Lab3.tex` using the exact layout, preamble, header, fonts, and styles from `main.tex`.
- Guarantee table margin safety using explicit column widths (`p{...}`).
- Cover all 4 sub-points per problem plus comprehensive answers for both Analysis sections from `DAA_Lab3.pdf`.
- Compile `Lab3.tex` to `Lab3.pdf` with `pdflatex` to verify zero errors and clean typesetting.

**Non-Goals:**
- Modifying `main.tex` (preserved as reference).

## Decisions

### 1. Document Structure in `Lab3.tex`
- **Header Banner**: SVNIT, M.Tech. I, Design and Analysis of Algorithm (CSDS103), Lab Assignment 3 (Dynamic Programming).
- **Problem Statement 1: Coin Change**:
  - Problem Statement and DP Formulation ($DP[a] = 1 + \min_{c \le a} DP[a-c]$).
  - Algorithm pseudocode: `CoinChangeDP`.
  - Python implementation listing (`style=code`).
  - Terminal output listing (`style=output`).
  - Complexity comparison table with explicit width bounds ($O(n \cdot A)$ vs $O(n^A)$).
  - Empirical execution time plot figure (`plot_coin_change.png`).
  - Formal Analysis answering why greedy fails on $\{1, 3, 4\}$ for amount $6$ while DP succeeds.
- **Problem Statement 2: Employee Training Planning**:
  - Problem Statement and 0/1 Knapsack formulation ($DP[i][w] = \max(DP[i-1][w], DP[i-1][w-c_i] + b_i)$).
  - Algorithm pseudocode: `EmployeeTrainingDP`.
  - Python implementation listing (`style=code`).
  - Terminal output listing on PDF dataset (`style=output`).
  - Complexity comparison table with explicit width bounds.
  - Empirical execution time scaling plot figure (`plot_employee_training.png`).
  - Formal Analysis answering the unbounded module repetition modification.

### 2. Margin Safety and Table Layout
- Tables will use `\begin{tabular}{|p{3.2cm}|p{3.2cm}|p{7.2cm}|}` ensuring the total table width ($13.6\,\text{cm}$) fits safely within the $15.9\,\text{cm}$ text width of A4 with 1-inch margins.

### 3. Figure Embedding
- Figures will use `\begin{figure}[H] \centering \includegraphics[width=0.92\textwidth]{...} \end{figure}` to prevent floating issues and ensure crisp visual integration.

## Risks / Trade-offs

- **[LaTeX package compatibility]** → `main.tex` preamble already specifies `newtxtext`, `newtxmath`, `geometry`, `listings`, `graphicx`, `float`, `algorithm`, `algpseudocode`, which are standard.
