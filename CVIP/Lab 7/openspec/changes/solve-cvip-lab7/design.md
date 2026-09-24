## Context

See `proposal.md` for background and problem scope. The solution must be implemented in a clean, readable Jupyter Notebook (`CVIP_Lab7.ipynb`), solving CVIP Lab 7 Part A (Questions 1, 2, 3, 6, 7) and Part B (omitting Questions 4 and 5).

## Goals / Non-Goals

**Goals:**
- Provide short, clean, mathematically sound Python implementations using only `numpy` and `matplotlib`.
- Organize the notebook into clear, labeled sections corresponding to each required lab problem.
- Include concise markdown explanations of observations for each experiment.
- For Part B, implement a self-contained synthetic object (e.g. 3D shaded sphere with surface texture) rendered under direct illumination and shadowed conditions to allow repeatable, robust statistical and perceptual comparisons.

**Non-Goals:**
- Do not implement Part A Question 4 (diffuse parameter investigation) or Part A Question 5 (camera parameters), as explicitly excluded.
- Avoid large external dependencies, complex ray-tracing libraries, or unnecessary GUI toolkits.
- Avoid cluttered or bloated code; keep functions and formulas minimal and directly illustrative of radiometry concepts.

## Decisions

### Decision: Notebook Structure and Code Simplicity
- **Choice**: Structure `CVIP_Lab7.ipynb` with clear Markdown headers for Part A (Q1, Q2, Q3, Q6, Q7) and Part B, followed by concise, executable Python code cells.
- **Rationale**: Meets the user's explicit requirement for "simple solution code... short and simple, don't include anything unnecessary".
- **Alternative Considered**: Multiple standalone Python scripts; rejected because an interactive notebook provides inline plots and direct readability for lab submissions.

### Decision: Radiometric Modeling and Mathematical Formulations
- **Choice**:
  - **Part A Q1**: $E = I / d^2$ and $\Phi = E \cdot A = (I \cdot A) / d^2$.
  - **Part A Q2**: $E = \frac{P \cdot \rho}{4\pi d^2} \cos\theta$ evaluated across 1D sweeps for $P$, $d$, $\theta$, and $\rho$.
  - **Part A Q3**: Lambertian ($I_d = k_d (\mathbf{N} \cdot \mathbf{L})$) vs. Phong specular ($I_s = k_s (\mathbf{R} \cdot \mathbf{V})^\alpha$).
  - **Part A Q6**: Full sensor pipeline from surface radiance $L_o \to$ optical irradiance $E_i = L_o \frac{\pi}{4} \left(\frac{D}{f}\right)^2 \to$ exposure $H = E_i \cdot \Delta t \to$ quantized digital value $P = \text{clip}(\text{round}(g \cdot H), 0, 255)$.
  - **Part A Q7**: 2D synthetic scene with distinct planar/curved patches rendered under direct overhead vs. oblique low-angle illumination with cross-sectional profiles and histograms.
  - **Part B**: Render/analyze a 3D geometric object under direct lighting vs. soft shadow/diffuse lighting, computing brightness, histograms, mean, standard deviation, and line profile slices.
- **Rationale**: Exact alignment with radiometry theory while keeping code compact and vector-oriented.

## Risks / Trade-offs

- [Risk] Running interactive plots in headless environments.
  → Mitigation: Standard `plt.show()` and `inline` figures will be embedded in notebook cell outputs without requiring interactive display servers.
