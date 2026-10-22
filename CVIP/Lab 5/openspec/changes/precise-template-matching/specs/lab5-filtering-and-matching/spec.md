## Purpose

Provides high-precision multi-scale cross-correlation template matching to accurately detect the target product on the shelf image and highlight it with a blue bounding box.

## ADDED Requirements

### Requirement: Precise Multi-scale Cross-Correlation Template Matching
The template matching implementation SHALL search across multiple candidate template scales using normalized cross-correlation or normalized correlation coefficient to locate the global maximum similarity response on the shelf image.

#### Scenario: Accurate detection of target product across scale variations
- **WHEN** multi-scale template matching is evaluated on the shelf image across varying template scales
- **THEN** the system detects the true product instance with peak correlation > 0.90 at coordinates $(247, 235)$ and draws a blue bounding box accurately enclosing the item.

#### Scenario: Highlighting comparison between single-scale and multi-scale matching
- **WHEN** single-scale and multi-scale template matching results are evaluated
- **THEN** the notebook documents the scale discrepancy and demonstrates how multi-scale matching resolves false detections.
