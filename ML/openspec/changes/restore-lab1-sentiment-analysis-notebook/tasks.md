## 1. Extraction and Parsing Setup

- [x] 1.1 Create an extraction and cleaning script to extract all 20 code listings and 2 analytical insight sections from `Lab 1/machine_learning_lab.pdf`, stripping line numbers, page breaks, student metadata headers, and normalizing typographic quotes. Verify extracted code fragments with `ast.parse`.

## 2. Notebook Reconstruction

- [x] 2.1 Assemble Part 1 cells (20 Newsgroups Dataset): title markdown, section headings, code cells for Listings 1 through 10, and Section 11 Key Insights markdown block.
- [x] 2.2 Assemble Part 2 cells (California Housing Dataset): section headings, code cells for Listings 11 through 20, and Section 11 Key Insights markdown block.
- [x] 2.3 Generate the complete notebook file at `Lab 1/sentiment_analysis.ipynb` conforming to Jupyter Notebook format v4 with proper cell structure and metadata.

## 3. Verification

- [x] 3.1 Validate `Lab 1/sentiment_analysis.ipynb` by verifying JSON structure (`nbformat: 4`, `nbformat_minor: 2`) and compiling every code cell through Python's `ast.parse` to ensure zero syntax errors.
