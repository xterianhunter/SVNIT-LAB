## Purpose

Generates vector SVG complexity plots, interactive HTML reports, and ASCII terminal graphs for sorting algorithm benchmarks across Random, Sorted, and Reverse input configurations.

## ADDED Requirements

### Requirement: Standalone SVG Complexity Plot Generation
The system SHALL generate a standalone, dependency-free vector SVG plot (`results/sorting_complexity_plot.svg`) that maps Input Size ($N$) on the X-axis against Execution Time on the Y-axis for Bubble Sort, Selection Sort, and Insertion Sort across multiple input sizes.

#### Scenario: Successfully generating SVG complexity plot
- **WHEN** the sorting benchmark completes
- **THEN** an SVG file is generated at `results/sorting_complexity_plot.svg` with axes, gridlines, distinctive styled series for each algorithm-distribution pair, and an informative legend matching the visual style of `results/search_complexity_plot.svg`

### Requirement: Multi-Distribution Comparative Visualization
The system SHALL visualize the performance of Bubble Sort, Selection Sort, and Insertion Sort across three distinct input distributions: Randomly Ordered, Already Sorted, and Reverse Sorted, clearly displaying the differences between $\mathcal{O}(n)$, $\mathcal{O}(n^2)$, and $\Theta(n^2)$ complexities.

#### Scenario: Visualizing best-case vs worst-case behaviors
- **WHEN** benchmark results containing Random, Sorted, and Reverse cases are processed
- **THEN** the plot highlights the linear scaling of optimized Bubble Sort and Insertion Sort on sorted data alongside quadratic curves on reverse and random inputs

### Requirement: Interactive HTML Report Generation
The system SHALL generate a comprehensive HTML report (`results/sorting_analysis.html`) embedding the SVG plot, structured benchmark metrics table, and theoretical vs empirical complexity analysis.

#### Scenario: Generating HTML summary report
- **WHEN** the benchmark execution concludes
- **THEN** a responsive HTML report styled in modern dark mode is saved to `results/sorting_analysis.html`

### Requirement: Script Integration
The system SHALL integrate benchmark execution, tabular output, and visualization generation within `problem2_sorting.py`, producing all visual and tabular artifacts upon running the script.

#### Scenario: Executing problem2_sorting.py directly
- **WHEN** `problem2_sorting.py` is executed from the terminal
- **THEN** it prints formatted console tables and theoretical analysis, and saves the SVG plot and HTML report to the `results/` directory
