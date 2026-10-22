## 1. SVG & Terminal Visualizers

- [x] 1.1 Implement sorting SVG plot generation (`generate_sorting_svg_plot`) mapping Input Size ($N$) vs Execution Time across Bubble, Selection, and Insertion Sorts for Random, Sorted, and Reverse datasets, matching the visual aesthetic and coordinate structure of `results/search_complexity_plot.svg`. Verify SVG output is valid XML and scales cleanly.
- [x] 1.2 Implement ASCII terminal bar chart generator (`generate_sorting_ascii_charts`) for sorting algorithms across input types and verify proper formatting in terminal output.

## 2. HTML Reporting & Metric Exports

- [x] 2.1 Implement interactive HTML report generation (`generate_sorting_html_report`) with embedded SVG plot, metric cards, styled dark-mode results table, and theoretical complexity breakdown. Verify HTML output renders correctly in browser.
- [x] 2.2 Implement CSV and Markdown table exporters for sorting benchmark metrics. Verify exported files in `results/` contain complete test case rows.

## 3. Integration & End-to-End Verification

- [x] 3.1 Integrate visualization generators and export steps into `problem2_sorting.py` while maintaining zero-dependency portability and self-contained execution.
- [x] 3.2 Run `python3 problem2_sorting.py` end-to-end and verify that `results/sorting_complexity_plot.svg`, `results/sorting_analysis.html`, and formatted terminal outputs are generated accurately.
