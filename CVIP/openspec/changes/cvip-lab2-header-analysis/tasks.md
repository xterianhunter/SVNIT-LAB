## 1. Test Asset Preparation & Data Structures

- [x] 1.1 Generate a sample PPM test image (`sample_01.ppm`) from `sample_01.pgm` (or synthetic color test pattern) and define the `ImageHeader` struct in `lab2_analysis.c`. Verify image file existence.
- [x] 1.2 Implement robust header parsing (`skip_comments`, magic number extraction, width, height, MaxVal, channel detection, bytes per sample) and total file size measurement via `fseek`/`ftell`. Verify with test header prints.

## 2. Payload Reading, Verification & Analytical Routines

- [x] 2.1 Implement dynamic payload memory allocation, `fread()` buffer reading, and integrity verification comparing expected bytes vs actual bytes read and file length.
- [x] 2.2 Implement first-10 pixel inspection supporting 1-channel grayscale (PGM), 3-channel RGB (PPM), and 16-bit sample decoding explanations.
- [x] 2.3 Implement automated format vs. extension justification and the $640 \times 480$ critical-thinking scaling computation for 8-bit/16-bit PGM/PPM.

## 3. Build Configuration & End-to-End Verification

- [x] 3.1 Update `Makefile` with `lab2_analysis` build target and `run-lab2` execution target.
- [x] 3.2 Compile using `gcc -std=c99 -Wall -Wextra -O2 lab2_analysis.c -o lab2_analysis` (or `make lab2`) and execute on `sample_01.pgm` and `sample_01.ppm` to verify complete output matching all Lab 2 objectives.
