## Context

Problem 3 of DAA Lab Assignment 2 requires students to evaluate Matrix Addition ($\mathcal{O}(n^2)$), Matrix Transpose ($\mathcal{O}(n^2)$), and Matrix Multiplication ($\mathcal{O}(n^3)$) across square matrix sizes (10x10, 50x50, 100x100, 200x200, 500x500), generating plots of Matrix Size vs Execution Time and comparing empirical scaling against theoretical complexities.

Currently, `problem3_matrix.py` contains first-principle implementations and runs benchmarks, but lacks graphical vector plots and HTML report generation. Problems 1 and 2 established a zero-dependency SVG vector generator pattern (`results/search_complexity_plot.svg`, `results/sorting_complexity_plot.svg`) and interactive HTML reporting.

## Goals / Non-Goals

**Goals:**
- Implement standalone vector SVG plotting (`results/matrix_complexity_plot.svg`) mapping Matrix Size ($N \times N$) vs Execution Time (ms) across Addition, Transpose, and Multiplication, matching the visual aesthetic and coordinate structure of Problem 1 and Problem 2 plots.
- Illustrate the dramatic divergence between $\mathcal{O}(n^2)$ quadratic operations (Addition, Transpose) and the $\mathcal{O}(n^3)$ cubic polynomial curve (Multiplication).
- Implement interactive HTML report generation (`results/matrix_analysis.html`) embedding the SVG plot, theoretical complexity comparisons ($n^2$ vs $n^3$), and dark-mode results table.
- Implement CSV and Markdown table exporters for matrix metrics.
- Keep implementation zero-dependency (pure Python stdlib).

**Non-Goals:**
- Modifying core matrix operations or using optimized third-party libraries (e.g. NumPy/SciPy/BLAS), preserving academic assignment compliance.

## Decisions

1. **SVG Vector Architecture**:
   - *Choice*: Standalone XML/SVG vector file (`results/matrix_complexity_plot.svg`) with 960x580 dimensions, labeled axes, grid lines, distinct styled lines, and legend.
   - *Rationale*: Matches the design standard across the workspace with zero pip dependencies.

2. **Series Styling**:
   - Matrix Multiplication ($\mathcal{O}(n^3)$): `#d00000` (solid red, diamond glyph) — emphasizes dominant cubic latency.
   - Matrix Addition ($\mathcal{O}(n^2)$): `#3a86ff` (solid blue, circle glyph) — clear quadratic baseline.
   - Matrix Transpose ($\mathcal{O}(n^2)$): `#2b9348` (dashed green, square glyph) — lightweight quadratic assignment baseline.

3. **Integration Surface**:
   - *Choice*: Embed generators directly in `problem3_matrix.py` and provide modular utilities in `src/visualizer.py`.
   - *Rationale*: Single command `python3 problem3_matrix.py` runs benchmarks and outputs all terminal and graphical artifacts.

## Risks / Trade-offs

- **[Cubic polynomial magnitude range]** → Matrix Multiplication at 500x500 takes ~1000–1200 ms while Addition at 10x10 takes < 0.005 ms. Mitigation: Provide precise millisecond scaling and detailed analytical callouts in the HTML report and console outputs.
- **[Zero external dependencies]** → Manual SVG coordinate math. Mitigation: Use proven coordinate mapping techniques established in previous problem visualizers.
