## Purpose

Extends the DAA lab notebook with concise implementations and benchmarks for Karatsuba large integer multiplication and conventional multiplication.

## ADDED Requirements

### Requirement: Conventional Large Integer Multiplication
The notebook SHALL implement conventional grade-school large integer multiplication operating on strings/digit arrays or base-$10$ decompositions with $O(n^2)$ time complexity.

#### Scenario: Multiplication accuracy
- **WHEN** two large integers $X$ and $Y$ are multiplied using conventional multiplication
- **THEN** the computed product MUST match the true arithmetic product $X \times Y$.

### Requirement: Karatsuba Divide and Conquer Multiplication
The notebook SHALL implement the Karatsuba divide-and-conquer multiplication algorithm that splits $n$-digit integers into high and low halves and recursively computes three multiplications ($z_0, z_1, z_2$) with asymptotic time complexity $O(n^{\log_2 3}) \approx O(n^{1.585})$.

#### Scenario: Karatsuba product verification
- **WHEN** two large positive integers are multiplied using the Karatsuba algorithm
- **THEN** the returned product MUST be strictly equal to the product returned by conventional multiplication and built-in multiplication.

#### Scenario: Base case threshold
- **WHEN** the number of digits falls below a defined base threshold (e.g. $\le 16$ or single-digit)
- **THEN** the algorithm MUST switch to conventional base multiplication to avoid recursion overhead.

### Requirement: Empirical Benchmarking and Asymptotic Comparison
The notebook SHALL evaluate both algorithms on randomly generated integers across increasing digit lengths (e.g., 64, 128, 256, 512, 1024 digits), record execution times in microseconds, and tabulate the empirical performance comparison against theoretical expectations.

#### Scenario: Scaling benchmark
- **WHEN** digit lengths scale up from 64 to 1024 digits
- **THEN** the Karatsuba algorithm MUST demonstrate faster growth scalability than conventional multiplication, illustrating the transition from $O(n^2)$ to $O(n^{1.585})$.

### Requirement: Appending to Existing Notebook
The implementation SHALL be appended cleanly to `daa_assignments_1_to_5.ipynb` as Assignment 6 without modifying or removing existing assignment solutions or outputs.

#### Scenario: Notebook integrity
- **WHEN** Assignment 6 is added to `daa_assignments_1_to_5.ipynb`
- **THEN** all prior assignments (1 to 5) MUST remain intact and fully functional.
