## Why

The user requested redoing Part B with a specific focus on retaining the cup, which is black in colour, in contrast to the gray colour of the background and the tones of the holding hand in `cup_holding.jpg`.

## What Changes

- **Part B Redo**: Refine the Part B segmentation pipeline in `test.ipynb` and `lab6_image_segmentation.ipynb` to specifically isolate the black cup.
- **Accurate Grounding**: Target the black cup using seed coordinates ($y=187, x=230$, intensity $\approx 48$) and dark intensity characteristics.
- **Single Method Contrast**: Explicitly contrast the pipeline against single thresholding failures:
  - Global Otsu thresholding cannot distinguish the black cup from the overall person/silhouette.
  - Naive dark thresholding ($I < 80$) incorrectly captures hair and clothing shadows alongside the cup due to lack of spatial localization.
- **Refined Pipeline**: Combine spatially constrained seeded region growing on the black cup with morphological closing/opening to extract the exact cup boundary.
- **Retention & Disappearance**:
  - Retain only the black cup against a clean white/contrasting background.
  - Inpaint the cup region so the black cup disappears naturally while preserving the holding hand and gray background.
- **Updated Observations**: Add detailed discussion explaining how the black cup is discriminated from the gray background and why the hybrid pipeline succeeds where single techniques fail.

## Capabilities

### New Capabilities
- `black-cup-segmentation`: Dedicated segmentation and disappearance pipeline targeting the black cup against the gray background in Part B.

### Modified Capabilities
*(None)*

## Impact

- Updates `test.ipynb` and `lab6_image_segmentation.ipynb`.
- Uses existing image `cup_holding.jpg` without introducing new external dependencies.
