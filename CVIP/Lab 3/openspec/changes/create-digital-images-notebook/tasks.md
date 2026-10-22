## 1. Setup and Notebook Scaffolding

- [x] 1.1 Create `Lab3_Understanding_Digital_Images.ipynb` structure with notebook metadata and Part 1 library imports (`cv2`, `numpy`, `matplotlib.pyplot`), and verify the notebook is valid JSON.
- [x] 1.2 Implement Part 2 image loading with `sample.jpg` default fallback and RGB Matplotlib display, and verify `sample.jpg` loads successfully.

## 2. Image Inspection and Representation

- [x] 2.1 Implement Part 3 image property inspection (data type, shape, pixel dtype, min/max values) and Part 4 grayscale conversion with side-by-side visualization, and verify channel dimensions match expected shapes.
- [x] 2.2 Implement Part 5 matrix slice inspection and row-column `[y, x]` pixel intensity access, and verify matrix values and coordinates print accurately.

## 3. Pixel Manipulation and Intensity Transformations

- [x] 3.1 Implement Part 6 single-pixel modification to white (`255`), and verify pixel modification execution.
- [x] 3.2 Implement Part 7 intensity transformation (negative image $s = 255 - r$), and verify inverted grayscale visualization.
- [x] 3.3 Implement Part 8 brightness transformation ($s = \text{clip}(r + 50, 0, 255)$) with bounds clipping, and verify no uint8 wrapping occurs.
- [x] 3.4 Implement Part 9 binary thresholding investigation for $T \in \{50, 100, 180, 220\}$, and verify multi-threshold subplot grid rendering.

## 4. Histograms, Spatial Operations, and Filtering

- [x] 4.1 Implement Part 10 intensity histogram visualization and Part 11 image cropping and resizing, and verify histogram plot and resized dimensions.
- [x] 4.2 Implement Part 12 impulse salt-and-pepper noise simulation and Part 13 mean vs. median filtering comparison, and verify 3-panel comparative visualization.
- [x] 4.3 Implement Part 14 manual order-statistic neighborhood calculation verification (min, max, median, mean, midpoint), and verify outputs match expected statistical values.

## 5. End-to-End Execution and Validation

- [x] 5.1 Execute the complete notebook head-to-tail to verify that all 14 parts run cleanly without errors, all reflection questions are present, and output sizes remain concise.
