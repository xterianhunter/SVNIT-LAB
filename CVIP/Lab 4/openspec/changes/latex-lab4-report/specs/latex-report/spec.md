## Purpose

Provides a standalone, publication-ready LaTeX lab report document compiling all Python implementations, outputs, figures, comparative tables, and empirical analysis from CVIP Lab 4 into a professionally formatted document matching the required departmental style and header specifications.

## ADDED Requirements

### Requirement: Departmental Header and Preamble Formatting
The LaTeX report SHALL conform strictly to the specified preamble and departmental header template, incorporating the 12pt article document class, 1-inch margins, Times-style font, custom `listings` styles (`code` and `output`), student identification metadata, and institutional title block.

#### Scenario: Header and Preamble Compliance
- **WHEN** the document is compiled with LaTeX
- **THEN** it produces pages with margins of 1 inch, fancy header containing student Name ("Kishan Sahu") and Enrollment No. ("P26DS017"), 12pt text size, and the SVNIT Computer Science and Engineering Department title block.

### Requirement: Full Reproduction of Notebook Content
The LaTeX document SHALL incorporate all content from `cvip_lab4.ipynb`, including problem formulation, algorithm implementations, console execution outputs, image plots, parameter comparisons, and observations.

#### Scenario: Complete Lab Content Inclusion
- **WHEN** the LaTeX source is rendered
- **THEN** it contains the complete Python code for noise addition and all 6 order-statistic filters (Median, Min, Max, Midpoint, Alpha-Trimmed Mean, Percentile), verbatim console output streams, and detailed analysis text.

### Requirement: High-Resolution Embedded Visualizations
The report SHALL include extracted high-resolution figure assets representing the visual comparisons generated in the notebook.

#### Scenario: Visual Comparison Figures
- **WHEN** the document compiles
- **THEN** it embeds figures for (1) original vs noisy inputs, (2) comparison of all 7 filter variations on Salt & Pepper noise, (3) neighborhood size progression ($3 \times 3, 5 \times 5, 7 \times 7$), and (4) Gaussian noise filtering comparisons using centered figure floats and descriptive captions.

### Requirement: Comparative Summary Table
The LaTeX report SHALL provide a formatted comparative table summarizing each statistical filter's mathematical definition, rank selection formula, computational complexity, optimal noise type, and edge preservation properties.

#### Scenario: Tabular Comparison Presentation
- **WHEN** the document is reviewed
- **THEN** it presents a clear comparative table contrasting Median, Min, Max, Midpoint, Alpha-Trimmed Mean, and Percentile filters across noise robustness, edge retention, and boundary handling metrics.

### Requirement: Clean PDF Compilation
The generated LaTeX file SHALL compile cleanly without errors or missing figure warnings.

#### Scenario: Successful Compilation
- **WHEN** compiled using `pdflatex`
- **THEN** the compilation exits with status code 0 and outputs `cvip_lab4_report.pdf`.
