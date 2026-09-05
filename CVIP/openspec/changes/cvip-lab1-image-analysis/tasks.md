## 1. Core Program Structure & PGM I/O

- [x] 1.1 Create `lab1_analysis.c` defining the `Image` struct and implementing robust PGM (P5 binary and P2 ASCII) image reading, writing, and memory management; verify by loading `sample_01.pgm` and `sample_02.pgm` without memory leaks or errors.
- [x] 1.2 Implement core statistical routines (dimensions, min intensity, max intensity, average intensity, variance, and standard deviation); verify by checking computed dimensions ($640 \times 426$ and $1280 \times 853$) and valid intensity bounds in $[0, 255]$.

## 2. Histogram & Range Analysis

- [x] 2.1 Implement 256-bin histogram generation and terminal-friendly ASCII visualization/summary table; verify that total bin counts exactly match total pixel counts ($W \times H$).
- [x] 2.2 Implement intensity range classification for Dark ($[0, 85]$), Medium ($[86, 170]$), and Bright ($[171, 255]$) intervals; verify that computed category percentages sum to $100.0\%$.

## 3. Comparative & Region of Interest (ROI) Analysis

- [x] 3.1 Implement numerical comparison logic between `sample_01.pgm` and `sample_02.pgm` to evaluate which image is brighter, darker, and which exhibits higher contrast.
- [x] 3.2 Implement Region of Interest (ROI) extraction and separate statistical profiling for selected high-contrast bounding boxes on both images; verify correct sub-grid boundary handling and stats computation.

## 4. Brightness Enhancement, Iso-mean Analysis & Segmentation

- [x] 4.1 Implement brightness modification (additive offset with $[0, 255]$ clamping), compute before/after comparative statistics and histogram shift, and save `sample_01_brightened.pgm`.
- [x] 4.2 Implement an iso-mean demonstration contrasting two visually distinct patterns (e.g. checkerboard vs. solid gray) that share identical average intensity.
- [x] 4.3 Implement thresholding/segmentation suitability analysis comparing histogram bimodality and dynamic range to provide clear scientific justification.

## 5. Build, Verification & Documentation

- [x] 5.1 Compile and run `lab1_analysis.c` with `gcc -Wall -Wextra -O2`, verifying all 9 assignment requirements are cleanly printed with clear reasoning in console output.
- [x] 5.2 Add build and execution instructions (including sample output summary) for student lab submission.
