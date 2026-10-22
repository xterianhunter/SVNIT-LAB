## Context

See `proposal.md` for motivation. The workspace contains two binary PGM images (`sample_01.pgm` at $640 \times 426$ and `sample_02.pgm` at $1280 \times 853$). The assignment requires a pure C solution utilizing basic array operations and standard libraries, without complex external image dependencies (such as OpenCV).

## Goals / Non-Goals

**Goals:**
- Implement a clear, modular, and idiomatic C program (`lab1_analysis.c`) suitable for student comprehension and submission.
- Use a clean `Image` struct encapsulating width, height, max value, and a contiguous 1D pixel buffer.
- Provide functions for reading/writing standard PGM images (handling comments and whitespace robustly).
- Implement all analytical routines required by CVIP Lab 1: basic stats, contrast (standard deviation), 256-bin histogram, range distribution (Dark/Med/Bright), ROI analysis, brightness transformation, iso-mean demonstration, and thresholding suitability justification.
- Produce organized, formatted console output (tables and ASCII distribution bars) that directly answers all assignment questions.

**Non-Goals:**
- External GUI or heavy library integration (e.g. OpenCV, GTK).
- Support for compressed image formats (JPEG/PNG) which require external decompression libraries.
- Complex multi-threaded image processing pipelines.

## Decisions

1. **Language and Standard**: Standard C99 (`gcc -std=c99 -Wall -Wextra -O2 lab1_analysis.c -lm -o lab1_analysis`).
   - *Rationale*: Maximum portability, zero external dependencies, native array manipulation as requested.
   - *Alternative Considered*: C++ with `std::vector` (rejected because assignment specifically mandates C).

2. **Data Representation**:
   - `typedef struct { int width; int height; int max_val; unsigned char *data; } Image;`
   - *Rationale*: A contiguous 1D array indexed via `y * width + x` offers cache locality, simple memory allocation (`malloc(width * height)`), and straightforward pointer arithmetic.

3. **PGM Parser**:
   - Custom lightweight parser supporting binary P5 (and ASCII P2 fallback), skipping Netpbm comment lines (`# ...`).
   - *Rationale*: Keeps code self-contained and avoids buffer overflows.

4. **Statistical and Range Metrics**:
   - Mean intensity: $\mu = \frac{1}{N} \sum I(x, y)$
   - Contrast / Variance: $\sigma^2 = \frac{1}{N} \sum (I(x, y) - \mu)^2$, $\sigma = \sqrt{\sigma^2}$
   - Ranges: Dark $[0, 85]$, Medium $[86, 170]$, Bright $[171, 255]$.
   - *Rationale*: Standard definitions in digital image processing literature (Gonzalez & Woods).

5. **Region of Interest (ROI) Selection**:
   - Centered or feature-rich sub-rectangles (e.g., $100 \times 100$ or $200 \times 200$ bounding box) from each sample image to highlight local vs. global statistical variations.

6. **Iso-mean Demonstration**:
   - Demonstrating using two complementary synthetic patterns (or distinct image regions) with identical mean ($128.0$) but completely divergent variance and histogram profiles (e.g., high-contrast black/white checkerboard vs. flat solid gray).

## Risks / Trade-offs

- **[Risk]** Large image file size memory footprint.
  - *Mitigation*: Images are $\le 1.1\text{ MB}$, fitting trivially into standard process memory. Dynamic memory is cleanly freed (`free_image`).
- **[Risk]** Integer overflow during sum computation.
  - *Mitigation*: Use 64-bit integer (`unsigned long long`) or `double` for accumulation before division.
- **[Risk]** Pixel clipping during brightness enhancement.
  - *Mitigation*: Explicit clamping `val > 255 ? 255 : (unsigned char)val`.
