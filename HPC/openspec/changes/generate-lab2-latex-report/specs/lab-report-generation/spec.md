## Purpose

Generates a complete LaTeX laboratory report document `Lab2.tex` replicating the visual styling, typography, headers, listing environments, terminal execution outputs, and benchmark comparison tables from `main.tex` for the three OpenMP experiments.

## ADDED Requirements

### Requirement: Document Layout and Header Formatting
The system SHALL format `Lab2.tex` matching the document structure, geometry (A4, 1-inch margins), 12pt Times typography (`newtxtext,newtxmath`), header rules (`Name: Kishan Sahu`, `Enrollment No.: P26DS017`), title block (Department of CSE, SVNIT Surat, M.Tech I, HPC Lab Assignment 2), and paragraph spacing as defined in `main.tex`.

#### Scenario: Visual layout and header parity
- **WHEN** `Lab2.tex` is rendered
- **THEN** it SHALL display the header with student credentials, department title block for Lab Assignment 2, and exact margin and font properties matching `main.tex`

### Requirement: Code Listings and Execution Outputs
The system SHALL present source code listings and terminal execution logs for all three OpenMP problems using the `lstlisting` styles (`style=code` adapted for C language with syntax highlighting and `style=output` with light background).

#### Scenario: Problem Statement 1 presentation
- **WHEN** Problem Statement 1 is viewed in `Lab2.tex`
- **THEN** it SHALL contain the problem description, complete C source code for `race_condition.c`, terminal output demonstrating lost updates, and theoretical race condition analysis

#### Scenario: Problem Statement 2 presentation
- **WHEN** Problem Statement 2 is viewed in `Lab2.tex`
- **THEN** it SHALL contain the problem description, complete C source code for `critical_section.c`, verified terminal output with zero errors, and mutual exclusion analysis

#### Scenario: Problem Statement 3 presentation
- **WHEN** Problem Statement 3 is viewed in `Lab2.tex`
- **THEN** it SHALL contain the problem description, complete C source code for `matrix_mult.c`, terminal execution output, empirical performance benchmark tables across thread counts, and in-depth analysis of coarse-grained vs. fine-grained data decomposition

### Requirement: Empirical Benchmark Tables in Analysis
The system SHALL include formatted LaTeX tables displaying execution time, GFLOPS, speedup, and parallel efficiency across matrix sizes ($N = 500, 1000, 1500$) and thread counts ($T \in \{1, 2, 4, 8\}$) within the analysis of Problem Statement 3.

#### Scenario: Benchmark table inclusion
- **WHEN** the analysis for Problem Statement 3 is rendered
- **THEN** it SHALL include structured tabular data comparing sequential, coarse-grained, and fine-grained matrix multiplication performance

### Requirement: Exclusion of Algorithm Blocks
The system SHALL NOT include pseudo-code algorithm environments (`\begin{algorithm}...\end{algorithm}`) in `Lab2.tex`.

#### Scenario: Absence of algorithm environment
- **WHEN** `Lab2.tex` is inspected or compiled
- **THEN** no `algorithm` or `algpseudocode` environment blocks SHALL be present in the document

### Requirement: Successful PDF Compilation
The system SHALL successfully compile `Lab2.tex` to `Lab2.pdf` using `pdflatex` without syntax errors or missing package dependencies.

#### Scenario: Compilation via pdflatex
- **WHEN** `pdflatex Lab2.tex` is executed
- **THEN** the compilation SHALL exit with status code 0 and produce `Lab2.pdf`
