## 1. Single Technique Failure Analysis

- [x] 1.1 Implement and display failure modes of single thresholding techniques (Global Otsu merging foreground, and Naive dark thresholding $I < 80$ capturing hair and shadows) when attempting to isolate the black cup from the gray background

## 2. Refined Black Cup Pipeline Implementation

- [x] 2.1 Implement the composite pipeline targeting the black cup using seed $(187, 230)$, calibrated $\Delta T \approx 25$, and $5\times 5$ morphological closing and opening
- [x] 2.2 Generate the Object Retained image (black cup isolated on contrasting white background) and Object Disappeared image (Telea inpainting removing the black cup)
- [x] 2.3 Add structured analytical observations explaining why the localized hybrid pipeline isolates the black cup from the gray background and hand whereas single thresholding fails

## 3. Notebook Updates & Verification

- [x] 3.1 Update and evaluate both `test.ipynb` and `lab6_image_segmentation.ipynb`, verifying that all cells run cleanly and all figures render properly
