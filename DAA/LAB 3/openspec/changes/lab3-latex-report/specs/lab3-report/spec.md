## Purpose

Generates a complete, publication-quality LaTeX document (`Lab3.tex`) and associated execution time graph figures for Lab Assignment 3, adhering strictly to the typography, layout, header metadata, algorithm pseudocode, code listings, and margin-safe formatting of `main.tex`.

## ADDED Requirements

### Requirement: Document Layout, Metadata, and Styling
The system SHALL produce `Lab3.tex` matching the visual layout, 1-inch margins, 12pt Times font, fancy header (Name: Kishan Sahu, Enrollment No.: P26DS017), title banner, algorithm styling, and listing styles (`code` and `output`) defined in `main.tex`.

#### Scenario: Header and preamble matching
- **WHEN** inspecting `Lab3.tex`
- **THEN** the preamble and header block reflect the standard student metadata and Lab Assignment 3 header

### Requirement: Problem 1 (Coin Change) Coverage
The system SHALL include in `Lab3.tex` the complete solution for Problem 1, comprising DP state formulation, algorithm pseudocode (`CoinChangeDP`), Python code listing, executed output block, margin-safe complexity comparison table, embedded execution time plot figure (`plot_coin_change.png`), and detailed analysis on the greedy strategy counterexample.

#### Scenario: Problem 1 completeness
- **WHEN** inspecting the Problem 1 section of `Lab3.tex`
- **THEN** all 4 required points, the PDF example $\{1, 3, 4\}$ with amount $6$, combination reconstruction, execution time plots, and greedy counterexample analysis are fully present

### Requirement: Problem 2 (Employee Training Planning) Coverage
The system SHALL include in `Lab3.tex` the complete solution for Problem 2, comprising 0/1 Knapsack formulation, algorithm pseudocode (`EmployeeTrainingDP`), Python code listing, executed output block on the PDF dataset ($M_1, M_2, M_3, M_4$), margin-safe complexity table, embedded execution time scaling plot figure (`plot_employee_training.png`), and detailed analysis on the unbounded module repetition modification.

#### Scenario: Problem 2 completeness
- **WHEN** inspecting the Problem 2 section of `Lab3.tex`
- **THEN** all 4 required points, module reconstruction for budget $B=10$, execution time scaling plots, and unbounded recurrence analysis are fully present

### Requirement: Margin Safety and Successful Compilation
The system SHALL ensure that all tables use bounded column widths (`p{...}` or `tabularx`) to prevent margin overflows, and generate clean graph PNGs that compile error-free with `pdflatex`.

#### Scenario: Compile Lab3.tex to PDF
- **WHEN** compiling `Lab3.tex` with `pdflatex`
- **THEN** `Lab3.pdf` compiles with 0 errors and no table margin overflows
