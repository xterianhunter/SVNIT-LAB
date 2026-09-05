## Why

The user requires a formal academic LaTeX report document formatted according to a specific documentclass, typography (12pt Times-style), header layout (Name: Kishan Sahu, Enrollment No.: P26DS017), and custom `listings` environments (`style=code` and `style=output`). The LaTeX report must document all 14 parts of the CSDS119 Computer Vision & Image Processing lab ("Understanding Digital Images Using Python"), embedding Python source codes, program outputs, mathematical matrices/tables, generated plot figures, and answers to theoretical reflection prompts.

## What Changes

- Extract and save all high-resolution output figures from the lab notebook execution into a local `figures/` directory.
- Create `Lab3_Understanding_Digital_Images.tex` matching the exact LaTeX preamble, page geometry, font configuration, header, and listings styles specified by the user.
- Structure the report systematically across all 14 parts:
  - Part 1: Setup and library imports.
  - Part 2: Image ingestion with fallback logic and original RGB image figure.
  - Part 3: Image properties inspection (shape, dtype, min/max intensity).
  - Part 4: Grayscale conversion and comparative color vs. grayscale visualization.
  - Part 5: Matrix representation inspection (slice table/listing) and row-column `[y, x]` indexing.
  - Part 6: Single-pixel modification experiment and perceptibility analysis.
  - Part 7: Intensity negative transformation ($s = 255 - r$) with visual comparison figure.
  - Part 8: Brightness transformation ($s = \text{clip}(r + 50, 0, 255)$) and clipping analysis.
  - Part 9: Binary thresholding investigation across $T \in \{50, 100, 180, 220\}$ with 4-panel subplot figure.
  - Part 10: Intensity histogram visualization figure and distribution analysis.
  - Part 11: Cropping and resizing operations with comparative figure.
  - Part 12: Impulse salt-and-pepper noise simulation figure.
  - Part 13: Order-statistic filtering (mean box blur vs. median filter) comparative figure and analysis.
  - Part 14: Manual order-statistic matrix calculations table and Python verification.
- Provide responses to all "Think Before Moving Ahead", "Investigation", and "Critical Thinking" questions directly in the report.

## Capabilities

### New Capabilities
- `latex-lab-report`: Compiles the complete digital image processing lab curriculum, source codes, terminal outputs, mathematical formulas, and generated visual figures into an academic LaTeX report.

### Modified Capabilities
<!-- None -->

## Impact

- **New files**: `Lab3_Understanding_Digital_Images.tex`, and figure assets in `figures/`.
- **Dependencies**: LaTeX distribution / Overleaf with standard packages (`geometry`, `newtxtext`, `newtxmath`, `fancyhdr`, `listings`, `graphicx`, `float`, `amsmath`).
