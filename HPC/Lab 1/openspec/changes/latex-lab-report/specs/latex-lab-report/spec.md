## Purpose

Defines the structure, required content, formatting, and analysis for a standardized LaTeX lab report covering Lab 1.

## ADDED Requirements

### Requirement: Document Header and Preamble Configuration
The document SHALL contain the exact geometry, fonts (`newtxtext,newtxmath`), listing styles (`code` and `output`), student information (Name: Kishan Sahu, Enrollment No.: P26DS017), and institutional department title block provided by the user.

#### Scenario: Verify header and styles
- **WHEN** the document preamble and header are rendered
- **THEN** the student details and SVNIT header block appear with the required formatting and styling

### Requirement: Inclusion of All Four Lab 1 Programs
The document SHALL contain distinct sections for each of the four lab programs:
1. Minimum and Maximum in an Array
2. Matrix Multiplication
3. Vector Dot Product
4. Divide-and-Conquer Merge Sort

Each section SHALL include problem objective, complete source code in the `code` listing environment, sample execution output in the `output` listing environment, and a concise algorithmic analysis.

#### Scenario: Presence of all 4 lab exercises
- **WHEN** the document sections are inspected
- **THEN** all four programs are represented with code, output, and analysis

### Requirement: Algorithmic and Complexity Analysis
The document SHALL provide a concise theoretical analysis for each program, covering time complexity, auxiliary space complexity, and dynamic memory allocation characteristics.

#### Scenario: Comprehensive short analysis
- **WHEN** the analysis subsection is reviewed for any program
- **THEN** time complexity, space complexity, and memory management aspects are explicitly documented
