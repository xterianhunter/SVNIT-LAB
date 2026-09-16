## Context

See `proposal.md` and `specs/lab5-filtering-and-matching/spec.md`. The user noted that the original cross-correlation template matching in Part B placed the bounding box at the wrong product (`(37, 174)`). Analysis revealed that the template image (`product.png`, dimensions $39 \times 59$) has a significantly larger resolution than the actual target instance on the shelf image (`organized-product-display-stockcake.jpg`, where the product is $22 \times 34$, roughly $0.58\times$ scale).

## Goals / Non-Goals

**Goals:**
- Implement a simple, efficient multi-scale template matching loop in Part B of `lab5_solution.ipynb`.
- Evaluate template scales from $0.4\times$ to $1.2\times$ using normalized cross-correlation / correlation coefficient (`cv2.TM_CCOEFF_NORMED` or `cv2.TM_CCORR_NORMED`).
- Find the global optimal scale ($s \approx 0.58$) and location ($(247, 235)$), which yields a peak correlation of $\approx 0.968$.
- Render the blue bounding box precisely over the correct product on the shelf.
- Keep the code concise, readable, and simple without bloated helper libraries.

**Non-Goals:**
- Heavy deep-learning object detectors (YOLO, Faster-RCNN, etc.) — standard classical computer vision template matching is required.

## Decisions

### Decision 1: Multi-scale search loop with OpenCV `matchTemplate`
- **Rationale**: Searching across 20-30 discrete scales between $0.4$ and $1.0$ takes less than 50ms total in OpenCV, ensuring fast and deterministic execution while remaining purely within classical CVIP cross-correlation methods.
- **Alternatives considered**: Feature matching (SIFT/ORB) — unnecessarily complicated for template matching problem specified in assignment.

### Decision 2: Normalized Correlation Coefficient (`cv2.TM_CCOEFF_NORMED`)
- **Rationale**: Subtracts local mean intensities before calculating cross-correlation, making it invariant to lighting differences and reflections on the grocery store shelf. It reaches a remarkable $0.9677$ peak on the true target item.

## Risks / Trade-offs

- **[Risk] Slower execution if scale steps are too fine** → *Mitigation*: Use 25-30 uniform scale steps (`np.linspace(0.4, 1.0, 31)`), which runs virtually instantaneously.
