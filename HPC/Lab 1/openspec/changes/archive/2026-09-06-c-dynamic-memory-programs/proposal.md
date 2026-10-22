## Why

Minimal, educational C programs are required to demonstrate core computational algorithms (matrix multiplication, vector dot product, and divide-and-conquer array sorting) using dynamic memory allocation with the simplest possible code.

## What Changes

- Add `matrix_mult.c`: computes matrix multiplication for user-defined dimensions and matrices allocated dynamically.
- Add `dot_product.c`: computes the dot product of two vectors of user-defined length allocated dynamically with user inputs.
- Add `merge_sort.c`: sorts an array of user-defined size using divide-and-conquer (merge sort) and dynamic memory allocation.

## Capabilities

### New Capabilities
- `matrix-multiplication`: Matrix multiplication of user-specified dimensions using dynamically allocated 2D arrays.
- `vector-dot-product`: Dot product calculation of two user-specified vectors using dynamically allocated 1D arrays.
- `divide-and-conquer-sort`: Divide-and-conquer array sorting (merge sort) using dynamic memory allocation.

### Modified Capabilities
<!-- Existing capabilities whose REQUIREMENTS are changing -->

## Impact

- Adds three standalone C source files: `matrix_mult.c`, `dot_product.c`, and `merge_sort.c`.
- Uses standard C library (`stdio.h`, `stdlib.h`).
- No external dependencies.
