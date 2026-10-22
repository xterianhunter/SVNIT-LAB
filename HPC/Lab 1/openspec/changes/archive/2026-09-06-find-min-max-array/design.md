## Context

See proposal.md. The implementation requires the simplest possible C program using dynamic memory allocation to find the minimum and maximum of an array of integers without unnecessary boilerplate or libraries.

## Goals / Non-Goals

**Goals:**
- Provide clear, minimal, idiomatic standard C code in a single file (`min_max.c`).
- Use `malloc` to allocate memory dynamically for `n` integers and `free` to release memory.
- Find both minimum and maximum in a single pass ($O(n)$ time, $O(1)$ extra space).

**Non-Goals:**
- Elaborate CLI flag parsing or menu systems.
- Custom dynamic array resizing or data structure abstractions.
- Complex error-handling frameworks beyond basic allocation safety.

## Decisions

- **File Layout**: Single source file `min_max.c` with a straightforward `main()` function.
  - *Rationale*: Fits the user's constraint for the simplest code possible without extra headers or helper modules.
- **Dynamic Allocation**: Use standard `malloc(n * sizeof(int))` and check for allocation failure.
  - *Rationale*: Standard C dynamic memory allocation idiom.
- **Single-Pass Search**: Initialize `min` and `max` with the first element (`arr[0]`), then iterate from index 1 to `n-1`.
  - *Rationale*: Optimal $O(n)$ comparisons, simplest logic.

## Risks / Trade-offs

- [Memory allocation failure] → Check if pointer returned by `malloc` is `NULL` and exit cleanly.
- [Invalid input size (n <= 0)] → Handle with a simple check and message.
