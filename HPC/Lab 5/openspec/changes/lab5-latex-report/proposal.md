## Why

A formatted LaTeX report is required for HPC Lab Assignment 5 (CSDS125, CSE Department, SVNIT Surat) documenting the implementation and comparative evaluation of Parallel Genetic Algorithm (GA) and Parallel Particle Swarm Optimization (PSO) for distributed task allocation using OpenMP.

## What Changes

- Create `lab5_report.tex` formatted using the departmental template (M.Tech. I, Semester I, Name: Kishan Sahu, Enrollment: P26DS017).
- Include problem definition, mathematical cost model ($\sum \text{Exec} + \sum \text{Comm}$ across distinct nodes), verification of sample $6 \times 2$ problem (Serial = 58, Optimal = 38).
- Include algorithm summaries for Sequential vs. OpenMP Parallel GA and PSO.
- Embed implementation source code listings and formatted benchmark output with execution times, speedup factors, and cost reductions.

## Capabilities

### New Capabilities
- `lab-report`: Generates the complete LaTeX laboratory report for Lab Assignment 5 incorporating mathematical formulation, C implementation code, and comparative benchmark results.

### Modified Capabilities
<!-- No existing capabilities modified -->

## Impact

- Generates `lab5_report.tex` in the root workspace directory.
- Compilable via `pdflatex lab5_report.tex`.
