## Context

To make the code execution self-contained, interactive, and clearly illustrative for academic lab reports, each script should print a sample run demonstrating the state of inputs Before and After applying the algorithm before presenting the multi-size scalability table.

## Goals / Non-Goals

**Goals:**
- In `clean_code/problem1_searching.py`, implement `demonstrate_searching()` to show the $N=10$ array before search, followed by target search results (Beginning, Middle, End, Absent) for Linear & Binary Search.
- In `clean_code/problem2_sorting.py`, implement `demonstrate_sorting()` to show the $N=10$ array Before Sorting and After Sorting (Bubble, Selection, Insertion) across Random, Already Sorted, and Reverse Sorted inputs.
- In `clean_code/problem3_matrix.py`, implement `demonstrate_matrix_operations()` to show $3\times3$ input matrices $A$ and $B$, followed by the result matrices After Addition, Transpose, and Multiplication.
- Retain complete 10-size benchmark tables and theoretical complexity analysis in all three files.

**Non-Goals:**
- Bloating the scripts with non-essential libraries.

## Decisions

1. **Demonstration Placement**:
   - Execute the demonstration phase first (Step 1), followed by the 10-size benchmark table (Step 2), followed by the theoretical analysis (Step 3).
   - This creates a natural narrative: (1) Correctness proof -> (2) Empirical Benchmarks -> (3) Complexity Analysis.

2. **Matrix Print Helper**:
   - Use a lightweight, clean 3-line matrix printer helper to format 2D matrices neatly with bracketed rows and aligned columns.

## Risks / Trade-offs

- **[Slight increase in console output]** → Output will show both demonstration and benchmark tables. Mitigation: Use clear section separators (`===`) so the report reader can easily distinguish Demonstration from Scaling Metrics.
