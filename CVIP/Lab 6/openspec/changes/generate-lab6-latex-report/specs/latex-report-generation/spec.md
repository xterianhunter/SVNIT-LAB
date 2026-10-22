## Purpose

Generates a publication-quality LaTeX laboratory report for CVIP Lab Assignment 6 embedding all codes, outputs, figures, and comparative observations.

## ADDED Requirements

### Requirement: Preamble and Document Header Conformance
The LaTeX report SHALL strictly adhere to the user's provided document layout, package list, 12pt font settings, header specifications (Name: Kishan Sahu, Enrollment No.: P26DS017), and department title formatting for Lab Assignment 6 (Image Segmentation).

#### Scenario: Inspecting document header
- **WHEN** the LaTeX document is compiled or viewed
- **THEN** the top header SHALL display "Name: Kishan Sahu" and "Enrollment No.: P26DS017", and the center title SHALL read "Lab Assignment 6: Image Segmentation".

### Requirement: Image Asset Extraction
The system SHALL extract all generated visual output plots from `lab6_image_segmentation.ipynb` into a dedicated `figures/` folder as standalone PNG files.

#### Scenario: Extracting figures
- **WHEN** the extraction routine runs
- **THEN** high-resolution PNG images for the original input, point/line detection, edge detection operators, thresholding comparisons, region growing sensitivity, and Part B object retention/disappearance SHALL be present in `figures/`.

### Requirement: Complete Source Code and Verbatim Output Listings
The LaTeX report SHALL format all Python source code using `lstlisting[style=code]` and verbatim execution outputs using `lstlisting[style=output]`.

#### Scenario: Formatting code and output blocks
- **WHEN** code blocks are rendered in the LaTeX document
- **THEN** each cell's implementation from `lab6_image_segmentation.ipynb` SHALL be enclosed in `style=code`, and associated terminal printouts SHALL be enclosed in `style=output`.

### Requirement: Part A and Part B Structured Presentation
The LaTeX report SHALL organize the experimental writeup into clearly defined sections covering Part A (Point/Line detection, Edge operators, Global vs. Otsu thresholding, Region growing) and Part B (Single-technique failure analysis, Black cup composite pipeline, Object retention, and Object disappearance).

#### Scenario: Reviewing report sections
- **WHEN** the document structure is evaluated
- **THEN** both Part A and Part B SHALL include theoretical mathematical formulations, code listings, embedded visual figures, and analytical observations.
