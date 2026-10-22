## Why

Implement the requirements of CVIP Lab Assignment 6 (Image Segmentation) for M.Tech CSE/DS at SVNIT. The assignment requires exploring classical spatial segmentation techniques (point, line, edge, thresholding, and region growing) and designing a composite segmentation pipeline to isolate or make an object disappear from an input image (`cup_holding.jpg`) in a clean, self-contained Jupyter Notebook with straightforward, minimal code.

## What Changes

- Create a self-contained Jupyter notebook (`lab6_image_segmentation.ipynb` or updating `test.ipynb`) containing simple, direct implementations for all assignment parts using `cup_holding.jpg`.
- **Part A.1: Point and Line Detection**: Apply point detection mask and directional line detection masks (horizontal, vertical, +45°, -45°) to detect prominent features.
- **Part A.2: Edge Detection**: Apply Roberts, Prewitt, Sobel, and Laplacian spatial edge operators, comparing boundary detection on the person and cup.
- **Part A.3: Thresholding-Based Segmentation**: Implement and compare basic Global Thresholding and Otsu's automated thresholding method.
- **Part A.4: Region-Based Segmentation**: Implement region growing segmentation and evaluate the effect of different seed points and similarity criteria ($\Delta T$).
- **Part A.5: Display & Observations**: Visual comparisons and concise analytical commentary on segmentation effectiveness.
- **Part B: Object Disappearance / Isolation Pipeline**: Build a composite segmentation pipeline combining color/intensity thresholding, morphological filtering, and masking to isolate the cup (or make it disappear) even with background intensity overlap, contrasting against single-technique failures.

## Capabilities

### New Capabilities
- `image-segmentation`: Classical point/line/edge masks, global and Otsu thresholding, region growing, and composite object extraction/disappearance pipeline with visual results and observations.

### Modified Capabilities
*(None)*

## Impact

- **Notebook**: Creates `lab6_image_segmentation.ipynb` (or populates `test.ipynb`).
- **Dependencies**: Python 3 with `numpy`, `opencv-python` / `cv2` (or PIL fallback), and `matplotlib`.
- **Assets**: Utilizes local `cup_holding.jpg`.
