## Purpose

Provides simple, lightweight grayscale image loading, statistical calculation, histogram extraction, range partitioning, region-of-interest analysis, brightness transformation, and segmentation suitability evaluation using basic C arrays and operations.

## Requirements

### Requirement: Simple Grayscale Image I/O
The system SHALL read and write grayscale image files in PGM (P5 binary) format into memory using a minimal contiguous memory buffer structure without external computer vision dependencies.

#### Scenario: Load valid P5 PGM image into struct
- **WHEN** a valid P5 binary PGM image file is provided
- **THEN** the system parses the dimensions, loads pixel bytes into a simple contiguous array in an `Image` structure, and closes the file.

#### Scenario: Write modified image to P5 PGM
- **WHEN** a modified image is saved to disk
- **THEN** the system outputs a compliant P5 header followed by the binary byte buffer.

### Requirement: Core Image Statistics Computation
The system SHALL calculate basic first- and second-order pixel statistics: width, height, total pixel count, minimum intensity, maximum intensity, dynamic range, mean intensity, variance, and standard deviation (contrast).

#### Scenario: Calculate image metrics
- **WHEN** an image structure is analyzed
- **THEN** the system computes minimum in $[0, 255]$, maximum in $[0, 255]$, mean ($\mu$), variance ($\sigma^2$), and standard deviation ($\sigma$).

### Requirement: 256-Bin Histogram and Range Distribution
The system SHALL calculate a 256-bin frequency histogram and categorize pixels into Dark ($[0, 85]$), Medium ($[86, 170]$), and Bright ($[171, 255]$) intervals with percentage calculations summing to 100.0%.

#### Scenario: Intensity range and histogram calculation
- **WHEN** the image is scanned
- **THEN** each pixel increments its respective 0-255 frequency bin and increments the corresponding Dark, Medium, or Bright partition counter.

### Requirement: Numerical Comparative Evaluation
The system SHALL compare two input images using their numerical mean and standard deviation to determine which image is brighter/darker and which has higher contrast.

#### Scenario: Compare two images
- **WHEN** metrics from both images are compared
- **THEN** the system clearly reports which image is brighter (higher mean) and which has higher contrast (higher standard deviation).

### Requirement: Region of Interest (ROI) Analysis
The system SHALL compute sub-region statistics (min, max, mean, std dev, range percentages) for designated bounding boxes $(x, y, w, h)$ such as center and corner areas.

#### Scenario: Analyze spatial sub-region
- **WHEN** an ROI bounding box is specified within image boundaries
- **THEN** the system computes statistical metrics and dark/med/bright breakdown specifically for pixels within that box.

### Requirement: Brightness Modification with Clamping
The system SHALL add an intensity offset to an image's pixel values, clamp values to $[0, 255]$, and report before-and-after statistics.

#### Scenario: Apply positive brightness offset
- **WHEN** a constant offset (+40) is added to all pixel intensities
- **THEN** pixel values are clamped at 255, mean intensity increases, and the resulting image is saved to disk.

### Requirement: Iso-Mean Demonstration and Segmentation Feasibility
The system SHALL demonstrate through synthetic patterns why visually different images can have the same average intensity, and evaluate histogram properties to justify segmentation suitability.

#### Scenario: Iso-mean demonstration
- **WHEN** a checkerboard pattern (high contrast) and a solid uniform gray pattern are compared
- **THEN** both produce the exact same mean intensity (127.0) despite having radically different standard deviations and spatial layouts.

#### Scenario: Segmentation suitability justification
- **WHEN** evaluating histogram spread and contrast
- **THEN** the system identifies the higher contrast image with distinct dark/bright modes as more suitable for global thresholding.
