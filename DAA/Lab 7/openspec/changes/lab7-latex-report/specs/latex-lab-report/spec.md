## Purpose

Defines requirements for generating a complete, publication-quality LaTeX report documenting Lab Assignment 7 (String Matching Algorithms) with student credentials, problem formulations, algorithms, execution traces, collision analyses, and benchmark figures.

## ADDED Requirements

### Requirement: Document Structure and Header Format
The document SHALL adhere to the user's specific LaTeX document class, packages, page geometry, typography settings, fancyhdr headers displaying "Name: Kishan Sahu" and "Enrollment No.: P26DS017", and listing styles for code and terminal output.

#### Scenario: Verify LaTeX header and document styling
- **WHEN** the document preamble and header are processed
- **THEN** the exact margins (1in), Times font (newtxtext, newtxmath), 12pt body font, fancyhdr running headers with student name and enrollment number, and lstdefinestyle definitions for code and output are present

### Requirement: Problem 1 Naive String Matching Section
The report SHALL document the Naive String Matching algorithm, time complexities ($O(n)$ best case, $O((n-m+1)m)$ worst case), space complexity ($O(1)$), complete Python code listing, terminal output on sample text "AABAACAADAABAABA", and worst-case analysis with theoretical versus actual comparisons and explanation.

#### Scenario: Complete Problem 1 presentation
- **WHEN** inspecting Problem 1 in the LaTeX report
- **THEN** the mathematical formulation, full Python source in code style, actual terminal output in output style, and worst-case comparison verification are rendered

### Requirement: Problem 2 KMP String Matching Section
The report SHALL document the Knuth–Morris–Pratt algorithm, the LPS array definition and construction, time complexity ($O(n+m)$), space complexity ($O(m)$), complete Python code for LPS and KMP search, terminal execution outputs, and character comparison reduction compared to Naive.

#### Scenario: Complete Problem 2 presentation
- **WHEN** inspecting Problem 2 in the LaTeX report
- **THEN** the LPS computation trace for "ABABCABAB", search results, and comparison comparison table/text are rendered

### Requirement: Problem 3 Rabin-Karp String Matching Section
The report SHALL document the Rabin-Karp algorithm, polynomial rolling hash mechanism, rolling update formula ($O(1)$), average ($O(n+m)$) and worst-case ($O(nm)$) complexities, complete Python code, terminal output, deliberate hash collision demonstration (e.g., 'AAB' and 'BEA'), and discussion of hash parameter effects.

#### Scenario: Complete Problem 3 presentation
- **WHEN** inspecting Problem 3 in the LaTeX report
- **THEN** mathematical hash equations, code listing, verification counters, and spurious hit collision analysis are rendered

### Requirement: Problem 4 Benchmarking, Visualizations and Summary Table
The report SHALL include experimental methodology, three embedded plots (Input Size vs Execution Time, Pattern Length vs Execution Time, Input Size vs Number of Comparisons), and a comprehensive summary table comparing all three algorithms.

#### Scenario: Visualizations and summary table inclusion
- **WHEN** inspecting Problem 4 in the LaTeX report
- **THEN** figures referencing generated plot images and the complete comparison table are properly formatted and placed in the document
