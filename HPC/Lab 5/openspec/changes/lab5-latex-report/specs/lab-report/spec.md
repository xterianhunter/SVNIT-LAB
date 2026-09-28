## Purpose

Defines the structure, mathematical descriptions, source code listings, and benchmark results required for the High Performance Computing Lab 5 LaTeX report.

## ADDED Requirements

### Requirement: Document Header and Academic Metadata
The report SHALL format the document header with SVNIT CSE departmental details, student name "Kishan Sahu", enrollment number "P26DS017", course "High Performance Computing (CSDS125)", and title "Lab Assignment 5: Parallel Genetic Algorithm and PSO for Task Allocation using OpenMP".

#### Scenario: Header verification
- **WHEN** the LaTeX document is compiled
- **THEN** the header displays the student details and SVNIT course title conforming to the 12pt A4 geometry template

### Requirement: Problem Statement and Mathematical Formulation
The report SHALL include the mathematical formulation of the Task Allocation Problem, including task execution matrix $X[M][P]$, communication cost matrix $C[M][M]$, and the conditional inter-processor communication penalty.

#### Scenario: Ground truth sample problem presentation
- **WHEN** reading the problem formulation section
- **THEN** the report details the sample 6-task 2-processor instance, verifying serial assignment cost = 58 and optimal assignment cost = 38

### Requirement: Code and Benchmark Output Listings
The report SHALL include the C implementation code formatted with syntax highlighting (`lstdefinestyle{code}`) and execution output logs (`lstdefinestyle{output}`) presenting execution times, speedup, and solution quality across algorithms.

#### Scenario: Performance comparison table
- **WHEN** viewing the experimental results
- **THEN** a table compares Sequential GA, Parallel GA, Sequential PSO, and Parallel PSO showing execution times, speedup factors, and cost reductions
