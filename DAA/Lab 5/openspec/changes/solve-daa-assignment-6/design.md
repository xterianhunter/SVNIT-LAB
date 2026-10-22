## Context

Lab Assignment 6 requires implementing large integer multiplication using the Karatsuba divide-and-conquer algorithm ($O(n^{\log_2 3}) \approx O(n^{1.585})$) and conventional multiplication ($O(n^2)$). The user specified adding this at the end of the existing notebook `daa_assignments_1_to_5.ipynb` while keeping the code short, simple, and avoiding unnecessary boilerplate.

## Goals / Non-Goals

**Goals:**
- Implement concise conventional grade-school multiplication ($O(n^2)$).
- Implement recursive Karatsuba divide-and-conquer multiplication ($O(n^{1.585})$).
- Benchmark both methods across increasing digit sizes (e.g. 64, 128, 256, 512, 1024 digits).
- Append the new markdown and code cells cleanly at the end of `daa_assignments_1_to_5.ipynb`.

**Non-Goals:**
- Modifying or re-executing assignments 1 through 5.
- Introducing external libraries or complex OOP structures.

## Decisions

### Decision 1: Concise Implementation of Conventional Multiplication ($O(n^2)$)
- **Choice**: Implement grade-school column multiplication: for each digit $d_i$ in multiplier $Y$, compute partial product $X \times d_i \times 10^i$ and sum them.
- **Rationale**: True $O(n^2)$ digit-level operations, expressed in just 6 lines of standard Python without heavy boilerplate.

### Decision 2: Recursive Karatsuba Algorithm ($O(n^{1.585})$)
- **Choice**: Split $X$ and $Y$ at $m = \lfloor n / 2 \rfloor$ using `divmod(x, 10**m)` into $(x_1, x_0)$ and $(y_1, y_0)$. Recursively compute:
  - $z_0 = \text{karatsuba}(x_0, y_0)$
  - $z_2 = \text{karatsuba}(x_1, y_1)$
  - $z_1 = \text{karatsuba}(x_0 + x_1, y_0 + y_1) - z_0 - z_2$
  - Return $z_2 \times 10^{2m} + z_1 \times 10^m + z_0$.
  - Base case: if $x < 10$ or $y < 10$, return $x \times y$.
- **Rationale**: Minimal, mathematically canonical Karatsuba reduction reducing 4 subproblems to 3, achieving $O(n^{\log_2 3}) \approx O(n^{1.585})$ complexity.

### Decision 3: Appending to `daa_assignments_1_to_5.ipynb`
- **Choice**: Read the existing notebook JSON, append the Assignment 6 markdown description, implementation code cell, and benchmark results cell, and write back.
- **Rationale**: Preserves 100% of existing assignment outputs while keeping the entire assignment series in one unified notebook.

## Risks / Trade-offs

- **[Risk] Recursion limit for huge integers**:
  - *Mitigation*: For inputs up to 1024 digits, recursion depth is $\approx \log_2(1024) = 10$, well below Python's recursion limit of 1000.
