## 1. Core Data Structures & Image I/O Simplification

- [x] 1.1 Replace multi-struct definitions with a minimal `Image` struct (`int w, h; unsigned char *data;`) and implement concise memory allocation/deallocation helpers. Verify with a quick compile check.
- [x] 1.2 Implement compact `read_pgm` (with comment skipping) and `write_pgm` (for P5 output) routines. Verify by loading `sample_01.pgm` and `sample_02.pgm`.

## 2. Statistical Analysis & Transformations Simplification

- [x] 2.1 Implement streamlined image statistics (min, max, mean, variance, std dev) and dark/medium/bright range classification functions. Verify calculations match expected numerical benchmarks.
- [x] 2.2 Implement 256-bin histogram computation and a concise tabular distribution printer.
- [x] 2.3 Implement compact ROI analysis function for center and corner sub-regions.
- [x] 2.4 Implement brightness transformation with $[0, 255]$ clamping, and concise functions for iso-mean proof and thresholding suitability justification.

## 3. Pipeline Integration & End-to-End Verification

- [x] 3.1 Assemble the complete simplified `main()` driver in `lab1_analysis.c` to run the end-to-end lab analysis with clean, compact output.
- [x] 3.2 Compile using `gcc -std=c99 -Wall -Wextra -O2 lab1_analysis.c -lm -o lab1_analysis` (or `make`) and execute `./lab1_analysis sample_01.pgm sample_02.pgm` to verify correct output and clean generation of `sample_01_brightened.pgm`.
