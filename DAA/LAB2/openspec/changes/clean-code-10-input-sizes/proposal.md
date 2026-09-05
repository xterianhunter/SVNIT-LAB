## Why

To demonstrate granular asymptotic complexity trends in the lab submission report, the experimental benchmarks should evaluate and display results across at least 10 distinct input sizes rather than only 4 or 5 sizes. Expanding the input dataset array to 10 sizes provides dense empirical data points that clearly exhibit linear $\mathcal{O}(n)$, logarithmic $\mathcal{O}(\log n)$, quadratic $\mathcal{O}(n^2)$, and cubic $\mathcal{O}(n^3)$ scaling curves across all three problems.

## What Changes

- Update `clean_code/problem1_searching.py` default sizes to 10 distinct inputs: `(10, 20, 50, 75, 100, 150, 200, 300, 400, 500)`.
- Update `clean_code/problem2_sorting.py` default sizes to 10 distinct inputs: `(20, 40, 60, 80, 100, 150, 200, 300, 400, 500)`.
- Update `clean_code/problem3_matrix.py` default sizes to 10 distinct dimensions: `(10, 20, 30, 40, 50, 75, 100, 150, 200, 300)`.
- Maintain adaptive benchmark iteration counts so all 10 sizes execute swiftly and output clean, comprehensive tables.

## Capabilities

### New Capabilities
- `clean-code-10-input-sizes`: Comprehensive multi-point benchmarking across at least 10 input sizes for searching, sorting, and matrix operations in `clean_code/`.

### Modified Capabilities
<!-- None -->

## Impact

- **Affected Code**:
  - `clean_code/problem1_searching.py`
  - `clean_code/problem2_sorting.py`
  - `clean_code/problem3_matrix.py`
- **Dependencies**: Python standard library only (`time`, `random`, `os`).
