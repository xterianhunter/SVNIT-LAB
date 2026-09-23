## Purpose

Provides focused segmentation and disappearance of the black cup held in hand in contrast to the surrounding gray background and skin tones.

## ADDED Requirements

### Requirement: Black Cup Intensity Characterization
The system SHALL characterize the black cup pixels (intensities $\approx 30\text{--}70$) distinct from the surrounding gray background (intensities $\approx 200\text{--}245$) and holding hand (intensities $\approx 150\text{--}210$).

#### Scenario: Inspecting black cup intensity range
- **WHEN** the image pixels in `cup_holding.jpg` are analyzed
- **THEN** the black cup SHALL be identified as a dark foreground cluster centered around row $187$ and column $230$.

### Requirement: Single Technique Failure Demonstration on Black Cup
The system SHALL demonstrate the failure modes of single thresholding techniques when attempting to isolate the black cup.

#### Scenario: Global Otsu failure
- **WHEN** global Otsu thresholding is applied
- **THEN** the generated mask SHALL merge the person, clothing, hand, and cup into a single undifferentiated segment.

#### Scenario: Naive dark thresholding failure
- **WHEN** naive dark intensity thresholding ($I < 80$) is applied without spatial localization
- **THEN** hair pixels and clothing shadow regions SHALL be incorrectly included alongside the cup.

### Requirement: Localized Composite Pipeline for Black Cup
The system SHALL isolate the black cup using a combination of seeded region growing starting inside the cup and morphological operations.

#### Scenario: Segmenting the black cup
- **WHEN** region growing with seed $(187, 230)$ and calibrated similarity threshold $\Delta T \approx 25$ is evaluated followed by morphological closing and opening
- **THEN** a precise binary mask covering exclusively the black cup SHALL be produced.

### Requirement: Black Cup Retention and Disappearance Outputs
The system SHALL generate both an object-retained output (black cup isolated on contrasting white background) and an object-disappeared output (black cup removed via inpainting).

#### Scenario: Retaining black cup
- **WHEN** the black cup mask is applied to the original color image
- **THEN** only the black cup SHALL be retained while non-cup pixels are suppressed.

#### Scenario: Making black cup disappear
- **WHEN** inpainting is performed across the black cup mask
- **THEN** the resulting image SHALL show the scene with the cup cleanly removed and background/hand context preserved.
