## 1. Implementation of Sections Showcase

- [x] 1.1 Create `sections_demo.c` with `#pragma omp parallel section` and independent `#pragma omp section` blocks, printing thread ID and section name, and verify successful compilation with `gcc -fopenmp sections_demo.c -o sections_demo`.
- [x] 1.2 Run `./sections_demo` with multiple threads (`OMP_NUM_THREADS=3 ./sections_demo`) and verify that distinct sections are assigned to and executed by OpenMP threads.

## 2. Implementation of Task Showcase

- [x] 2.1 Create `task_demo.c` with `#pragma omp parallel` enclosing a `#pragma omp single` construct that spawns asynchronous `#pragma omp task` blocks synchronized with `#pragma omp taskwait`, and verify successful compilation with `gcc -fopenmp task_demo.c -o task_demo`.
- [x] 2.2 Run `./task_demo` with multiple threads (`OMP_NUM_THREADS=4 ./task_demo`) and verify that tasks are executed across worker threads and complete before the taskwait barrier.
