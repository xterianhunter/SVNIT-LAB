## Why

In High Performance Computing (HPC) using OpenMP in C, work sharing and task parallelism are fundamental concepts. The user wants simple, minimal, and standalone demonstration programs showcasing:
1. OpenMP `sections` (`#pragma omp sections` and `#pragma omp section`) for static non-iterative work-sharing among threads.
2. OpenMP `task` (`#pragma omp task` and `#pragma omp single`) for dynamic, irregular, or asynchronous task parallelism.

Separating these showcases into dedicated C programs provides clean, readable examples without boilerplate or unnecessary complexity.

## What Changes

- Create a standalone C showcase program `sections_demo.c` demonstrating `#pragma omp parallel sections` and `#pragma omp section`.
- Create a standalone C showcase program `task_demo.c` demonstrating `#pragma omp single` with `#pragma omp task` and `#pragma omp taskwait`.
- Provide compilation commands / verification steps using GCC (`gcc -fopenmp`).

## Capabilities

### New Capabilities
- `openmp-sections-and-tasks`: Showcase implementation of OpenMP `sections` and `task` pragmas in C through two standalone, minimal demonstration programs.

### Modified Capabilities
<!-- None -->

## Impact

- **Affected Code**: Adds `sections_demo.c` and `task_demo.c` to the workspace.
- **Dependencies**: Requires a C compiler with OpenMP support (e.g., `gcc` with `-fopenmp`).
- **APIs / Libraries**: Uses `omp.h` and standard OpenMP runtime functions (`omp_get_thread_num()`).
