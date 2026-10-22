## Purpose

Defines the structure, required content, formatting specifications, and validation criteria for the OpenMP Parallel Sorting Lab 4 LaTeX report document and associated benchmarks.

## ADDED Requirements

### Requirement: Document Header and Preamble Compliance
The report SHALL strictly adopt the user-specified LaTeX document class, packages (`geometry`, `amsmath`, `amssymb`, `newtxtext`, `newtxmath`, `fancyhdr`, `listings`, `xcolor`, `graphicx`, `float`, `algorithm`, `algpseudocode`, `booktabs`), custom listings styles (`code` and `output`), running headers with student identity (`Kishan Sahu`, `P26DS017`), and official departmental header block.

#### Scenario: Verify preamble and running header format
- **WHEN** the LaTeX document is compiled or inspected
- **THEN** it contains the specified 12pt article class, custom listings styles, fancyhdr headers with student name and enrollment number, and department title banner.

### Requirement: Inclusion of Specified Source Codes
The document SHALL include full C language source code listings formatted using the `code` listing style for exactly the three specified programs: `parallel_merger_sort.c`, `parallel_quick_sort.c`, and `quicksort_depth.c`.

#### Scenario: Code listings presentation
- **WHEN** viewing the source code sections of the document
- **THEN** all three programs are displayed in distinct labeled listings with line numbers and syntax highlighting without omissions.

### Requirement: Execution Outputs Presentation
The document SHALL display verbatim terminal execution outputs for each of the three programs formatted using the gray-background `output` listing style.

#### Scenario: Execution output rendering
- **WHEN** inspecting the output blocks for merge sort, unconstrained quicksort, and depth-limited quicksort
- **THEN** the console outputs accurately reflect the runtime measurements, thread counts, problem sizes, and calculated speedup/efficiency metrics.

### Requirement: Performance Benchmarks and Analysis Tables
The document SHALL present structured comparison tables summarizing empirical performance across sequential execution, parallel execution, thread scaling, and recursion cutoff depths.

#### Scenario: Performance analysis and comparison
- **WHEN** evaluating the benchmark tables in the document
- **THEN** execution times, speedup ratios, and parallel efficiency metrics for merge sort, unconstrained quicksort, and depth-limited quicksort are systematically contrasted.

### Requirement: Comparative Analysis of Parallel Sorting Strategies
The document SHALL provide detailed technical commentary explaining why sections-based merge sort achieves speedup, why unconstrained task creation in quicksort degrades performance due to task queue and scheduling overhead, and how recursion depth cutoff with sequential base-case switching restores scalability.

#### Scenario: Architectural and runtime analysis validation
- **WHEN** reviewing the analysis and discussion sections of the report
- **THEN** theoretical complexity, OpenMP runtime task scheduling overhead, depth limits, and Amdahl's law considerations are thoroughly addressed.
