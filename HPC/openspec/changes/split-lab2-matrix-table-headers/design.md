## Context

`Lab2.tex` contains three empirical performance comparison tables in the Problem Statement 3 analysis section for matrix dimensions $500 \times 500$, $1000 \times 1000$, and $1500 \times 1500$. The table format is standard `booktabs` with centered columns (`cccccc`). The current single-line headers for "Decomposition Method" and "Throughput (GFLOPS)" cause the table bounding box to approach or exceed the margins. See `proposal.md` for background and `specs/lab-report-formatting/spec.md` for requirements.

## Goals / Non-Goals

**Goals:**
- Break column headers "Decomposition Method" and "Throughput (GFLOPS)" into two distinct vertically stacked lines across all three benchmark tables in `Lab2.tex`.
- Keep column alignment (`cccccc`) and typography (`\textbf{...}`) consistent.
- Ensure 100% clean compilation via `pdflatex` with zero syntax errors or font/layout regressions.

**Non-Goals:**
- Modifying C source code or benchmark numerical results.
- Changing other sections or tables in other documents.

## Decisions

### Decision 1: LaTeX Multi-Line Header Method
- **Chosen Option**: Use `\shortstack[c]{...}` (or `\makecell{...}` / stacked sub-tabular) within the table header row.
  - `\shortstack[c]{\textbf{Decomposition}\\\textbf{Method}}`
  - `\shortstack[c]{\textbf{Throughput}\\\textbf{(GFLOPS)}}`
- **Rationale**: `\shortstack` is a built-in LaTeX primitive that operates within standard tabular environments without requiring external package changes, maintaining exact horizontal center alignment with the data rows underneath.
- **Alternatives Considered**:
  - Two explicit `tabular` header rows: Adds blank cells for the other single-line headers or requires `\multirow`, complicating alignment.
  - Adding `\usepackage{makecell}`: Valid option, but `\shortstack` avoids adding extra package dependencies while achieving the identical visual rendering.

### Decision 2: Consistency across all benchmark tables
- Apply the header splitting uniformly across Table 1 ($500 \times 500$), Table 2 ($1000 \times 1000$), and Table 3 ($1500 \times 1500$) for uniform visual presentation.

## Risks / Trade-offs

- [Vertical Spacing in Header] → `\shortstack` respects baseline heights; adding small baseline strut or standard `\addlinespace` if needed ensures proper breathing room above `\midrule`.
