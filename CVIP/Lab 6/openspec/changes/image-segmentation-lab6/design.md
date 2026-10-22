## Context

The assignment requires implementing classical spatial segmentation and feature extraction techniques on `cup_holding.jpg` in a Jupyter Notebook. The implementation must be kept simple, concise, and focused strictly on the assignment instructions without unnecessary complexity or dependencies.

See `proposal.md` and `specs/image-segmentation/spec.md` for background and behavior specifications.

## Goals / Non-Goals

**Goals:**
- Provide clear, simple Python code in a Jupyter Notebook (`lab6_image_segmentation.ipynb` or populating `test.ipynb`).
- Implement spatial convolutions for point and line detection using classical 3x3 kernels (horizontal, vertical, +45°, -45°).
- Implement spatial edge detection comparing Roberts, Prewitt, Sobel, and Laplacian operators.
- Implement and compare iterative Global Thresholding and Otsu's thresholding.
- Implement a clear Region Growing routine demonstrating sensitivity to seed coordinates and similarity threshold $\Delta T$.
- Design a compact Part B segmentation pipeline combining color/intensity thresholds with morphological filtering to retain only the cup or make it disappear, contrasting with single-method failure modes.
- Include clear visual displays and concise analytical observations for every section.

**Non-Goals:**
- Deep learning or modern neural network segmentation frameworks (e.g., SAM, Mask R-CNN).
- Complex GUI applications or interactive widgets.
- Over-engineered class hierarchies; pure functional/scripted notebook cells are preferred.

## Decisions

### 1. Execution Environment & Notebook Format
- **Decision**: Deliver the solution directly in a Jupyter Notebook format (`.ipynb`), writing standard cells with markdown headers and clean code blocks.
- **Rationale**: Meets the user's explicit request ("solve the problems given in it in a ipynb file... give simple codes").

### 2. Standard Libraries
- **Decision**: Rely on Python standard imaging libraries: `numpy`, `matplotlib.pyplot`, and `cv2` (OpenCV) / `PIL`.
- **Rationale**: Built-in functions for reading/writing images are explicitly permitted by the assignment prompt ("Note: For reading and writing images, you may use built-in functions from OpenCV or any other library you use"). Convolutions and mathematical operations will use simple `cv2.filter2D` or basic numpy slicing to keep code short and robust.

### 3. Mask Definitions
- **Point Detection**:
  $$\begin{bmatrix} -1 & -1 & -1 \\ -1 & 8 & -1 \\ -1 & -1 & -1 \end{bmatrix}$$
- **Directional Lines**:
  - Horizontal: $\begin{bmatrix} -1 & -1 & -1 \\ 2 & 2 & 2 \\ -1 & -1 & -1 \end{bmatrix}$
  - Vertical: $\begin{bmatrix} -1 & 2 & -1 \\ -1 & 2 & -1 \\ -1 & 2 & -1 \end{bmatrix}$
  - $+45^\circ$: $\begin{bmatrix} -1 & -1 & 2 \\ -1 & 2 & -1 \\ 2 & -1 & -1 \end{bmatrix}$
  - $-45^\circ$: $\begin{bmatrix} 2 & -1 & -1 \\ -1 & 2 & -1 \\ -1 & -1 & 2 \end{bmatrix}$
- **Edge Operators**:
  - Roberts: $2\times 2$ diagonal gradient kernels.
  - Prewitt: $3\times 3$ horizontal and vertical finite difference kernels.
  - Sobel: $3\times 3$ smoothed gradient kernels.
  - Laplacian: standard second-derivative isotropic kernel.

### 4. Part B Segmentation Strategy
- **Decision**: Combine color/HSV or intensity thresholding with morphological operations (opening to remove isolated noise, closing to fill holes) and connected component / contour filtering to isolate the cup region. To make the object disappear, fill the cup region using surrounding background patch interpolation or inpainting.
- **Rationale**: Single global thresholding fails when the object shares intensity with background regions (as noted in Part B). Combining spatial localized constraints and morphological cleanup solves the ambiguity directly and simply.

## Risks / Trade-offs

- **[Dependency Availability]**: System Python may lack `cv2` or `matplotlib`.
  - *Mitigation*: Ensure user environment has necessary packages installed via standard pip/venv if needed, or provide fallback routines using PIL/NumPy.
- **[Seed Point Sensitivity in Region Growing]**: Region growing can easily leak across weak boundaries if similarity threshold $T$ is set too high.
  - *Mitigation*: Demonstrate this exact behavior empirically in the notebook to address Part A.4's explicit instruction to investigate sensitivity.
