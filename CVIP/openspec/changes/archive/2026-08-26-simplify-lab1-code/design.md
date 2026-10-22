## Context

See `proposal.md` for motivation. The initial implementation was ~576 lines with extensive ASCII chart generation, redundant intermediate structs, and multi-layered helper functions. The design simplifies the program into clean, concise, idiomatic C (~150-180 lines) while preserving all mathematical, analytical, and academic deliverables of CVIP Lab 1.

## Goals / Non-Goals

**Goals:**
- Provide a clean, minimal `Image` struct (`int w, h; unsigned char *data;`) for storing image buffers.
- Implement concise helper routines for PGM reading, writing, statistics computation, histogram counting, ROI analysis, and brightening.
- Keep all terminal outputs clean, clear, and easy to read, presenting all required answers for Lab 1.
- Keep code compact, readable, and under 200 lines.

**Non-Goals:**
- Supporting arbitrary formats beyond standard P5/P2 PGM files.
- Implementing GUI or terminal graphics libraries.
- Creating separate translation units or complex header files (single C file + Makefile is ideal for this lab).

## Decisions

### 1. Minimal Image Representation
- **Decision**: Define a single concise structure:
  ```c
  typedef struct {
      int w, h;
      unsigned char *data;
  } Image;
  ```
- **Rationale**: Minimal memory overhead, zero boilerplate, direct contiguous 1D array indexing (`y * w + x`).
- **Alternatives Considered**: Complex OOP-like image structs with redundant metadata fields (`max_val`, `channels`, etc.) - rejected as unnecessary clutter for 8-bit grayscale images.

### 2. Streamlined Statistics & Range Calculation
- **Decision**: Compute min, max, mean, variance, std dev, and dark/medium/bright counts in simple, clean loops.
- **Rationale**: Keeps calculations straightforward and easy to understand for student lab evaluations without unnecessary wrapper functions or duplicated passes.

### 3. Compact Tabular Histogram Summary
- **Decision**: Compute full 256-bin histogram and print a compact 16-interval table with percentages.
- **Rationale**: Conveys the exact distribution clearly and compactly without requiring 50+ lines of ASCII bar drawing code.

### 4. Direct ROI & Brightness Manipulation
- **Decision**: Compute sub-region statistics directly with boundary checks, and apply brightness offset + clamping via `min(255, val + offset)`.
- **Rationale**: Direct, clean implementation matching the core digital image processing definitions.

## Risks / Trade-offs

- **[Risk] PGM Header variations (comments in headers)** → **Mitigation**: Use a concise comment-skipping helper before reading width, height, and max value.
- **[Risk] Clamping overflow on brightened pixels** → **Mitigation**: Perform integer addition before casting back to `unsigned char`.
