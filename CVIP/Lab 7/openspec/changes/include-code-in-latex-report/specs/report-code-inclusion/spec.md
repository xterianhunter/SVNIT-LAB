## Purpose

Provides complete, properly formatted, and reproducible Python source code listings within the CVIP Lab 7 LaTeX report across all theoretical and experimental questions.

## ADDED Requirements

### Requirement: Complete Radiometry and Inverse Square Law Code Listing
The LaTeX report SHALL include the complete Python code for irradiance and flux calculation versus distance and surface area in Part A, Question 1.

#### Scenario: Viewing Part A Q1 code
- **WHEN** the user inspects Part A Section 1 in the compiled PDF or LaTeX source
- **THEN** it displays the complete Python code implementing $E = I/d^2$ and $\Phi = I \cdot A / d^2$ alongside its visualization commands.

### Requirement: Complete Parameter Sensitivity Analysis Code Listing
The LaTeX report SHALL include the complete Python implementation of the multi-parameter sensitivity analysis in Part A, Question 2 without cutoff or truncated lines.

#### Scenario: Viewing Part A Q2 code
- **WHEN** the user inspects Part A Section 2 in the compiled report
- **THEN** it displays the complete `calc_intensity` function, parameter sweeps for power $P$, distance $d$, angle $\theta$, and reflectance $\rho$, and the 4-subplot generation code.

### Requirement: Complete Surface Reflectance Simulation Code Listing
The LaTeX report SHALL include the complete Python implementation for Lambertian diffuse versus specular (Phong) reflection modeling in Part A, Question 3.

#### Scenario: Viewing Part A Q3 code
- **WHEN** the user inspects Part A Section 3 in the compiled report
- **THEN** it displays both viewing angle sweep and illumination angle sweep calculations and comparison plotting code.

### Requirement: Complete Image Formation Pipeline Code Listing
The LaTeX report SHALL include the complete Python code for scene radiance calculation, optical transfer, sensor gain, exposure time integration, and 8-bit quantization/saturation in Part A, Question 6.

#### Scenario: Viewing Part A Q6 code
- **WHEN** the user inspects Part A Section 6 in the compiled report
- **THEN** it displays the `simulate_image_formation` function, the illumination range evaluation for matte vs. glossy surfaces, and response curve plotting.

### Requirement: Complete Synthetic 3D Scene Simulation Code Listing
The LaTeX report SHALL include the complete Python code for synthetic hemispherical scene generation and dual-illumination analysis in Part A, Question 7.

#### Scenario: Viewing Part A Q7 code
- **WHEN** the user inspects Part A Section 7 in the compiled report
- **THEN** it displays 3D surface normal derivation, direct overhead and oblique light rendering, difference map computation, row 80 profile extraction, and histogram generation code.

### Requirement: Complete Experimental Investigation Code Listing
The LaTeX report SHALL include the complete Python implementation of the Part B experimental comparison between direct illumination and shadowed conditions.

#### Scenario: Viewing Part B experimental code
- **WHEN** the user inspects Part B in the compiled report
- **THEN** it displays noisy scene simulation, statistical metric calculations (mean and standard deviation), and 4-panel comparison visualization code.

### Requirement: Error-Free Document Compilation
The LaTeX source file SHALL compile with `pdflatex` into an updated PDF report without listings syntax errors, unescaped characters, or layout defects.

#### Scenario: Compiling LaTeX document
- **WHEN** `pdflatex CVIP_Lab7_Report.tex` is executed
- **THEN** it terminates with exit code 0 and produces an updated, readable PDF report.
