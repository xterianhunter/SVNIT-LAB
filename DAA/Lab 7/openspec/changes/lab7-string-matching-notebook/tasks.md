## 1. Problem 1 - Naive String Matching Implementation & Analysis

- [x] 1.1 Implement naive string search function counting character comparisons and verify occurrences at [0, 9, 12] for text "AABAACAADAABAABA" and pattern "AABA"
- [x] 1.2 Implement worst-case demonstration (e.g., text of repeated 'A's and pattern "AAAB") showing comparison count close to $(n-m+1) \times m$ with markdown explanation

## 2. Problem 2 - Knuth-Morris-Pratt (KMP) String Matching

- [x] 2.1 Implement `compute_lps` without built-in matching and verify LPS array [0, 0, 1, 2, 0, 1, 2, 3, 4] for pattern "ABABCABAB"
- [x] 2.2 Implement `kmp_search` with comparison counter and verify matching indices and reduced comparisons relative to Naive on repetitive inputs

## 3. Problem 3 - Rabin-Karp String Matching & Collision Analysis

- [x] 3.1 Implement `rabin_karp_search` with polynomial rolling hash, counting hash matches and character-by-character verifications
- [x] 3.2 Construct and demonstrate an explicit hash collision case, explaining why hash match does not guarantee pattern match and discussing modulus/radix selection

## 4. Problem 4 - Experimental Benchmarking & Visualizations

- [x] 4.1 Implement benchmark runner measuring runtime and comparison counts across varying text lengths ($n$) and pattern lengths ($m$)
- [x] 4.2 Create clean matplotlib plots for Input Size vs Execution Time, Pattern Length vs Execution Time, and Input Size vs Number of Comparisons
- [x] 4.3 Assemble and validate the complete student Jupyter Notebook `DAA_Lab7_String_Matching.ipynb` ensuring all cells execute cleanly without errors
