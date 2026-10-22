## Context

See `proposal.md` for the motivation and academic lab requirements. The objective is to produce a clean, accessible Jupyter Notebook (`DAA_Lab7_String_Matching.ipynb`) for SVNIT M.Tech DAA Lab Assignment 7, covering Naive, KMP, and Rabin-Karp algorithms with analytical counters and visualization plots.

## Goals / Non-Goals

**Goals:**
- Provide clear, idiomatic, beginner-friendly Python functions for each of the 3 algorithms without complex OOP wrappers or obscure idioms.
- Accurately count character comparisons (Naive, KMP) and hash matches/verifications (Rabin-Karp) as mandated by the lab instructions.
- Provide explicit demonstrations of the assignment's specific examples (e.g., $T =$ "AABAACAADAABAABA", $P =$ "AABA", LPS for "ABABCABAB", and hash collision analysis).
- Deliver 3 clean, styled Matplotlib graphs comparing runtime and comparison operations across various text and pattern sizes.

**Non-Goals:**
- Production-grade string search libraries (e.g., C-extensions, Boyer-Moore, Aho-Corasick).
- Over-engineered visualization dashboards or web interfaces.

## Decisions

1. **Jupyter Notebook Architecture (`.ipynb`)**:
   - Organize into logical sections: Header & Setup, Problem 1 (Naive), Problem 2 (KMP), Problem 3 (Rabin-Karp), and Problem 4 (Comparative Analysis & Plots).
   - Use Markdown cells to describe the algorithm logic, time complexities ($O(n \cdot m)$, $O(n + m)$, etc.), and auxiliary space complexities before each code block.
   - *Alternative considered*: Separate `.py` scripts. *Rationale*: Lab assignment explicitly asks for an `.ipynb` file with inline graphs and theoretical analysis.

2. **Instrumenting Comparison and Hash Verification Counters**:
   - Return metrics as a clean dictionary or tuple `(positions, comparisons)` from search functions.
   - For Rabin-Karp, return `(positions, hash_matches, verifications)`.
   - *Rationale*: Avoids global state, simplifies testing, and makes comparisons transparent for the student.

3. **Standard Hash Parameters for Rabin-Karp**:
   - Use standard radix $d = 256$ and a prime modulus $q = 101$ (classic textbook choice) or $q = 1000000007$ for benchmarks. For collision demonstration, use a smaller modulus (e.g., $q = 13$ or $101$) to intentionally trigger and demonstrate a hash collision.
   - *Rationale*: Aligns directly with CLRS curriculum taught in university algorithms courses.

4. **Synthetic Data Generation for Visualizations**:
   - Use strings drawn from small alphabets (e.g., $\Sigma = \{'A', 'B'\}$) to induce realistic partial matches where the difference between $O(n \cdot m)$ Naive and $O(n)$ KMP is visibly pronounced.
   - Measure execution times using `time.perf_counter()` over several iterations to ensure smooth, representative plot curves.

## Risks / Trade-offs

- **[Risk]** Large text lengths in Python can cause timing jitter on short patterns.
  - *Mitigation*: Select appropriate input ranges (e.g., $n$ from 1,000 to 20,000) so timing differences are clear and repeatable without running excessively long.
- **[Risk]** Student notebook dependencies.
  - *Mitigation*: Restrict dependencies to built-in Python modules (`time`, `random`) and standard `matplotlib`.
