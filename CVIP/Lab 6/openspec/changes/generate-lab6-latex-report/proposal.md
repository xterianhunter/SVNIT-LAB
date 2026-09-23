## Why

The user requires a formal LaTeX laboratory report for CVIP Lab Assignment 6 (Image Segmentation) at SVNIT using their specified preamble, document styling, and student header (Name: Kishan Sahu, Enrollment No.: P26DS017). The report must incorporate all code, textual outputs, generated plots, and analytical discussions from `lab6_image_segmentation.ipynb`.

## What Changes

- **Figure Extraction**: Extract all base64-embedded plot outputs from `lab6_image_segmentation.ipynb` and save them as high-resolution PNG images in a dedicated `figures/` directory.
- **LaTeX Report Creation**: Write a complete LaTeX report file (`lab6_report.tex` and/or `main.tex`) conforming strictly to the user's provided template, including:
  - Header: Name: Kishan Sahu, Enrollment No.: P26DS017, SVNIT Computer Science and Engineering Department, M.Tech. I -- Semester I, Computer Vision and Image Processing (CSCS111/CSDS119), Lab Assignment 6: Image Segmentation.
  - Listings configurations (`style=code` for Python source and `style=output` for execution logs).
  - Mathematical formulations and filter kernel matrices for point, line, edge, threshold, and region growing operations.
  - Complete code listings and verbatim terminal outputs for all experimental sections.
  - Embedded figures corresponding to Part A (original image, point/line detection, edge operators, thresholding, region growing sensitivity) and Part B (single-technique failure comparison, black cup mask, retained object, and disappeared inpainted scene).
  - In-depth analytical observations comparing classical segmentation methods and justifying the hybrid pipeline for the black cup.

## Capabilities

### New Capabilities
- `latex-report-generation`: Standalone LaTeX report document with extracted figures, listings, and complete academic writeup for Lab 6.

### Modified Capabilities
*(None)*

## Impact

- Creates `figures/` directory with image assets (`fig1_original.png`, `fig2_point_line.png`, `fig3_edges.png`, `fig4_thresholding.png`, `fig5_region_growing.png`, `fig6_part_b_black_cup.png`).
- Creates `lab6_report.tex` (and `main.tex`).
- No modifications to notebook source code.
