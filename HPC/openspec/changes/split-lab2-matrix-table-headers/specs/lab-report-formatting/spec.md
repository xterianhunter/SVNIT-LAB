## Purpose

Defines table layout and multi-line column header formatting specifications for LaTeX laboratory benchmark reporting in Lab2.tex.

## ADDED Requirements

### Requirement: Multi-Line Table Headers for Matrix Multiplication Tables
The system SHALL format the empirical benchmark comparison tables for matrix multiplication in `Lab2.tex` using multi-line column headers to reduce column width.

#### Scenario: Decomposition Method header split
- **WHEN** the benchmark tables for matrix sizes $500 \times 500$, $1000 \times 1000$, and $1500 \times 1500$ are rendered
- **THEN** the decomposition method column header SHALL display "Decomposition" on the first line and "Method" on the second line

#### Scenario: Throughput header split
- **WHEN** the benchmark tables for matrix sizes $500 \times 500$, $1000 \times 1000$, and $1500 \times 1500$ are rendered
- **THEN** the throughput column header SHALL display "Throughput" on the first line and "(GFLOPS)" on the second line

### Requirement: Document Layout and Margin Compliance
The system SHALL ensure that all three matrix multiplication performance comparison tables remain fully within the document text margins and compile cleanly via `pdflatex`.

#### Scenario: Clean PDF compilation
- **WHEN** `pdflatex Lab2.tex` is executed
- **THEN** the compilation SHALL exit with code 0 and produce `Lab2.pdf` without margin overflow warnings
