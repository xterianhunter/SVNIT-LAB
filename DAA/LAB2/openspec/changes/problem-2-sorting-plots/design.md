## Context

Problem 2 of DAA Lab Assignment 2 requires students to experimentally evaluate Bubble Sort, Selection Sort, and Insertion Sort across three input distributions (Randomly ordered, Already sorted, Reverse sorted) and multiple input sizes (50, 100, 200, 500), generating plots of Input Size vs Execution Time and comparing them to theoretical best/worst-case complexities ($\mathcal{O}(n)$, $\mathcal{O}(n^2)$, $\Theta(n^2)$).

Currently, `problem2_sorting.py` contains the algorithm implementations and a terminal table output harness, but lacks automated graph plotting. Problem 1 established a standalone SVG vector renderer pattern in `src/visualizer.py` (`results/search_complexity_plot.svg`) and interactive HTML generation (`results/search_analysis.html`) without external dependencies.

## Goals / Non-Goals

**Goals:**
- Implement standalone SVG plotting for sorting algorithms that matches the styling, high resolution, and aesthetic design of `results/search_complexity_plot.svg`.
- Plot Input Size vs Execution Time (in µs or ms) across all 3 algorithms for Random, Already Sorted, and Reverse Sorted datasets.
- Support both multi-series comparative views and sub-category representations so linear $\mathcal{O}(n)$ and quadratic $\mathcal{O}(n^2)$ behaviors are easily readable.
- Generate an interactive, self-contained HTML report (`results/sorting_analysis.html`) that embeds the SVG plot, detailed metrics table, and theoretical complexity breakdown.
- Integrate the visualizer into `problem2_sorting.py` while keeping the script self-contained and zero-dependency (pure Python stdlib).

**Non-Goals:**
- Adding external heavy plotting dependencies (such as `matplotlib` or `seaborn`) to ensure portability across grading environments.
- Modifying the core sorting algorithm implementations in `problem2_sorting.py`.

## Decisions

1. **SVG Vector Architecture matching Search Complexity Plot**:
   - *Choice*: Generate standard standalone vector SVG (`results/sorting_complexity_plot.svg`) using XML string templates.
   - *Rationale*: Zero external dependencies, crisp vector scaling at any resolution, consistent with `search_complexity_plot.svg`.
   - *Alternatives*: Matplotlib/PNG export (rejected due to missing dependencies in some lab testbeds).

2. **Series Styling & Palette Hierarchy**:
   - *Choice*: Group colors by algorithm family with line styles indicating input distribution:
     - Bubble Sort: Blue tones (`#1d3557` Reverse, `#457b9d` Random, `#a8dadc` Sorted).
     - Selection Sort: Green tones (`#2b9348` Reverse, `#55a630` Random, `#80b918` Sorted).
     - Insertion Sort: Red/Orange tones (`#d62828` Reverse, `#e85d04` Random, `#faa307` Sorted).
     - Dashed/solid lines and distinct geometric glyphs (circles, squares, triangles, diamonds) for crystal-clear visual differentiation.
   - *Rationale*: Makes 9 series immediately intuitive and distinguishable at a glance.

3. **Time Scaling & Units**:
   - *Choice*: Render primary execution times in microseconds (µs) or milliseconds (ms) with dynamically scaled Y-axis ticks and labeled data points.
   - *Rationale*: Clearly illustrates the divergence between $\mathcal{O}(n)$ flat/linear curves and $\mathcal{O}(n^2)$ parabolic curves as $N$ scales from 50 to 500.

4. **Integration Surface**:
   - *Choice*: Embed SVG and HTML generation directly in `problem2_sorting.py` (and export helper in `src/visualizer.py` if modularized), saving outputs to `results/sorting_complexity_plot.svg` and `results/sorting_analysis.html`.
   - *Rationale*: Running `python3 problem2_sorting.py` produces the complete experimental evaluation suite in a single command.

## Risks / Trade-offs

- **[Wide magnitude difference between $\mathcal{O}(n)$ and $\mathcal{O}(n^2)$]** → Reverse sort for $N=500$ takes ~10–12 ms while sorted insertion sort takes < 1 µs. Mitigation: Use clean grid scaling, precise tooltips in HTML, and highlight best-case vs worst-case callouts in both the SVG subtitle and the HTML report.
- **[Zero-dependency requirement]** → Must manually calculate Cartesian coordinates for SVG path generation and axis ticks. Mitigation: Leverage and adapt the proven coordinate math from `src/visualizer.py`.
