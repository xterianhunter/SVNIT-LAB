## Purpose

Provides radiometric simulations and empirical image-formation experiments covering irradiance falloff, surface reflection characteristics, synthetic sensor pipelines, and comparative lighting analysis.

## ADDED Requirements

### Requirement: Illumination vs Distance and Area Simulation
The system SHALL compute and visualize irradiance and total received radiant flux across varying surface distances and receiver surface areas according to the inverse-square law.

#### Scenario: Distance and area variation
- **WHEN** receiver distance $d$ varies from 1 to 10 meters and surface area $A$ varies from 0.5 to 8.0 m² for a point source
- **THEN** irradiance decreases inversely with $d^2$, and received radiant flux scales proportionally to $A/d^2$ with corresponding graphical curves

### Requirement: Multi-Parameter Radiometric Sensitivity
The system SHALL evaluate the isolated impact of radiation power, source-surface distance, surface normal inclination angle, and surface albedo on received irradiance.

#### Scenario: One-at-a-time parameter sweeps
- **WHEN** radiation power, distance, incidence angle ($\cos \theta$), or reflectance is varied while holding other parameters fixed
- **THEN** irradiance exhibits linear dependence on source power and $\cos\theta$, and inverse-quadratic dependence on distance

### Requirement: Diffuse vs Specular Surface Reflectance Simulation
The system SHALL simulate and contrast outgoing radiance from a Lambertian diffuse surface and a specular (Phong/Blinn-Phong) surface across varying incident light angles and viewing angles.

#### Scenario: Varying illumination and viewing angles
- **WHEN** the light source vector or viewing vector is altered across an angular range
- **THEN** diffuse surface intensity depends solely on incidence angle and is view-independent, whereas specular surface intensity peaks sharply around the reflection direction

### Requirement: Complete Image Formation Pipeline Simulation
The system SHALL simulate the conversion of incident light on distinct surface patches through optical attenuation, exposure integration, and quantization into digital pixel values (0–255).

#### Scenario: Processing multiple surface types through sensor pipeline
- **WHEN** scene patches with distinct albedo/reflectance profiles are exposed under varying illumination levels
- **THEN** the pipeline outputs simulated 8-bit digital pixel values reflecting source intensity, surface reflectance, and sensor quantization

### Requirement: Synthetic Scene Illumination and Comparative Analysis
The system SHALL synthesize images of a geometric scene under at least two distinct illumination conditions and compare them using intensity profiles and pixel histograms.

#### Scenario: Comparing scenes under different lighting conditions
- **WHEN** synthetic images under direct, oblique, or attenuated illumination are analyzed
- **THEN** horizontal intensity profiles and intensity histograms clearly demonstrate shifts in contrast, dynamic range, and shadow/highlight regions

### Requirement: Real or Synthetic Object Direct vs Shadow Comparative Investigation
The system SHALL analyze an object captured or rendered under direct illumination and shadowed conditions, evaluating overall brightness, intensity distribution, statistical moments (mean, standard deviation), and localized surface variations.

#### Scenario: Evaluating direct vs shadow image metrics
- **WHEN** direct illumination and shadow images are evaluated
- **THEN** quantitative statistics (mean, std) and visual distribution plots (histograms and cross-section profiles) reveal the radiometric differences between directly illuminated and shadowed regions
