## Context

See proposal.md. Three standalone programs are required demonstrating basic numerical and sorting operations using dynamic memory allocation in C with the simplest, most readable code possible.

## Goals / Non-Goals

**Goals:**
- Provide 3 self-contained C files (`matrix_mult.c`, `dot_product.c`, `merge_sort.c`).
- Use standard dynamic memory allocation (`malloc`, `free`) from `<stdlib.h>`.
- Use the simplest standard algorithms without superfluous abstractions:
  - 2D pointer-based arrays for matrix multiplication.
  - Linear vectors for dot product.
  - Classic recursive Merge Sort for divide-and-conquer array sorting.

**Non-Goals:**
- Complex CLI argument parsers or UI formatting.
- Multi-threaded or BLAS/LAPACK optimizations.
- Generic type templates or macro wrappers.

## Decisions

- **Matrix Allocation**: Allocate an array of row pointers `int **` where each row is allocated dynamically. This allows standard `A[i][j]` index syntax in C.
- **Dot Product**: Single dynamically allocated 1D array for each vector with a single accumulation loop.
- **Divide and Conquer Sort**: Implement Merge Sort with standard recursive splitting (`mergeSort(arr, l, r)`) and standard temporary merge array.
- **Memory Safety**: Free each allocated block explicitly before exiting.

## Risks / Trade-offs

- [Incompatible matrix dimensions] → Check condition $c_1 == r_2$ before allocating Matrix B / result matrix and multiplying; exit with message if incompatible.
- [Allocation failure] → Check pointers returned by `malloc` for `NULL`.
