# SVNIT Surat - CVIP Lab Assignment 1
**Course:** Computer Vision and Image Processing (`CSCS111` / `CSDS119`)  
**Department:** Computer Science and Engineering Department  
**Topic:** Understanding and Analysing Digital Images Using C  

---

## 1. Problem Statement & Objectives

Given two grayscale images (`sample_01.pgm` and `sample_02.pgm`), write a modular, clean, and dependency-free C program using basic arrays and operations to:
1. **Read and Store:** Load both grayscale images into contiguous arrays without external computer vision libraries.
2. **Compute Dimensions & Statistics:** Determine dimensions ($W \times H$), minimum intensity, maximum intensity, dynamic range, average (mean) intensity, variance, and contrast (standard deviation).
3. **Histogram Generation:** Generate 256-bin intensity histograms and examine the distribution across intensity intervals with ASCII visualization.
4. **Range Partitioning:** Classify pixels into Dark ($[0, 85]$), Medium ($[86, 170]$), and Bright ($[171, 255]$) ranges and calculate percentage distributions.
5. **Numerical Comparison:** Identify which image is brighter, darker, or has higher contrast based on mathematical metrics.
6. **Region of Interest (ROI) Analysis:** Select distinct spatial sub-regions (e.g. Center vs. Corner) and compute dedicated statistical profiles.
7. **Brightness Transformation:** Increase image brightness via constant offset addition with $[0, 255]$ clamping, and analyze before/after statistics and histogram shift.
8. **Iso-mean Study:** Mathematically and experimentally investigate whether two visually different images can share identical average intensity.
9. **Further Processing Suitability:** Evaluate which image is better suited for global thresholding/segmentation (e.g. Otsu's method) and provide scientific reasoning.

---

## 2. Compilation and Execution

### Using Make
```bash
make
make run
```

### Manual Compilation
```bash
gcc -std=c99 -Wall -Wextra -O2 lab1_analysis.c -lm -o lab1_analysis
./lab1_analysis sample_01.pgm sample_02.pgm
```

---

## 3. Detailed Results & Answers to Assignment Questions

### 3.1 Dimensions and Pixel Statistics
| Metric | Image 1 (`sample_01.pgm`) | Image 2 (`sample_02.pgm`) |
| :--- | :--- | :--- |
| **Dimensions ($W \times H$)** | $640 \times 426$ ($272,640$ pixels) | $1280 \times 853$ ($1,091,840$ pixels) |
| **Minimum Intensity** | $0$ | $0$ |
| **Maximum Intensity** | $255$ | $255$ |
| **Dynamic Range** | $255$ | $255$ |
| **Average (Mean) Intensity ($\mu$)** | $98.24$ | $98.13$ |
| **Variance ($\sigma^2$)** | $4039.63$ | $4133.62$ |
| **Contrast / Std Deviation ($\sigma$)** | $63.56$ | $64.29$ |

### 3.2 Intensity Range Breakdown
| Intensity Range | Category | Image 1 Percentage | Image 2 Percentage |
| :--- | :--- | :--- | :--- |
| $[0 - 85]$ | **Dark** | $46.70\%$ ($127,330$ px) | $47.16\%$ ($514,923$ px) |
| $[86 - 170]$ | **Medium** | $35.92\%$ ($97,926$ px) | $35.08\%$ ($383,018$ px) |
| $[171 - 255]$ | **Bright** | $17.39\%$ ($47,384$ px) | $17.76\%$ ($193,899$ px) |
| **Total Check** | - | **$100.00\%$** | **$100.00\%$** |

### 3.3 Numerical Image Comparison
- **Brighter / Darker:** Image 1 has a slightly higher mean intensity ($\mu_1 = 98.24$) compared to Image 2 ($\mu_2 = 98.13$), making **Image 1 marginally brighter** overall and **Image 2 marginally darker** (with higher concentration in lower intensity bands).
- **Contrast:** Image 2 exhibits a higher standard deviation ($\sigma_2 = 64.29$ vs $\sigma_1 = 63.56$), indicating that **Image 2 has higher contrast**.

### 3.4 Region of Interest (ROI) Analysis
- **Center Region (50% area):**
  - Image 1: Mean = $137.89$, Std Dev = $65.11$ (Dark: $23.20\%$, Med: $39.32\%$, Bright: $37.48\%$).
  - Image 2: Mean = $137.83$, Std Dev = $65.64$ (Dark: $23.60\%$, Med: $38.53\%$, Bright: $37.88\%$).
  - *Observation:* The center region in both images is significantly brighter (+$\approx 40$ intensity units above global mean) with balanced distribution across medium and bright tones.
- **Top-Left Corner Region:**
  - Image 1: Mean = $103.92$, Std Dev = $24.32$ (Dark: $24.79\%$, Med: $74.39\%$, Bright: $0.82\%$).
  - Image 2: Mean = $103.95$, Std Dev = $24.73$ (Dark: $25.08\%$, Med: $73.83\%$, Bright: $1.09\%$).
  - *Observation:* Corner regions are predominantly mid-tone ($>73\%$ medium pixels) with low contrast ($\sigma \approx 24$).

### 3.5 Brightness Modification (+40 Offset)
- **Transformation Function:** $I_{\text{new}}(x, y) = \min(255, I_{\text{old}}(x, y) + 40)$
- **Results:**
  - Mean intensity increased from $98.24 \to 137.74$ ($+39.50$).
  - Dark pixel percentage decreased from $46.70\% \to 26.57\%$.
  - Bright pixel percentage increased from $17.39\% \to 30.36\%$.
  - Spatial dimensions ($640 \times 426$) remained unchanged.
  - Output image written to `sample_01_brightened.pgm`.

### 3.6 Iso-Mean Phenomenon Demonstration
- **Question:** *Can two visually different images have the same average intensity?*
- **Answer:** **Yes.** 
- **Proof:**
  - **Pattern A (High-Contrast Checkerboard):** $50\%$ pixels at $0$ and $50\%$ pixels at $254 \implies \mu = 127.00, \sigma = 127.00$.
  - **Pattern B (Uniform Flat Gray):** $100\%$ pixels at $127 \implies \mu = 127.00, \sigma = 0.00$.
- **Scientific Reason:** Average intensity is a first-order statistical moment representing global central tendency. It discards spatial frequency, variance (second-order moment), and spatial arrangement.

### 3.7 Thresholding & Segmentation Suitability
- **Selected Image:** **Image 2 (`sample_02.pgm`)** (or Image 1, as both share similar high-dynamic bimodal characteristics with Image 2 showing slightly higher contrast).
- **Justification:**
  1. **Higher Contrast ($\sigma = 64.29$):** Wider separation between dark background/shadows and illuminated structures.
  2. **Histogram Distribution:** Strong separation between dark ($47.16\%$) and medium/bright modes ($52.84\%$) creates a distinct histogram valley suitable for Otsu's optimal threshold calculation.
  3. **Full Dynamic Span ($[0, 255]$):** Maximizes discrimination capability and minimizes noise-induced false segmentation.
