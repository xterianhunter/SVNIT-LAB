## Context

See [proposal.md](file:///home/xterianhunter/LABS/HPC/Lab%205/openspec/changes/lab5-latex-report/proposal.md).
The report must present the work conducted in Lab 5: parallelizing Genetic Algorithm and Particle Swarm Optimization for the Task Allocation Problem (TAP) in distributed systems using OpenMP.

## Goals / Non-Goals

**Goals:**
- Adhere strictly to the requested 12pt A4 geometry and header template with SVNIT Surat course and student details.
- Provide clear mathematical formulation of execution costs and cross-node communication penalties.
- Include verification against the sample 6-task, 2-node problem from the problem specification.
- Present the core C implementation using `\begin{lstlisting}[style=code]`.
- Present actual benchmark output from the terminal and a clean summary table using `booktabs` and `\begin{lstlisting}[style=output]`.

**Non-Goals:**
- Multi-page fluff or unnecessary boilerplates.

## Decisions

### 1. Document Structure
- **Section 1: Objective & Problem Formulation**: Mathematical definition of Stone's task assignment model, $X[M][P]$ and $C[M][M]$, and the conditional communication cost.
- **Section 2: Verification of Sample Problem**: Step-by-step breakdown of the 6-task, 2-processor sample topology showing Serial Cost = 58 and Optimal Cost = 38.
- **Section 3: Parallelization Methodology (OpenMP)**: Explaining how loop parallelism with persistent parallel regions and per-thread LCG RNG accelerates GA and PSO.
- **Section 4: Source Code**: Clean C implementation code.
- **Section 5: Experimental Results & Analysis**: Benchmark table with times, speedups, and costs for $M=250, P=8$ across 4 threads, along with the terminal output.

### 2. Code Listing Strategy
- Use the requested `style=code` and `style=output` definitions.

## Risks / Trade-offs

- **[Risk] LaTeX compilation errors with special characters in code/output** $\rightarrow$ **Mitigation**: Escape underscores, percent signs, and use proper `listings` delimiters.
