## Why

A complete, formal academic lab report in LaTeX (`report.tex`) is required for SVNIT M.Tech DAA Lab Assignment 7 (String Matching Algorithms) under the student's credentials (Name: Kishan Sahu, Enrollment No.: P26DS017). The document must incorporate all problem descriptions, theoretical analyses, clean Python code listings, terminal execution outputs, worst-case / collision proofs, and visualization plots.

## What Changes

- Create `report.tex` utilizing the student's exact LaTeX preamble, page geometry, typography, running headers, and listing styles.
- Include comprehensive sections for:
  - **Problem 1 – Naive String Matching**: Algorithm formulation, $O((n-m+1)m)$ worst-case and $O(n)$ best-case analysis, complete Python code, terminal output, worst-case demonstration ($T=\text{"A"}^{20}, P=\text{"A"}^4\text{"B"}$), and explanation of redundant comparisons.
  - **Problem 2 – Knuth–Morris–Pratt (KMP)**: LPS array mathematical definition, $O(n+m)$ complexity analysis, Python code for `compute_lps` and `kmp_search`, output on "ABABCABAB", and comparative character comparison count.
  - **Problem 3 – Rabin–Karp Algorithm**: Polynomial rolling hash function, $O(1)$ rolling update equation, average vs worst-case complexity, Python implementation, terminal outputs, and detailed hash collision analysis ($d=256, q=101$ with strings `'AAB'` and `'BEA'`).
  - **Problem 4 – Experimental Comparison & Visualizations**: Descriptions of benchmarks, embedded/saved figures for:
    1. Input Size vs Execution Time
    2. Pattern Length vs Execution Time
    3. Input Size vs Number of Comparisons
  - **Summary & Conclusion**: Comparative table summarizing preprocessing, matching time, space, backtracking, and use cases.
- Export plot images from the notebook as image assets for seamless LaTeX figure inclusion.

## Capabilities

### New Capabilities
- `latex-lab-report`: Generation and compilation of the comprehensive academic LaTeX lab report (`report.tex`) with complete code listings, output blocks, and visualization figures.

### Modified Capabilities
<!-- None -->

## Impact

- Creates `report.tex` in `/home/xterianhunter/LABS/DAA/Lab 7/`.
- Exports plot figures (e.g. `plot_time_vs_n.png`, `plot_time_vs_m.png`, `plot_comp_vs_n.png`) in the workspace for LaTeX `\includegraphics`.
- No modification to existing assignment code or `.ipynb` file.
