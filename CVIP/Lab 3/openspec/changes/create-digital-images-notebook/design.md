## Context

The workspace contains the reference lab manual `CVIP_Lab_3_Understanding_Digital_Images-Copy1.pdf`, an input test image `sample.jpg`, and an existing scratch notebook `Lab3_assignment.ipynb` that contains partial code, syntax errors, and bloated output cells (~29MB). A clean, valid, standard Jupyter Notebook format (`Lab3_Understanding_Digital_Images.ipynb`) must be generated, implementing Parts 1 through 14 accurately, concisely, and cleanly.

## Goals / Non-Goals

**Goals:**
- Generate a standalone, standards-compliant Jupyter Notebook (`.ipynb` v4 format) matching the structure and theoretical progression of the lab PDF.
- Implement both tutorial cells and all 11 `#add your code here` exercises with clean, idiomatic NumPy and OpenCV code.
- Ensure the notebook executes cleanly against `sample.jpg` in local Jupyter and Google Colab environments.
- Include all conceptual questions and markdown callouts ("Think Before Moving Ahead", "Critical Thinking", "Investigation") for complete academic submission readiness.

**Non-Goals:**
- Not modifying `sample.jpg` or the reference PDF.
- Not adding external third-party frameworks or bloated custom algorithms where standard OpenCV/NumPy functions are expected.
- Not generating giant debug logs or unformatted pixel dumps that inflate the notebook file size.

## Decisions

### 1. Notebook File Name and Format
- **Decision**: Create `Lab3_Understanding_Digital_Images.ipynb` following the standard Jupyter nbformat schema (version 4, minor 4) with Python 3 kernel metadata.
- **Alternatives considered**: Modifying `Lab3_assignment.ipynb` directly. Creating a fresh file is much cleaner and avoids carrying over the 29MB bloat and corrupt cell outputs.

### 2. Image Ingestion Strategy (Part 2)
- **Decision**: Maintain Colab upload compatibility via `try/except ImportError`, defaulting directly to `filename = "sample.jpg"` in local environments.
- **Alternatives considered**: Hardcoding `sample.jpg` only. Retaining Colab upload handling matches the PDF specification while ensuring zero-input execution locally.

### 3. Implementation of Exercise Blocks (`#add your code here`)
- **Part 5 (Matrix inspection & pixel access)**:
  - Print matrix slice (e.g. `gray[:5, :5]`) to illustrate grayscale intensity values as numerical data.
  - Demonstrate row-major indexing `gray[y, x]` with a sample coordinate.
- **Part 6 (Modify single pixel)**:
  - Copy grayscale image: `mod_img = gray.copy()`, assign `mod_img[100, 100] = 255`.
  - Contrast with original and provide concise explanation why 1 pixel in thousands is imperceptible.
- **Part 7 (Negative transformation)**:
  - Compute vectorized linear inversion `neg = 255 - gray`.
  - Display with Matplotlib side-by-side with grayscale.
- **Part 8 (Brightness transformation)**:
  - Compute `bright = np.clip(gray.astype(np.int16) + 50, 0, 255).astype(np.uint8)`.
  - Prevents uint8 modulo wrap-around overflow.
- **Part 9 (Thresholding investigation)**:
  - Use `cv2.threshold` or NumPy boolean indexing across $T \in [50, 100, 180, 220]$.
  - Plot a $1\times4$ subplot grid comparing the resulting binary masks.
- **Part 10 (Histogram)**:
  - Plot intensity distribution using `plt.hist(gray.ravel(), bins=256, range=[0, 256], color='gray')`.
- **Part 11 (Cropping & Resizing)**:
  - Crop subregion using NumPy slicing `gray[h//4:3*h//4, w//4:3*w//4]`.
  - Resize with `cv2.resize(gray, (w // 2, h // 2))`.
- **Part 12 (Salt-and-Pepper Noise)**:
  - Add impulse noise using vectorized random indexing (~5% density: 2.5% salt at 255, 2.5% pepper at 0).
- **Part 13 (Mean vs Median Filtering)**:
  - Apply `cv2.blur(noisy, (3, 3))` (mean filter) and `cv2.medianBlur(noisy, 3)` (median filter).
  - Plot Noisy, Mean Filtered, and Median Filtered images in a $1\times3$ grid.
- **Part 14 (Manual Order-Statistic Verification)**:
  - Create $3\times3$ neighborhood array `np.array([[42, 43, 44], [43, 255, 45], [44, 45, 46]])`.
  - Calculate `min`, `max`, `median`, `mean`, and `midpoint = (int(max) + int(min)) / 2.0`.

## Risks / Trade-offs

- **[Risk] Slicing coordinates out of bounds on arbitrary image dimensions**  
  → *Mitigation*: Use relative coordinate calculations (`h//4:3*h//4`, `w//4:3*w//4`) so cropping works cleanly regardless of input image aspect ratio or resolution.
- **[Risk] Integer overflow during brightness transformation**  
  → *Mitigation*: Cast array to signed 16-bit integer before addition, then apply `np.clip` before casting back to `uint8`.
