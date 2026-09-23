## Purpose

Provides image segmentation algorithms and an experimental pipeline for point, line, edge, threshold-based, and region-based segmentation on user images.

## ADDED Requirements

### Requirement: Point and Line Detection
The system SHALL apply point detection and directional line detection masks (horizontal, vertical, +45 degrees, -45 degrees) to detect prominent spatial discontinuities in the input image.

#### Scenario: Running point and line detection on input image
- **WHEN** point and directional line detection filters are applied to the grayscale image of `cup_holding.jpg`
- **THEN** filtered feature maps for isolated points, horizontal lines, vertical lines, and diagonal lines (+45° and -45°) SHALL be generated and displayed.

### Requirement: Classical Edge Detection
The system SHALL compute edge boundary representations using Roberts Cross, Prewitt, Sobel, and Laplacian spatial operators.

#### Scenario: Comparing edge detection operators
- **WHEN** Roberts, Prewitt, Sobel, and Laplacian operators are applied to `cup_holding.jpg`
- **THEN** gradient magnitude and zero-crossing/Laplacian responses SHALL show structural boundaries of both the person and the held object.

### Requirement: Global and Otsu Thresholding
The system SHALL segment the image into foreground and background using basic iterative Global Thresholding and Otsu's optimal variance thresholding.

#### Scenario: Thresholding comparison
- **WHEN** Global thresholding and Otsu thresholding are executed on the grayscale image
- **THEN** binary masks and the computed threshold values for both methods SHALL be produced and visually contrasted.

### Requirement: Region Growing Segmentation
The system SHALL implement region-based segmentation using region growing with configurable seed locations and intensity distance tolerances.

#### Scenario: Seed point and criterion sensitivity analysis
- **WHEN** region growing is executed with different seed coordinates (e.g., inside the cup vs on clothing/background) and differing intensity thresholds ($\Delta T$)
- **THEN** the resulting segmented regions SHALL demonstrate how seed placement and similarity tolerance govern region expansion and leakage.

### Requirement: Object Isolation and Disappearance Pipeline
The system SHALL implement a multi-stage segmentation pipeline to selectively isolate the target object (cup) and alternately remove/disappear it from the image while handling background intensity confusion.

#### Scenario: Isolate object from background
- **WHEN** the composite segmentation pipeline is applied to `cup_holding.jpg`
- **THEN** a final mask isolating the cup SHALL be generated, producing an image where the cup is retained and the rest is suppressed.

#### Scenario: Make object disappear
- **WHEN** the inverted object mask is applied to `cup_holding.jpg`
- **THEN** an output image where the cup is removed/inpainted or replaced while background context is preserved SHALL be generated.

### Requirement: Results Display and Analytical Observations
The system SHALL display input images, intermediate outputs, and final results side-by-side with written analytical observations explaining method performance.

#### Scenario: Displaying all results with observations
- **WHEN** the notebook cells are evaluated
- **THEN** visual comparison figures SHALL be rendered alongside textual explanations detailing which techniques best segment the object and why.
