## Context

See `proposal.md` and `specs/lab5-filtering-and-matching/spec.md`. The lab assignment consists of two parts:
- Part A: Spatial filtering (Mean, Gaussian, Laplacian) and Frequency domain filtering (2D DFT, ILPF, IHPF, GLPF, GHPF, BLPF, BHPF) on the Cameraman image.
- Part B: Template matching of a product on a shelf using cross-correlation, marked with a blue bounding box.

The user explicitly requested: "give a simple ipynb code as simple as possible don't overdo anythinf don't put anything that is not necesary and solve the problems given in CVIP_LAB5.pdf".

## Goals / Non-Goals

**Goals:**
- Implement all required tasks from Part A and Part B in a single, simple, readable `.ipynb` notebook (`lab5_solution.ipynb`).
- Maintain clean, minimal code without unnecessary classes, boilerplate, or external heavy dependencies.
- Provide clear visual plots for all filtering stages and magnitude/phase spectra.
- Include concise, required observations on noise reduction, blur, ringing artifacts, and edge enhancement.
- Accurately run cross-correlation template matching between the provided shelf image and product template.

**Non-Goals:**
- Creating custom command-line interfaces or GUI applications.
- Complex multi-scale or invariant feature extraction pipelines (standard cross-correlation is specified).
- Over-engineered utility packages or excessive lines of code.

## Decisions

### Decision 1: Use NumPy FFT (`np.fft.fft2`, `fftshift`, `ifft2`) for frequency domain filtering
- **Rationale**: It provides standard, transparent mathematical operations directly corresponding to the equations given in the assignment.
- **Alternatives considered**: OpenCV's `cv2.dft` (more cumbersome with 2-channel complex representation) and custom $O(N^4)$ DFT loops (too slow for 2D images).

### Decision 2: Standardized frequency distance grid calculation
- **Rationale**: For an image of shape $(M, N)$, center coordinates $(u_0, v_0) = (M/2, N/2)$, compute Euclidean distance matrix $D(u,v) = \sqrt{(u - u_0)^2 + (v - v_0)^2}$. This unified distance array simplifies ILPF, IHPF, GLPF, GHPF, BLPF, and BHPF transfer functions to 1-2 lines of vector operations each.

### Decision 3: Template matching using normalized cross-correlation
- **Rationale**: `cv2.matchTemplate` with `cv2.TM_CCORR_NORMED` directly solves Part B cleanly and accurately, identifying the peak correlation location and drawing the bounding box with `cv2.rectangle(..., color=(255, 0, 0), thickness=2)`.
- **Alternatives considered**: Unnormalized cross-correlation (susceptible to bright background regions).

### Decision 4: Cameraman image source handling
- **Rationale**: If a local `cameraman.png` or `cameraman.tif` is not present in the workspace, use `skimage.data.camera()` (or fetch it via urllib) so the notebook executes out-of-the-box without manual downloads.

## Risks / Trade-offs

- **[Risk] High-pass filtered images have negative values / low contrast** → *Mitigation*: Normalize or clip outputs appropriately to $[0, 255]$ for display.
- **[Risk] Dimension mismatch in template matching** → *Mitigation*: Read `product.png` and `organized-product-display-stockcake.jpg` in grayscale, verify shapes, and ensure template is smaller than the target shelf.
