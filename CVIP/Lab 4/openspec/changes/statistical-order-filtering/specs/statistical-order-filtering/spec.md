## Purpose

Provides statistical order filtering algorithms and comparative evaluation for image noise reduction and detail preservation.

## ADDED Requirements

### Requirement: Statistical Order Filters Implementation
The system SHALL provide implementations of statistical order filtering operations for grayscale images, specifically: median filter, minimum filter, maximum filter, midpoint filter ($\frac{\min + \max}{2}$), alpha-trimmed mean filter, and percentile/rank filters (specifically 25th and 75th percentiles).

#### Scenario: Median filtering applied to neighborhood
- **WHEN** a median filter is executed over an $N \times N$ sliding neighborhood of an image
- **THEN** the center pixel is replaced by the median value of all pixel intensities in that neighborhood

#### Scenario: Min and Max filtering
- **WHEN** min or max filters are executed over an $N \times N$ neighborhood
- **THEN** the center pixel is replaced by the minimum or maximum intensity value within the neighborhood, respectively

#### Scenario: Midpoint filtering
- **WHEN** the midpoint filter is executed over an $N \times N$ neighborhood
- **THEN** the center pixel is replaced by the average of the minimum and maximum pixel values in that neighborhood

#### Scenario: Alpha-trimmed mean filtering
- **WHEN** the alpha-trimmed mean filter is executed with parameter $\alpha$ ($0 < \alpha < 0.5$) or trimming $d$ lowest and highest values
- **THEN** the center pixel is replaced by the mean of the remaining sorted pixel intensities after discarding the extremes

#### Scenario: Percentile rank filtering
- **WHEN** a 25th or 75th percentile filter is executed over an $N \times N$ neighborhood
- **THEN** the center pixel is replaced by the value corresponding to the specified percentile rank in the sorted neighborhood array

### Requirement: Multi-Scale Evaluation across Neighborhood Sizes
The system SHALL evaluate each statistical order filter across different neighborhood window sizes: $3 \times 3$, $5 \times 5$, and $7 \times 7$.

#### Scenario: Multi-scale filtering comparison
- **WHEN** filters are run on noisy Cameraman images with $3 \times 3$, $5 \times 5$, and $7 \times 7$ kernels
- **THEN** filtered images for each size are generated and displayed to illustrate the trade-off between noise reduction and blurring of edges

### Requirement: Clean and Concise Jupyter Notebook Output
The system SHALL provide the entire implementation, visual comparisons, and written observations in a clean, self-contained Jupyter Notebook (`cvip_lab4.ipynb`).

#### Scenario: Notebook execution
- **WHEN** the notebook `cvip_lab4.ipynb` is run sequentially
- **THEN** all code cells execute without errors, load `Filtering-Cameraman.png`, display side-by-side visual results using Matplotlib, and present concise written observations on filter behaviors
