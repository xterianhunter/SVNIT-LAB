## 1. Race Condition and Critical Section Programs

- [x] 1.1 Implement `race_condition.c` showing unsynchronized concurrent shared counter increments, and verify compilation and output with `gcc -fopenmp -O2 race_condition.c -o race_condition && ./race_condition`
- [x] 1.2 Implement `critical_section.c` using `#pragma omp critical` to synchronize shared counter updates, and verify that actual output strictly matches expected output with `gcc -fopenmp -O2 critical_section.c -o critical_section && ./critical_section`

## 2. Parallel Matrix-Matrix Multiplication

- [x] 2.1 Implement `matrix_mult.c` with coarse-grained and fine-grained OpenMP decompositions and wall-clock timing, and verify correctness and timing with `gcc -fopenmp -O2 matrix_mult.c -o matrix_mult && ./matrix_mult`

## 3. Build Configuration and Verification

- [x] 3.1 Create `Makefile` supporting `all`, individual targets, and `clean`, and verify clean build of all targets via `make clean && make`
