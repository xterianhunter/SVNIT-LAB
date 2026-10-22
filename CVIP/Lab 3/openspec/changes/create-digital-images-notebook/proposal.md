## Why

The CSDS119 Computer Vision and Image Processing lab requires an organized, complete, and runnable Jupyter Notebook based on `CVIP_Lab_3_Understanding_Digital_Images-Copy1.pdf`. A clean, self-contained notebook implementing Parts 1 through 14 using `sample.jpg` as the input image is needed to replace incomplete scratch files and ensure all exercises and theoretical reflection questions are properly structured, concise, and executable.

## What Changes

- Create a structured, executable Jupyter Notebook (`Lab3_Understanding_Digital_Images.ipynb`) covering all 14 parts defined in the lab guide.
- Retain the exact lab structure, markdown headers, and theoretical "Think" reflection prompts from the lab document.
- Include all pre-written tutorial code cells from the PDF (Part 1 imports, Part 2 image loading with `sample.jpg` fallback and RGB display, Part 3 image property inspection, Part 4 grayscale conversion).
- Implement clean, concise code for all exercise blocks (`#add your code here`):
  - Part 5: Matrix representation inspection and row-column `[y, x]` pixel indexing.
  - Part 6: Single-pixel modification to white (`255`).
  - Part 7: Grayscale negative transformation ($s = 255 - r$).
  - Part 8: Brightness increase by 50 with `np.clip` bounds clamping.
  - Part 9: Binary thresholding investigation across $T \in \{50, 100, 180, 220\}$.
  - Part 10: Intensity histogram visualization.
  - Part 11: Image cropping and resizing demonstrations.
  - Part 12: Impulse salt-and-pepper noise generation.
  - Part 13: Mean ($3\times3$ box blur) vs. Median filtering comparison for salt-and-pepper noise removal.
  - Part 14: Manual order-statistic matrix calculation verification (min, max, median, mean, midpoint).
- Ensure all code is concise, avoids extraneous loops/prints, and executes smoothly without bloat.

## Capabilities

### New Capabilities
- `digital-image-processing-lab`: Provides an end-to-end Jupyter Notebook executing fundamental digital image manipulation, transformations, noise models, and spatial filtering using OpenCV, NumPy, and Matplotlib.

### Modified Capabilities
<!-- None -->

## Impact

- **New files**: Creates `Lab3_Understanding_Digital_Images.ipynb`.
- **Inputs**: Uses `sample.jpg` present in the project directory.
- **Dependencies**: Uses `opencv-python` (`cv2`), `numpy`, and `matplotlib`.
