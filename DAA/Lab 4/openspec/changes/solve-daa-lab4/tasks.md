## 1. Problem 1 Implementation (Sorting and Inversion Counting)

- [x] 1.1 Implement Divide and Conquer inversion counting via Merge Sort (`count_inversions_dc`) and Brute Force (`count_inversions_bf`), verifying both on sample array `[8, 4, 2, 1]` returning 6 inversions.
- [x] 1.2 Implement baseline sorting algorithms (Quick Sort and Insertion Sort) to compare against Merge Sort, verifying all algorithms produce sorted arrays.
- [x] 1.3 Implement empirical timing harness measuring execution times for varying array sizes and generate Matplotlib performance curves.
- [x] 1.4 Formulate concise markdown analysis documenting time/space complexity comparisons ($O(n \log n)$ vs $O(n^2)$) and theoretical vs empirical behaviour.

## 2. Problem 2 Implementation (Fast Exponentiation)

- [x] 2.1 Implement repeated multiplication (`power_iterative`), naive recursive exponentiation (`power_recursive_naive`), and Divide & Conquer exponentiation (`power_dc`), verifying outputs match standard exponentiation.
- [x] 2.2 Implement benchmarking across varying exponent sizes $n$ and render comparative Matplotlib plots.
- [x] 2.3 Formulate concise markdown analysis deriving the recurrence relation ($T(n) = T(n/2) + \Theta(1)$), explaining repeated subproblems, iterative vs recursive auxiliary space, and Divide & Conquer paradigm insights.

## 3. Notebook Assembly and Final Validation

- [x] 3.1 Construct the complete, self-contained `DAA_Lab4.ipynb` Jupyter Notebook adhering strictly to the clean, minimal code guidelines with zero unnecessary boilerplate.
- [x] 3.2 Execute the notebook using python/nbconvert or test runner to confirm all cells execute sequentially without errors and output valid results.
