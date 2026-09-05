## Purpose

Provides interactive and educational executable workflows for loading digital images, inspecting properties, performing spatial and intensity transformations, introducing noise, and evaluating order-statistic filtering in Python.

## ADDED Requirements

### Requirement: Lab Notebook Structure and Environment Setup
The notebook SHALL contain all 14 sequential lab sections with descriptive markdown headers, instructional prompts, reflection questions, and runnable code cells importing `cv2`, `numpy`, and `matplotlib.pyplot`.

#### Scenario: Running initial setup
- **WHEN** the user executes the Part 1 setup cell
- **THEN** required libraries (`cv2`, `numpy`, `matplotlib.pyplot`) MUST import without errors and print a confirmation message.

### Requirement: Image Ingestion and Visualization
The notebook SHALL load `sample.jpg` using OpenCV and render the RGB visualization using Matplotlib.

#### Scenario: Image file loading
- **WHEN** the user executes Part 2
- **THEN** `sample.jpg` MUST be read into a NumPy ndarray and rendered with Matplotlib with proper BGR to RGB color conversion.

### Requirement: Property and Matrix Inspection
The notebook SHALL inspect image attributes including shape, data type, and min/max pixel values, display slice matrices, and demonstrate row/column pixel coordinate indexing `[y, x]`.

#### Scenario: Inspecting image properties and pixel values
- **WHEN** Part 3, Part 4, and Part 5 are executed
- **THEN** image shape, channel dimensions, and intensity matrix values MUST be displayed, and individual pixel intensity at `(y, x)` MUST be retrieved.

### Requirement: Intensity Transformations
The notebook SHALL implement grayscale conversion, single-pixel modification, negative image transformation ($s = 255 - r$), brightness increase with clipping ($s = \text{clip}(r + 50, 0, 255)$), and multi-threshold binary segmentation.

#### Scenario: Executing intensity transformations
- **WHEN** Parts 6, 7, 8, and 9 are executed
- **THEN** the modified pixel image, negative grayscale image, brightened image clamped to $[0, 255]$, and binary thresholded images for $T \in \{50, 100, 180, 220\}$ MUST be computed and rendered.

### Requirement: Histogram and Spatial Operations
The notebook SHALL plot intensity distribution histograms, extract cropped rectangular sub-regions, and resize image spatial dimensions.

#### Scenario: Visualizing histogram and geometric transforms
- **WHEN** Parts 10 and 11 are executed
- **THEN** an intensity frequency histogram MUST be plotted for the grayscale image, and cropped/resized images MUST be generated and visualized.

### Requirement: Noise Simulation and Spatial Filtering
The notebook SHALL introduce impulse salt-and-pepper noise and compare mean box filtering against median filtering.

#### Scenario: Filtering salt-and-pepper noise
- **WHEN** Parts 12 and 13 are executed
- **THEN** an impulse noisy image MUST be generated, and both mean-filtered and median-filtered outputs MUST be displayed side by side for visual comparison of noise removal and edge preservation.

### Requirement: Order-Statistic Matrix Verification
The notebook SHALL compute order-statistic metrics (minimum, maximum, median, mean, and midpoint) for the given $3\times3$ neighborhood matrix $\begin{bmatrix} 42&43&44\\ 43&255&45\\ 44&45&46 \end{bmatrix}$.

#### Scenario: Order-statistic computation
- **WHEN** Part 14 is executed
- **THEN** the minimum (42), maximum (255), median (44), mean (~66.78), and midpoint (148.5) MUST be calculated and printed.
