## 1. Environment & Notebook Setup

- [x] 1.1 Verify image reading of `cup_holding.jpg` and ensure necessary Python imaging dependencies (`numpy`, `matplotlib`, `opencv-python` / `PIL`) are configured in the environment
- [x] 1.2 Initialize clean notebook structure in `test.ipynb` (or `lab6_image_segmentation.ipynb`) with markdown section headers, imports, and image loading helper

## 2. Part A: Point, Line, Edge, Threshold, and Region Segmentation

- [x] 2.1 Implement point detection and directional line detection masks (horizontal, vertical, +45°, -45°) and verify feature maps display expected directional responses
- [x] 2.2 Implement spatial edge detection operators (Roberts Cross, Prewitt, Sobel, Laplacian) and verify side-by-side boundary visualization
- [x] 2.3 Implement basic iterative Global Thresholding and Otsu's thresholding, displaying binary segmented masks and reporting threshold values
- [x] 2.4 Implement Region Growing segmentation and verify sensitivity to seed location and similarity threshold ($\Delta T$) through comparative plots
- [x] 2.5 Add concise analytical observations comparing the performance and limitations of each technique in separating the object from background

## 3. Part B: Object Isolation & Disappearance Pipeline

- [x] 3.1 Implement composite segmentation pipeline combining color/intensity thresholding with morphological operations and contour filtering to cleanly isolate the cup
- [x] 3.2 Implement object disappearance operation (inpainting or masked background replacement) to remove the cup from the scene
- [x] 3.3 Add comparative analysis demonstrating why single-technique segmentation fails on intensity overlap and why the composite pipeline succeeds

## 4. Final Verification

- [x] 4.1 Run the entire notebook sequentially and verify that all cells evaluate successfully, plots render clearly, and all assignment requirements from the lab sheet are fulfilled
