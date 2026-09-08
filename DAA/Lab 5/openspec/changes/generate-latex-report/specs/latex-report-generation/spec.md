## Purpose

Generates a complete, publication-grade LaTeX lab report for SVNIT CS103 Design and Analysis of Algorithms, incorporating all solutions, code listings, and benchmark tables from the assignments notebook.

## ADDED Requirements

### Requirement: Document Layout and Preamble Adherence
The LaTeX report SHALL strictly incorporate the exact specified document preamble, 1-inch margins, 12pt Times-style typography, `fancyhdr` student headers (`Name: Kishan Sahu`, `Enrollment No.: P26DS017`), title block, and custom `listings` styles (`code` and `output`).

#### Scenario: Preamble and styling match
- **WHEN** the LaTeX document is rendered
- **THEN** it MUST match the layout, font sizing, running headers, and listing color styles specified in the user template.

### Requirement: Inclusion of All Implemented Assignments
The document SHALL contain thorough dedicated sections for all assignments implemented in `daa_assignments_1_to_5.ipynb`:
- Section 1: Introduction to Divide and Conquer.
- Assignment 1: 2D Closest Pair of Points (Brute Force vs Divide and Conquer).
- Assignment 2 & 3: 1,000,000 Positive Integer Dataset, Duplicate Resolution, and Linux Microsecond Timing.
- Assignment 4: Element at Index $i$ in Sorted Order (Heap vs Quickselect vs Sort).
- Assignment 5: Cost of Execution and Asymptotic Loop Analysis for all 4 snippets.
- Assignment 6: Karatsuba Large Integer Multiplication vs Conventional Multiplication.

#### Scenario: Complete assignment coverage
- **WHEN** any assignment from 1 to 6 is inspected in the LaTeX report
- **THEN** it MUST present the problem statement, theoretical time complexity, actual Python code used in the notebook, and empirical experimental results.

### Requirement: Margin-Safe Table Formatting
All tables (including benchmark comparisons and complexity summaries) SHALL be formatted using `booktabs` and constrained column widths so they do not exceed the 1-inch page margins.

#### Scenario: Table width verification
- **WHEN** the LaTeX source is compiled
- **THEN** no table column or rule MUST overflow the text width boundary.

### Requirement: Standard Code and Output Listings
All source code blocks SHALL be encapsulated within `\begin{lstlisting}[style=code]` environments, and empirical terminal execution outputs SHALL be formatted inside `\begin{lstlisting}[style=output]` environments.

#### Scenario: Clean code rendering
- **WHEN** Python code or terminal outputs are displayed
- **THEN** syntax highlighting, line wrapping, and proper font styles MUST render without text clipping.
