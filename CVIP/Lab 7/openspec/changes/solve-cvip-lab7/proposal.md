## Why

This change provides a clean, concise, and self-contained Jupyter Notebook solution for CVIP Lab Assignment 7 (Radiometry and Image Formation). It addresses all required problems from Part A (excluding questions 4 and 5 as explicitly requested) and Part B, demonstrating fundamental radiometric principles, surface reflection models, image formation, and real/synthetic comparative analysis with minimal, straightforward code.

## What Changes

- Implement Part A Question 1: Simulation of received illumination versus surface area and source distance.
- Implement Part A Question 2: Numerical experiments assessing the individual effects of illumination power, distance, surface orientation, and surface reflectance.
- Implement Part A Question 3: Simulation and comparison of two surfaces with differing reflectance models (diffuse Lambertian vs. specular/glossy Phong) under varying lighting and viewing directions.
- Skip Part A Questions 4 and 5 (as requested by user).
- Implement Part A Question 6: Complete end-to-end simulation of the image-formation pipeline from illumination source to surface reflection and digital pixel values for multiple surface types.
- Implement Part A Question 7: Synthetic scene generation under multiple lighting conditions with intensity profile and histogram comparison.
- Implement Part B: Comparative investigation of an object under direct illumination versus shadow, analyzing brightness, histogram distributions, mean/std statistics, profile variations, and visual appearance.
- Deliver solutions in a clean, standalone Jupyter notebook (`CVIP_Lab7.ipynb`) using standard libraries (`numpy`, `matplotlib`, `scipy`/`cv2` if needed) without boilerplate.

## Capabilities

### New Capabilities
- `radiometry-image-formation`: Core radiometric simulation and experimental analysis routines covering inverse square law, surface reflectance models, image formation pipeline, and comparative illumination analysis.

### Modified Capabilities
<!-- None -->

## Impact

- Modifies `CVIP_Lab7.ipynb` with clean, modular, self-contained code cells for each required problem.
- Uses standard Python scientific libraries (`numpy`, `matplotlib`).
- Does not alter existing standalone scripts or configuration files.
