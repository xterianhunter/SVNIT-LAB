## Purpose

Provides comprehensive image reading, statistical analysis, histogram profiling, range partitioning, region-of-interest extraction, brightness manipulation, and segmentation feasibility assessment for digital grayscale images using basic C operations.

## ADDED Requirements

### Requirement: Grayscale Image Ingestion
The system SHALL read grayscale image files in PGM (Netpbm binary P5 or ASCII P2) format and store their pixel values into memory arrays without external image processing libraries.

#### Scenario: Read valid P5 PGM image
- **WHEN** a valid P5 binary PGM image file path is provided
- **THEN** the system parses width, height, and max intensity, and loads all pixel values into a flat or 2D array of bytes/integers.

#### Scenario: Handle missing or invalid image file
- **WHEN** an invalid file path or unsupported format is specified
- **THEN** the system outputs a descriptive error message and terminates gracefully without crashing.

### Requirement: Image Statistics Computation
The system SHALL compute fundamental statistical properties of the loaded image arrays: dimensions ($W \times H$), minimum intensity, maximum intensity, average (mean) intensity, and contrast metric (standard deviation/variance).

#### Scenario: Compute metrics for standard grayscale image
- **WHEN** an image array is processed
- **THEN** the system determines minimum value in $[0, 255]$, maximum value in $[0, 255]$, mean intensity as a floating-point value, and contrast metric.

### Requirement: Intensity Histogram Generation
The system SHALL compute a 256-bin intensity histogram mapping frequencies of each gray level $[0, 255]$ and provide distribution metrics along with a terminal-friendly ASCII visualization.

#### Scenario: Generate 256-bin histogram
- **WHEN** the image pixels are scanned
- **THEN** the system populates an array of 256 counts where index $i$ corresponds to the frequency of pixel value $i$.

#### Scenario: Display histogram distribution
- **WHEN** the histogram analysis is displayed
- **THEN** the system outputs key distribution statistics and a scaled ASCII bar representation of the frequency bins.

### Requirement: Intensity Range Classification
The system SHALL partition pixel values into three distinct intensity intervals—Dark ($[0, 85]$), Medium ($[86, 170]$), and Bright ($[171, 255]$)—and calculate the exact percentage of total pixels in each category.

#### Scenario: Intensity range percentages calculation
- **WHEN** the range partitioner evaluates the pixel array
- **THEN** the sum of percentages across Dark, Medium, and Bright categories equals 100.0% ($\pm 0.01\%$).

### Requirement: Numerical Comparative Analysis
The system SHALL compare two input grayscale images using computed numerical statistics rather than subjective visual inspection to identify which image is brighter, darker, and which exhibits higher contrast.

#### Scenario: Compare two images with different statistics
- **WHEN** two distinct images are analyzed
- **THEN** the system reports which image has higher mean intensity (brighter), lower mean intensity (darker), and higher contrast (larger standard deviation / dynamic range).

### Requirement: Region of Interest (ROI) Analysis
The system SHALL allow selecting a rectangular sub-region (ROI) from an image and analyze its statistical properties and intensity distribution separately from the global image.

#### Scenario: Analyze sub-region with distinct intensity
- **WHEN** a sub-region bounding box $(x, y, w, h)$ is specified
- **THEN** the system computes dimensions, min, max, average intensity, and dark/medium/bright breakdown specifically for that ROI.

### Requirement: Brightness Modification and Shift Analysis
The system SHALL modify pixel values of an image to increase brightness without altering spatial dimensions, clamp resulting values to $[0, 255]$, and analyze before-and-after statistical and histogram changes.

#### Scenario: Brighten image by positive offset
- **WHEN** a brightness increment $\Delta$ is applied to an image
- **THEN** the mean intensity increases, histogram bins shift rightwards, and pixel values above 255 are clamped to 255.

### Requirement: Iso-mean Visual Dissimilarity Demonstration
The system SHALL mathematically demonstrate and explain how two visually and structurally distinct images can possess identical or near-identical average intensity values.

#### Scenario: Demonstrate identical mean with different distributions
- **WHEN** analyzing or synthesizing two patterns with identical average intensity but different spatial arrangements and histograms
- **THEN** the system illustrates how spatial distribution and variance differ despite having the same average intensity.

### Requirement: Thresholding and Segmentation Suitability Evaluation
The system SHALL evaluate computed statistics and histogram characteristics (such as bimodality and contrast spread) to determine which image is better suited for global thresholding/segmentation and provide clear justification.

#### Scenario: Evaluate thresholding feasibility
- **WHEN** comparing an image with a bimodal histogram and high contrast against an image with a unimodal or low-contrast histogram
- **THEN** the system identifies the higher contrast / bimodal image as more suitable for thresholding and prints the reasoning.
