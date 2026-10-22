## Purpose

Provides automated generation and compilation of a complete LaTeX report for CVIP Lab Assignment 5 containing all code, outputs, figures, comparison tables, and analytical observations.

## ADDED Requirements

### Requirement: Exact header and preamble formatting
The LaTeX source file `report.tex` SHALL adopt the exact user-specified LaTeX preamble, document geometry, Times-style font packages, listing definitions (`code` and `output`), parindent/parskip parameters, and fancyhdr configuration containing student Name "Kishan Sahu", Enrollment Number "P26DS017", and Lab Assignment 5 title.

#### Scenario: Preamble and header validation
- **WHEN** the LaTeX document `report.tex` is inspected
- **THEN** the preamble and header match the specified styling and student details exactly.

### Requirement: Full lab content coverage and figure embedding
The report SHALL include complete problem descriptions, theoretical mathematical equations, Python code listings, terminal execution logs, high-resolution figures extracted from `lab5_solution.ipynb`, comparison summary tables, and comprehensive observations for all tasks in Part A and Part B.

#### Scenario: Visual and textual completeness across all sections
- **WHEN** the compiled document is generated
- **THEN** it contains separate structured subsections for Spatial Filtering, 2D DFT, ILPF, IHPF, GLPF, GHPF, BLPF, BHPF, and Multi-scale Cross-Correlation Template Matching with all accompanying figures and comparison tables.

### Requirement: Error-free compilation to PDF
The LaTeX document SHALL compile cleanly using `pdflatex` into a PDF document (`report.pdf`) without undefined references or missing figure errors.

#### Scenario: Compiling report to PDF
- **WHEN** `pdflatex report.tex` is executed
- **THEN** the command exits with return code 0 and produces `report.pdf`.
