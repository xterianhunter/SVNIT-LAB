## Why

DAA Lab Assignment 7 requires implementing and analyzing three fundamental string matching algorithms (Naive String Matching, Knuth-Morris-Pratt (KMP), and Rabin-Karp) as well as generating empirical comparison graphs for a student's submission. A clean, beginner-friendly Jupyter Notebook (`.ipynb`) is needed to clearly demonstrate each algorithm, track comparison/verification metrics, analyze worst-case and collision scenarios, and visualize performance benchmarks without extraneous complexity.

## What Changes

- Create a structured, self-contained Jupyter Notebook (`DAA_Lab7_String_Matching.ipynb`) covering:
  - **Problem 1 (Naive String Matching)**: Simple implementation, exact comparison counter, test cases, and worst-case scenario demonstration.
  - **Problem 2 (Knuth-Morris-Pratt Algorithm)**: Clean LPS computation without built-in methods, search routine with comparison tracking, and direct comparison with Naive.
  - **Problem 3 (Rabin-Karp Algorithm)**: Straightforward polynomial rolling hash, rolling update formula, tracking of hash matches and character-by-character verifications, and demonstration of hash collisions.
  - **Problem 4 (Experimental Comparison & Visualizations)**: Clear benchmark driver and matplotlib plots for:
    1. Input Size vs Execution Time
    2. Pattern Length vs Execution Time
    3. Input Size vs Number of Comparisons
- Keep all implementations student-friendly, readable, standard Python with zero unnecessary dependencies beyond `matplotlib` and `time`.

## Capabilities

### New Capabilities
- `string-matching`: Implementation, analysis counters, and benchmark visualizations for Naive, KMP, and Rabin-Karp algorithms in a clean student Jupyter Notebook.

### Modified Capabilities
<!-- None -->

## Impact

- Creates `DAA_Lab7_String_Matching.ipynb` in the workspace.
- Requires standard Python libraries (`time`, `random`) and `matplotlib` for graph generation.
- No existing production or lab codebase is altered.
