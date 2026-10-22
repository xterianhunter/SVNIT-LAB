## Purpose

Defines requirements for generating a formatted academic LaTeX report representing the digital image processing lab, incorporating source code listings, terminal execution outputs, figure assets, and theoretical question answers.

## ADDED Requirements

### Requirement: Exact LaTeX Template and Metadata Adherence
The document SHALL adhere to the user's provided LaTeX configuration, including `\documentclass[12pt]{article}`, 1-inch margins, Times-style typography (`newtxtext`, `newtxmath`), fancy headers with `Name: Kishan Sahu` and `Enrollment No.: P26DS017`, and custom listings styles.

#### Scenario: Compiling document header and preamble
- **WHEN** the LaTeX document is inspected or compiled
- **THEN** it MUST contain the exact specified packages, header rules, parindent/parskip parameters, and font configurations.

### Requirement: Code and Output Environment Styling
The report SHALL format Python source code blocks using `\begin{lstlisting}[style=code]` and program outputs using `\begin{lstlisting}[style=output]`.

#### Scenario: Code listing formatting
- **WHEN** a code block or program output is rendered in the report
- **THEN** it MUST use the corresponding `lstlisting` style (`code` or `output`) specified in the template.

### Requirement: Complete Lab Curriculum Coverage
The report SHALL contain all 14 parts of the lab in sequence, including problem explanations, mathematical equations (negative, brightness, thresholding, order statistics), and answers to all "Think", "Investigation", and "Critical Thinking" questions.

#### Scenario: Verification of lab content
- **WHEN** the document content is reviewed across Parts 1 through 14
- **THEN** all instructional prompts, code implementations, theoretical explanations, and reflection answers MUST be fully present without omissions.

### Requirement: Visual Figure and Table Integration
The report SHALL reference and embed all generated lab plot figures using `figure` environments with `\includegraphics` pointing to exported image files in a `figures/` directory, and present the order-statistic neighborhood as a LaTeX matrix and summary table.

#### Scenario: Figure and table embedding
- **WHEN** the LaTeX document references visual results
- **THEN** every plot generated across Parts 2, 4, 6, 7, 8, 9, 10, 11, 12, and 13 MUST have a corresponding image file in `figures/` referenced by `\includegraphics`, and Part 14 MUST be displayed as a mathematical matrix and comparative table.
