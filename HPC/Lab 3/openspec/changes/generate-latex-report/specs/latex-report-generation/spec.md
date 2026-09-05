## Purpose

Specifies the requirements for generating a comprehensive LaTeX lab report document for OpenMP parallel linear regression, matching the user's styling, metadata, and technical contents.

## ADDED Requirements

### Requirement: Document Preamble and Header Compliance
The report SHALL adhere strictly to the user-specified LaTeX preamble, font packages, geometry margins, custom `listings` styles, running headers with author credentials (Kishan Sahu, P26DS017), and department title block.

#### Scenario: Verify header and styling compliance
- **WHEN** the LaTeX file is parsed or compiled
- **THEN** it contains the requested packages, margins, 12pt document font sizing, custom listing styles, and headers displaying author and department details.

### Requirement: Technical Content and Formulation
The report SHALL include the problem statement, mathematical derivation of batch gradient descent for 3D dataspace ($x_1, x_2, y$), OpenMP parallelization strategy using reductions, full code listing of `linear_regression_omp.c`, execution terminal output, and a comparative performance table showing runtime and speedup.

#### Scenario: Verify comprehensive technical sections
- **WHEN** reviewing the document sections
- **THEN** the report includes Problem Statement, Mathematical Formulation, Parallel Algorithm & OpenMP Strategy, Source Code Listing, Experimental Results Table, Execution Output, and Analysis of Parallel Performance.
