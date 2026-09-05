## Context

See `proposal.md` and `specs/statistical-order-filtering/spec.md`. The task is to implement and analyze order-statistics filtering on `Filtering-Cameraman.png` for CVIP Lab Assignment 4, adhering strictly to user guidelines: clean, concise, short, simple, and free of unnecessary bloat.

## Goals / Non-Goals

**Goals:**
- Implement all order statistics filters (median, min, max, midpoint, alpha-trimmed mean, 25th & 75th percentiles) using vectorized NumPy sliding window techniques to keep code exceptionally short, readable, and fast.
- Create a single, self-contained, clean Jupyter notebook: `cvip_lab4.ipynb`.
- Provide noise generation (salt-and-pepper and Gaussian) to showcase filter effectiveness.
- Display visual comparisons across kernel sizes ($3 \times 3$, $5 \times 5$, $7 \times 7$) and summarize concise observations directly in markdown cells.

**Non-Goals:**
- No complex GUI, CLI wrappers, or multi-file package architectures.
- No heavy third-party dependencies outside standard scientific Python libraries (`numpy`, `matplotlib`, `opencv-python` / `PIL`).
- No extraneous theoretical padding or verbose boilerplate.

## Decisions

- **Sliding Window via `numpy.lib.stride_tricks.sliding_window_view`**:
  - *Rationale*: Avoids slow nested 4-level pixel loops while avoiding opaque black-box libraries. With `sliding_window_view(np.pad(image, pad, mode='reflect'), (k, k))`, neighborhoods are shaped as `(H, W, k*k)` and sorted along the neighborhood axis. Every filter (min, max, median, midpoint, alpha-trimmed, percentiles) becomes a 1-to-2 line vectorized slice.
  - *Alternatives considered*:
    - 4 nested Python `for` loops: slow in Python for $5 \times 5$ and $7 \times 7$ kernels.
    - `scipy.ndimage.generic_filter`: requires extra dependency import and callback overhead.
- **Notebook Structure (`cvip_lab4.ipynb`)**:
  - Section 1: Setup & Image Loading (`Filtering-Cameraman.png`).
  - Section 2: Noise Injection (Salt-and-Pepper & Gaussian).
  - Section 3: Concise Order-Statistics Filter Functions.
  - Section 4: Multi-Scale Filtering ($3 \times 3, 5 \times 5, 7 \times 7$) & Visual Grid Comparison.
  - Section 5: Observations & Analysis (Noise reduction vs. edge preservation).

## Risks / Trade-offs

- **Memory usage with large kernels and high-resolution images**:
  - `sliding_window_view` creates a strided view (zero memory copy), but flattening or sorting creates a copy of shape `(H, W, k*k)`.
  - *Mitigation*: The Cameraman image is standard size ($256 \times 256$ or $512 \times 512$), so `k=7` requires only a few megabytes of RAM, executing in a fraction of a second.
