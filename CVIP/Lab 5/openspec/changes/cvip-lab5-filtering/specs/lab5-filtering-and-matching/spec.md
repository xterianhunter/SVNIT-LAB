## Purpose

Provides simple, clean implementations for spatial filtering, 2D Discrete Fourier Transform analysis, frequency-domain low-pass and high-pass filtering (Ideal, Gaussian, Butterworth), and template matching via cross-correlation for CVIP Lab 5.

## ADDED Requirements

### Requirement: Spatial domain smoothing and sharpening filters
The notebook SHALL apply mean, Gaussian, and Laplacian filters to the Cameraman image using multiple neighborhood sizes and display the resulting images along with comparative observations regarding noise reduction, blur, and edge enhancement.

#### Scenario: Visual comparison of spatial filters across kernel sizes
- **WHEN** spatial filtering code cells are executed on the Cameraman image
- **THEN** the outputs show mean-filtered, Gaussian-filtered, and Laplacian-filtered images across different kernel dimensions (e.g., 3x3, 5x5, 9x9) with concise written observations.

### Requirement: 2D Discrete Fourier Transform and spectrum visualization
The notebook SHALL compute the 2D Discrete Fourier Transform (DFT) of a grayscale image, display its centered magnitude spectrum and phase spectrum, and verify accurate reconstruction using the Inverse DFT (IDFT).

#### Scenario: Computing DFT, spectra, and reconstructing the image
- **WHEN** the 2D DFT is computed on the input grayscale image
- **THEN** the notebook displays the log-magnitude spectrum, phase spectrum, and the reconstructed image matching the original input.

### Requirement: Ideal Low-Pass and High-Pass filtering in DFT domain
The notebook SHALL implement circular Ideal Low-Pass Filter (ILPF) and Ideal High-Pass Filter (IHPF) transfer functions in the centered frequency domain, apply them to the DFT of the image, perform IDFT, and display the filter transfer functions and filtered results across varying cutoff frequencies $D_0$.

#### Scenario: Applying ILPF and IHPF with multiple cutoff frequencies
- **WHEN** ILPF and IHPF are applied with different cutoff frequencies $D_0$
- **THEN** the notebook displays the filter transfer function magnitude, original image, and filtered results showing smoothing/ringing for ILPF and high-frequency edge isolation for IHPF.

### Requirement: Gaussian Low-Pass and High-Pass filtering in DFT domain
The notebook SHALL implement Gaussian Low-Pass (GLPF) and Gaussian High-Pass (GHPF) filters in the frequency domain, apply them to the image DFT, reconstruct via IDFT, and compare the smooth transition behavior against ideal filters.

#### Scenario: Applying GLPF and GHPF with multiple cutoff frequencies
- **WHEN** GLPF and GHPF are evaluated at different cutoff thresholds $D_0$
- **THEN** the notebook renders the filtered images without ringing artifacts and provides observations comparing Gaussian against Ideal filters.

### Requirement: Butterworth Low-Pass and High-Pass filtering in DFT domain
The notebook SHALL implement Butterworth Low-Pass (BLPF) and Butterworth High-Pass (BHPF) filters in the frequency domain, evaluate the effect of varying cutoff frequency $D_0$ and filter order $n$, and document comparative observations among Ideal, Gaussian, and Butterworth filters.

#### Scenario: Applying BLPF and BHPF with varying cutoff and order
- **WHEN** BLPF and BHPF are applied with different cutoff frequencies $D_0$ and orders $n$
- **THEN** the notebook displays filtered outputs demonstrating the transition steepness and compares ringing behavior across Ideal, Gaussian, and Butterworth filters.

### Requirement: Cross-Correlation template matching
The notebook SHALL perform template matching via cross-correlation between a provided grocery shelf image and a product template image, locate the maximum correlation response, and draw a blue bounding box around the detected item.

#### Scenario: Detecting product on shelf using cross-correlation
- **WHEN** cross-correlation matching is run on the shelf and template images
- **THEN** the detected match location is highlighted with a blue rectangle on the shelf image and observations regarding matching accuracy are presented.
