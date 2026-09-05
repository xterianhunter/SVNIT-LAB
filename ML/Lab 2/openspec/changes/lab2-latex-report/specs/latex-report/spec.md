## Purpose

Generates a standalone, publication-quality LaTeX report (`lab2.tex`) that presents the complete machine learning sentiment classification pipeline from `assignment_2_naive_bayes.ipynb`, conforming to the exact visual style, header configuration, typography, listings definitions, and layout established in `main.tex`.

## ADDED Requirements

### Requirement: Academic Layout and Header Formatting Matching main.tex
The LaTeX document SHALL use the `article` class with 12pt Times typography via `newtxtext` and `newtxmath`, 1-inch margins on A4 paper, customized `fancyhdr` running headers containing the student's name (`Kishan Sahu`) and enrollment number (`P26DS017`), and a formal institutional header for the Computer Science and Engineering Department, SVNIT Surat for Lab Assignment 2.

#### Scenario: Verify header and page geometry
- **WHEN** the document is compiled to PDF
- **THEN** the first page displays the department and course title block, and subsequent pages carry the running student header and horizontal rule matching `main.tex`.

### Requirement: Code and Output Listing Environments
The LaTeX document SHALL define and utilize `\lstdefinestyle{code}` for Python source code listings and `\lstdefinestyle{output}` for text execution outputs, providing proper font scaling, bounding frames, line breaking, and syntax coloring.

#### Scenario: Code and output rendering
- **WHEN** source code or console outputs from any notebook task are presented
- **THEN** code blocks use `[style=code]` with syntax highlighting and line numbers, and output blocks use `[style=output]` with a shaded background and no line numbers.

### Requirement: Figure and Chart Visualization Inclusion
The LaTeX document SHALL embed all key graphical outputs produced during notebook execution as high-resolution PNG figures with numbered captions and float alignment.

#### Scenario: Visualizations included in document
- **WHEN** the LaTeX document is rendered
- **THEN** it displays the document length distribution plot, confusion matrices for both classifiers, performance comparison bar charts, and the smoothing hyperparameter curve from local figure assets.

### Requirement: Comprehensive Notebook Task Coverage
The LaTeX document SHALL incorporate all 7 core assignment tasks and the comprehensive final report from `assignment_2_naive_bayes.ipynb` without omission, including:
1. Dataset exploration and class distributions
2. Preprocessing pipeline implementation and comparative stats
3. Feature extraction (BoW count and binary representations)
4. Multinomial and Bernoulli Naive Bayes model training and evaluation
5. Comparative model performance analysis
6. Laplace/Lidstone smoothing hyperparameter analysis
7. In-depth misclassification and error diagnostics (10+ review samples)
8. Final conclusions and summary recommendations

#### Scenario: All 7 tasks and report present
- **WHEN** the document is read from beginning to end
- **THEN** all tasks 1 through 7 and the synthesis conclusion are fully documented with corresponding code, outputs, figures, and textual analyses.

### Requirement: Error-Free LaTeX Compilation
The LaTeX document `lab2.tex` and its associated figure assets SHALL be self-contained and compile cleanly to a PDF via standard LaTeX tools (`pdflatex` / `latexmk`).

#### Scenario: Successful PDF compilation
- **WHEN** `pdflatex -interaction=nonstopmode lab2.tex` is executed
- **THEN** a complete, valid `lab2.pdf` is generated without unhandled errors or missing figure references.
