## Context

`Lab 1/sentiment_analysis.ipynb` had all cells deleted and is currently an empty file. The complete source code, markdown titles, and key analytical takeaways are preserved across 20 code listings in `Lab 1/machine_learning_lab.pdf`.

Text extracted from the PDF contains typesetting artifacts, including:
- Separate line numbers interleaved between code statements
- Page headers and footers (e.g., student name, roll number, page break `\x0c`)
- Typographic/smart quotes (`’`, `‘`, `“`, `”`) and en-dashes instead of standard ASCII code characters

## Goals / Non-Goals

**Goals:**
- Faithfully reconstruct all 20 code listings across Part 1 (20 Newsgroups) and Part 2 (California Housing) into `Lab 1/sentiment_analysis.ipynb`.
- Structure the notebook with clear Markdown headers for parts and sections, matching the PDF outline.
- Restore the two comprehensive "Key Insights and Analysis" sections (Section 11 of Part 1 and Section 11 of Part 2) as rich Markdown cells.
- Clean all line numbers, headers, footers, and typographical characters so every code cell is syntactically valid Python.
- Validate the generated notebook using `json.loads` and Python AST parsing.

**Non-Goals:**
- Modifying or altering the code logic from what was documented in `machine_learning_lab.pdf`.
- Renaming the notebook file or executing heavy training runs outside of notebook validation.
- Creating code for datasets or tasks not present in the PDF.

## Decisions

### 1. Programmatic Extraction & Notebook Assembly via Python Script
- **Decision**: Use a Python utility script utilizing `pdftotext` to extract, segment, clean, and write cells into standard Jupyter notebook format v4.
- **Alternatives considered**:
  - *Manual copy-paste*: Prone to manual typos, missed listings, and indentation errors across 2,400+ lines of PDF text.
  - *Automated PDF parser*: Ensures deterministic extraction, automated stripping of line numbers and page headers, and automated AST validation.

### 2. Notebook Structure & Cell Organization
- **Decision**: Organize the notebook hierarchically:
  - Title and student metadata (Markdown)
  - Part 1: Header + 10 Section headers (Markdown), 10 Code cells (Listings 1-10), and Section 11 Key Insights (Markdown)
  - Part 2: Header + 10 Section headers (Markdown), 10 Code cells (Listings 11-20), and Section 11 Key Insights (Markdown)
- **Alternatives considered**: Putting all listings into one massive cell (poor readability and violates standard notebook practice).

### 3. Sanitization Pipeline
- **Decision**: Implement a multi-stage cleaning pipeline:
  1. Segment text into listings delimited by `Listing X:` and `Output:`.
  2. Strip page breaks (`\x0c`), repeated student headers (`Name: Kishan Sahu`, `Roll No.: P26DS017`).
  3. Strip standalone line numbers emitted by LaTeX listing environments.
  4. Replace curly single/double quotes with ASCII `'` and `"`.
  5. Validate each code cell with `ast.parse` to guarantee syntactical correctness before writing to `Lab 1/sentiment_analysis.ipynb`.

## Risks / Trade-offs

- **[Risk]** Indentation corruption during text extraction across line wraps or page boundaries.
  → **Mitigation**: Verify AST compilation for every code cell; inspect and format multi-line docstrings and loops carefully.
- **[Risk]** Local directory paths in code (e.g. `20_newsgroups` folder path).
  → **Mitigation**: Preserve the exact path parameters documented in the PDF while noting dataset dependencies in documentation.
