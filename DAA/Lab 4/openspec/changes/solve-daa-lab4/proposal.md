## Why

DAA Lab Assignment 4 (SVNIT CSDS103) requires students to implement, analyze, and compare Divide and Conquer algorithms against alternative approaches for two classic problems: Sorting & Counting Inversions, and Fast Exponentiation. Providing a concise, self-contained Jupyter Notebook (`DAA_Lab4.ipynb`) enables clean execution, timing comparisons, and graphical visualization without unnecessary code bloat or complex external dependencies.

## What Changes

- Create a single, clean Jupyter Notebook `DAA_Lab4.ipynb` addressing all requirements from `DAA_Lab4.pdf`.
- Implement Problem 1:
  - Divide and Conquer approach (enhanced Merge Sort counting inversions in $O(n \log n)$ time and $O(n)$ space).
  - Brute force approach (pairwise inspection in $O(n^2)$ time and $O(1)$ space).
  - Baseline comparison sorts (Quick Sort and Insertion Sort).
  - Empirical benchmarking across varying array sizes and visualization with matplotlib.
- Implement Problem 2:
  - Repeated multiplication ($O(n)$ iterative).
  - Naive recursive exponentiation ($O(n)$ time branching recurrence).
  - Divide and Conquer exponentiation computing $a^{n/2}$ once ($O(\log n)$ time).
  - Empirical timing across various values of $n$ and visualization.
  - Clear markdown cells addressing the analysis questions (recurrence derivation, complexity breakdown, effect of repeated subproblems, iterative vs recursive aux space, D&C paradigm comparison).
- Keep all implementations minimal, readable, and free of extraneous libraries or convoluted boilerplate.

## Capabilities

### New Capabilities
- `divide-and-conquer-lab`: Complete implementation, benchmarking, and analysis for Inversion Counting and Fast Exponentiation as required by DAA Lab 4.

### Modified Capabilities
<!-- None -->

## Impact

- **New Files**: `DAA_Lab4.ipynb` in workspace root.
- **Dependencies**: Python 3 standard library (`time`, `random`) and `matplotlib` for generating requirement-specified performance graphs.
- **No breaking changes** to any existing project files.
