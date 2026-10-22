## Context

In `cup_holding.jpg`, the scene consists of a gray/light-gray background (intensity values $\approx 200\text{--}245$), holding hand and skin tones (intensity values $\approx 150\text{--}210$), and a dark/black cup held in the hand (intensity values $\approx 30\text{--}70$, bounded around rows $[159, 211]$ and columns $[207, 248]$, centered near $y=187, x=230$).

See `proposal.md` and `specs/black-cup-segmentation/spec.md` for background and behavior specifications.

## Goals / Non-Goals

**Goals:**
- Formulate the Part B solution explicitly around isolating the **black cup** in contrast to the **gray background** and hand.
- Visually demonstrate why single segmentation methods fail:
  - Global Otsu ($T = 186$) groups the black cup with the person, clothing, and hand.
  - Direct dark thresholding ($I < 80$) captures the cup but also picks up hair and shadows across the image due to absence of spatial constraints.
- Implement a robust composite pipeline:
  1. Seeded Region Growing anchored at $(187, 230)$ with similarity $\Delta T \approx 25$.
  2. Morphological closing and opening with a $5\times 5$ elliptical kernel to seal any inner reflections and trim border bridges.
  3. Retain only the black cup against a clean white background.
  4. Make the black cup disappear using OpenCV Telea fast-marching inpainting.
- Update `test.ipynb` and `lab6_image_segmentation.ipynb` with clean, self-contained cells and high-quality plots.

**Non-Goals:**
- Changing Part A code or requirements (Part A already satisfies all point, line, edge, threshold, and region growing requirements).
- Adding complex deep learning or heavy external packages.

## Decisions

### 1. Direct Targeting of Black Cup Pixels
- **Decision**: Set the seed point at $(187, 230)$ where intensity is $\approx 48$.
- **Rationale**: This guarantees that region growing begins strictly inside the dark pigment of the cup body, exploiting the steep intensity gradient between the black cup ($\approx 48$) and the holding hand ($\approx 170\text{--}190$) and gray background ($\approx 220$).

### 2. Dual Single-Method Failure Demonstration
- **Decision**: In the Part B demonstration, show both (a) Global Otsu thresholding and (b) Naive dark thresholding ($I < 80$).
- **Rationale**: Otsu fails because it splits the whole image at $T=186$, grouping the entire foreground together. Naive dark thresholding fails because without spatial connectivity, it captures hair at the top of the image and clothing shadows. This proves precisely why the hybrid combination (spatial seed + similarity threshold + morphological cleaning) is necessary.

### 3. Mask Refinement & Disappearance
- **Decision**: Use a $5\times 5$ elliptical structuring element for closing and opening, followed by `cv2.inpaint(..., inpaintRadius=9, flags=cv2.INPAINT_TELEA)`.
- **Rationale**: A $5\times 5$ kernel avoids over-dilating across the holding fingers while ensuring a solid, hole-free mask of the cup.

## Risks / Trade-offs

- **[Inpainting at Hand-Cup Boundary]**: The boundary where fingers grip the cup requires clean mask edges to avoid blurring the fingers during inpainting.
  - *Mitigation*: The morphological opening step severs thin bridges into the fingers before inpainting is applied.
