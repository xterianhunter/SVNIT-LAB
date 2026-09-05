## Context

Academic lab reports and viva evaluations require clean, easy-to-follow code listings. While the root problem scripts in this repository include comprehensive SVG/HTML reporting pipelines, having separate lightweight, report-ready scripts allows students to copy compact, elegant code directly into document appendices.

## Goals / Non-Goals

**Goals:**
- Create a dedicated directory `clean_code/` containing streamlined versions of all three lab assignments.
- `clean_code/problem1_searching.py`: Linear & Binary Search with file dataset handling, 4 positional test cases, microsecond timing, comparison counts, and formatted tabular output (~120 lines).
- `clean_code/problem2_sorting.py`: Bubble Sort (early exit), Selection Sort, and Insertion Sort across Random, Sorted, and Reverse inputs with high-precision timing, comparison tracking, and tabular reporting (~130 lines).
- `clean_code/problem3_matrix.py`: Matrix Addition, Matrix Transpose, and Matrix Multiplication on programmatic square matrices ($10\times10$ to $500\times500$) with timing and theoretical $\mathcal{O}(n^2)$ vs $\mathcal{O}(n^3)$ table output (~120 lines).
- Zero third-party dependencies (pure Python standard library).

**Non-Goals:**
- Removing or altering the root visualization pipelines (`results/*.svg`, `results/*.html`) in existing root files.

## Decisions

1. **Dedicated Directory Structure (`clean_code/`)**:
   - *Choice*: Keep the simplified code isolated in `clean_code/` rather than replacing the root visualization scripts.
   - *Rationale*: Preserves both the full-featured plotting suite and the clean submission-ready code.

2. **Streamlined Code Architecture**:
   - *Choice*: Focus each script strictly on:
     1. First-principle core algorithms (clean & readable).
     2. Dataset generation / file I/O as required by the assignment sheet.
     3. Benchmarking harness with adaptive runs.
     4. Clean formatted console table printer.
     5. Concise theoretical vs empirical complexity analysis.
   - *Rationale*: Maximum academic readability and straightforward printability in a lab report.

## Risks / Trade-offs

- **[Duplication of core algorithm logic]** → Algorithms exist in both root and `clean_code/`. Mitigation: Keep both implementations strictly identical in algorithmic logic while omitting visualization bloat from `clean_code/`.
