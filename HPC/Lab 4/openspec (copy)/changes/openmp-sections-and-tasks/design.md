## Context

See `proposal.md` for motivation. The user requested simple, separate C programs demonstrating OpenMP `sections` and `task` pragmas with minimal boilerplate.

## Goals / Non-Goals

**Goals:**
- Provide `sections_demo.c` demonstrating `#pragma omp parallel sections` with multiple independent `#pragma omp section` blocks.
- Provide `task_demo.c` demonstrating `#pragma omp parallel` with `#pragma omp single`, generating dynamic `#pragma omp task` units and synchronizing them with `#pragma omp taskwait`.
- Keep the programs self-contained, minimal, easily readable, and compilable with standard GCC (`-fopenmp`).

**Non-Goals:**
- Complex data structures, heavy matrix computations, or external benchmarking libraries.
- Combining both pragmas into a single convoluted source file.

## Decisions

- **Two Separate Files**:
  - `sections_demo.c` for sections work-sharing.
  - `task_demo.c` for task parallelism.
  *Rationale*: Satisfies user request for separate, clean showcase programs.
  *Alternatives considered*: A single multi-mode program with command-line arguments (rejected for added complexity).

- **Standard OpenMP Runtime Reporting**:
  - Use `omp_get_thread_num()` and `omp_get_num_threads()` to print clear messages showing which thread is executing which section or task.
  *Rationale*: Visually confirms parallel execution without needing extra profiling tools.

## Risks / Trade-offs

- *[Risk]* Running with only 1 thread (`OMP_NUM_THREADS=1`) makes parallel behavior trivial or hard to observe.
  → *Mitigation*: Include explicit thread setting instructions (e.g. `export OMP_NUM_THREADS=4` or runtime hints) in documentation/build comments.
