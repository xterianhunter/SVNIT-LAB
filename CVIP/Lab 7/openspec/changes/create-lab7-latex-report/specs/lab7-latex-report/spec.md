## Purpose

Generates a complete, styled LaTeX lab report for CVIP Lab Assignment 7 with embedded code listings, numerical output blocks, high-resolution figures, and concise analytical observations.

## ADDED Requirements

### Requirement: Institutional Header and Document Formatting
The system SHALL generate a LaTeX document complying with the exact preamble provided by the user, including 12pt document font, `fancyhdr` headers with student information (Name: Kishan Sahu, Enrollment No.: P26DS017), department banner for SVNIT Surat, and custom `listings` styles for `code` and `output`.

#### Scenario: Document layout and header verification
- **WHEN** the LaTeX document is inspected or compiled
- **THEN** the header displays "Name: Kishan Sahu" on the left and "Enrollment No.: P26DS017" on the right, with "Lab Assignment 7 - Radiometry and Image Formation" in the title block

### Requirement: Problem Coverage and Structural Flow
The report SHALL document all required lab tasks, specifically Part A (Questions 1, 2, 3, 6, 7) and Part B (Direct Illumination vs. Shadow analysis), while explicitly omitting Questions 4 and 5.

#### Scenario: Checking question sections in report
- **WHEN** the document structure is evaluated
- **THEN** sections exist for Part A Q1, Q2, Q3, Q6, Q7, and Part B with corresponding mathematical models and principles

### Requirement: Code Listings, Outputs, Figures, and Observations Integration
The report SHALL include for every documented problem: the Python code snippet using `\lstdefinestyle{code}`, the textual or statistical output in `\lstdefinestyle{output}`, the generated graphical plot using `\includegraphics`, and a concise analytical observation.

#### Scenario: Visual and textual content completeness
- **WHEN** reviewing any problem section within the LaTeX report
- **THEN** the section contains a code listing, corresponding figure or tabular output, and a concise summary observation explaining the radiometric behavior
