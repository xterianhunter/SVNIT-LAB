import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

os.makedirs('figures', exist_ok=True)
plt.rcParams['figure.dpi'] = 300
plt.rcParams['font.size'] = 9

# -------------------------------------------------------------
# Q1: Received Illumination vs. Distance and Area
# -------------------------------------------------------------
I = 100.0
d = np.linspace(1.0, 10.0, 100)
areas = [0.5, 1.0, 2.0, 4.0]

plt.figure(figsize=(10, 3.8))

plt.subplot(1, 2, 1)
plt.plot(d, I / (d**2), 'b-', lw=2)
plt.title("Irradiance vs. Distance (E = I / d²)", fontweight='bold')
plt.xlabel("Distance d (m)")
plt.ylabel("Irradiance E (W/m²)")
plt.grid(True, linestyle="--", alpha=0.6)

plt.subplot(1, 2, 2)
for A in areas:
    plt.plot(d, (I * A) / (d**2), lw=1.8, label=f"Area = {A} m²")
plt.title("Received Flux vs. Distance (Φ = I·A / d²)", fontweight='bold')
plt.xlabel("Distance d (m)")
plt.ylabel("Total Flux Φ (Watts)")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.6)

plt.tight_layout()
plt.savefig('figures/q1_illumination.png', bbox_inches='tight')
plt.close()
print("Saved figures/q1_illumination.png")

# -------------------------------------------------------------
# Q2: Sensitivity Analysis (One Parameter at a Time)
# -------------------------------------------------------------
def calc_intensity(P, d, theta, rho):
    return (P * rho * np.maximum(0.0, np.cos(theta))) / (4.0 * np.pi * (d**2))

P_vals = np.linspace(10, 200, 50)
d_vals = np.linspace(1, 10, 50)
theta_vals = np.linspace(0, np.pi/2, 50)
rho_vals = np.linspace(0.1, 1.0, 50)

plt.figure(figsize=(9, 6.5))

plt.subplot(2, 2, 1)
plt.plot(P_vals, calc_intensity(P_vals, 2.0, 0, 0.8), 'r-', lw=2)
plt.title("1. Effect of Power P (d=2m, θ=0°, ρ=0.8)", fontweight='bold')
plt.xlabel("Power P (W)"); plt.ylabel("Intensity (W/m²)"); plt.grid(True, linestyle="--", alpha=0.6)

plt.subplot(2, 2, 2)
plt.plot(d_vals, calc_intensity(100, d_vals, 0, 0.8), 'g-', lw=2)
plt.title("2. Effect of Distance d (P=100W, θ=0°, ρ=0.8)", fontweight='bold')
plt.xlabel("Distance d (m)"); plt.ylabel("Intensity (W/m²)"); plt.grid(True, linestyle="--", alpha=0.6)

plt.subplot(2, 2, 3)
plt.plot(np.degrees(theta_vals), calc_intensity(100, 2.0, theta_vals, 0.8), 'b-', lw=2)
plt.title("3. Effect of Angle θ (Lambert's Law)", fontweight='bold')
plt.xlabel("Angle θ (degrees)"); plt.ylabel("Intensity (W/m²)"); plt.grid(True, linestyle="--", alpha=0.6)

plt.subplot(2, 2, 4)
plt.plot(rho_vals, calc_intensity(100, 2.0, 0, rho_vals), 'm-', lw=2)
plt.title("4. Effect of Reflectance ρ (P=100W, d=2m, θ=0°)", fontweight='bold')
plt.xlabel("Reflectance ρ"); plt.ylabel("Intensity (W/m²)"); plt.grid(True, linestyle="--", alpha=0.6)

plt.tight_layout()
plt.savefig('figures/q2_sensitivity.png', bbox_inches='tight')
plt.close()
print("Saved figures/q2_sensitivity.png")

# -------------------------------------------------------------
# Q3: Diffuse vs Specular Reflection
# -------------------------------------------------------------
view_angles = np.linspace(-np.pi/2, np.pi/2, 200)
theta_L = np.radians(35)
kd = 0.8
I_diffuse = np.full_like(view_angles, kd * max(0.0, np.cos(theta_L)))

ks, alpha = 0.85, 20
cos_RV = np.maximum(0.0, np.cos(view_angles - theta_L))
I_specular = (0.15 * max(0.0, np.cos(theta_L))) + ks * (cos_RV ** alpha)

plt.figure(figsize=(10, 3.8))

plt.subplot(1, 2, 1)
plt.plot(np.degrees(view_angles), I_diffuse, 'b-', lw=2, label="Surface 1: Lambertian Diffuse")
plt.plot(np.degrees(view_angles), I_specular, 'r--', lw=2, label="Surface 2: Specular (Phong, α=20)")
plt.axvline(np.degrees(theta_L), color="gray", linestyle=":", label="Specular Angle (35°)")
plt.title("Intensity vs. View Angle (θ_L = 35°)", fontweight='bold')
plt.xlabel("Viewing Angle (degrees)"); plt.ylabel("Reflected Intensity")
plt.legend(); plt.grid(True, linestyle="--", alpha=0.6)

light_angles = np.linspace(0, np.pi/2, 100)
I_diff_vs_L = kd * np.cos(light_angles)
I_spec_vs_L = (0.15 * np.cos(light_angles)) + ks * (np.maximum(0.0, np.cos(light_angles)) ** alpha)

plt.subplot(1, 2, 2)
plt.plot(np.degrees(light_angles), I_diff_vs_L, 'b-', lw=2, label="Diffuse")
plt.plot(np.degrees(light_angles), I_spec_vs_L, 'r--', lw=2, label="Specular")
plt.title("Intensity vs. Illumination Angle (View = 0°)", fontweight='bold')
plt.xlabel("Illumination Angle θ_L (degrees)"); plt.ylabel("Reflected Intensity")
plt.legend(); plt.grid(True, linestyle="--", alpha=0.6)

plt.tight_layout()
plt.savefig('figures/q3_reflection.png', bbox_inches='tight')
plt.close()
print("Saved figures/q3_reflection.png")

# -------------------------------------------------------------
# Q6: Image Formation Pipeline
# -------------------------------------------------------------
def simulate_image_formation(E0, rho, is_glossy=False, f_num=2.8, t_exp=0.012, sensor_gain=4500):
    Lo = (rho / np.pi) * E0 * (1.4 if is_glossy else 1.0)
    Ei = Lo * (np.pi / 4.0) * (1.0 / (f_num ** 2))
    raw_val = sensor_gain * Ei * t_exp
    return np.clip(np.round(raw_val), 0, 255).astype(int)

illum_range = np.linspace(20, 600, 100)
pixels_matte = [simulate_image_formation(e, rho=0.25, is_glossy=False) for e in illum_range]
pixels_glossy = [simulate_image_formation(e, rho=0.85, is_glossy=True) for e in illum_range]

plt.figure(figsize=(7.5, 3.8))
plt.plot(illum_range, pixels_matte, 'b-', lw=2, label="Surface A: Matte Diffuse (ρ = 0.25)")
plt.plot(illum_range, pixels_glossy, 'r-', lw=2, label="Surface B: Reflective Glossy (ρ = 0.85)")
plt.axhline(255, color="gray", linestyle="--", label="Sensor Saturation Limit (255)")
plt.title("Digital Pixel Intensity vs. Scene Illumination", fontweight='bold')
plt.xlabel("Incident Illumination E₀ (W/m²)")
plt.ylabel("Recorded Pixel Intensity (0-255 DN)")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.savefig('figures/q6_pipeline.png', bbox_inches='tight')
plt.close()
print("Saved figures/q6_pipeline.png")

# -------------------------------------------------------------
# Q7: Synthetic Scene Under Different Illumination Conditions
# -------------------------------------------------------------
y, x = np.mgrid[-1:1:160j, -1:1:160j]
r2 = x**2 + y**2
sphere_mask = r2 <= 0.64

Nx = np.zeros_like(x)
Ny = np.zeros_like(y)
Nz = np.ones_like(x)
Nx[sphere_mask] = x[sphere_mask] / 0.8
Ny[sphere_mask] = y[sphere_mask] / 0.8
Nz[sphere_mask] = np.sqrt(0.64 - r2[sphere_mask]) / 0.8

L1 = np.array([0.0, 0.0, 1.0])
scene_direct = np.clip(Nx * L1[0] + Ny * L1[1] + Nz * L1[2], 0.08, 1.0)
scene_direct[~sphere_mask] = 0.35

L2 = np.array([-0.75, -0.2, 0.63]); L2 /= np.linalg.norm(L2)
scene_oblique = np.clip(Nx * L2[0] + Ny * L2[1] + Nz * L2[2], 0.03, 1.0)
scene_oblique[~sphere_mask] = 0.18
cast_shadow = (~sphere_mask) & (x > 0.35) & (np.abs(y) < 0.65)
scene_oblique[cast_shadow] = 0.03

img_direct_8u = np.clip(scene_direct * 255, 0, 255).astype(np.uint8)
img_oblique_8u = np.clip(scene_oblique * 255, 0, 255).astype(np.uint8)

fig, axes = plt.subplots(2, 3, figsize=(11, 6))

axes[0, 0].imshow(img_direct_8u, cmap="gray", vmin=0, vmax=255)
axes[0, 0].axhline(80, color="cyan", linestyle="--", lw=1.2, label="Row 80")
axes[0, 0].set_title("Direct Overhead Lighting", fontweight='bold')
axes[0, 0].legend(loc="upper right", fontsize=8)

axes[0, 1].imshow(img_oblique_8u, cmap="gray", vmin=0, vmax=255)
axes[0, 1].axhline(80, color="cyan", linestyle="--", lw=1.2, label="Row 80")
axes[0, 1].set_title("Oblique Low-Angle Lighting", fontweight='bold')
axes[0, 1].legend(loc="upper right", fontsize=8)

diff_img = np.abs(img_direct_8u.astype(float) - img_oblique_8u.astype(float))
im_diff = axes[0, 2].imshow(diff_img, cmap="magma")
axes[0, 2].set_title("Absolute Difference Map", fontweight='bold')
plt.colorbar(im_diff, ax=axes[0, 2], fraction=0.046)

axes[1, 0].plot(img_direct_8u[80, :], "b-", lw=1.8, label="Direct")
axes[1, 0].plot(img_oblique_8u[80, :], "r--", lw=1.8, label="Oblique")
axes[1, 0].set_title("Horizontal Profile (Row 80)", fontweight='bold')
axes[1, 0].set_xlabel("Pixel Column"); axes[1, 0].set_ylabel("Intensity (0-255)")
axes[1, 0].legend(fontsize=8); axes[1, 0].grid(True, linestyle="--", alpha=0.6)

axes[1, 1].hist(img_direct_8u.ravel(), bins=32, range=(0, 255), color="blue", alpha=0.6, label="Direct")
axes[1, 1].hist(img_oblique_8u.ravel(), bins=32, range=(0, 255), color="red", alpha=0.6, label="Oblique")
axes[1, 1].set_title("Pixel Intensity Histograms", fontweight='bold')
axes[1, 1].set_xlabel("Intensity"); axes[1, 1].set_ylabel("Frequency")
axes[1, 1].legend(fontsize=8); axes[1, 1].grid(True, linestyle="--", alpha=0.6)

axes[1, 2].axis("off")

plt.tight_layout()
plt.savefig('figures/q7_synthetic_scene.png', bbox_inches='tight')
plt.close()
print("Saved figures/q7_synthetic_scene.png")

# -------------------------------------------------------------
# Part B: Experimental Investigation (Direct vs Shadow)
# -------------------------------------------------------------
np.random.seed(42)
direct_img = np.clip(img_direct_8u.astype(float) + np.random.normal(0, 1.5, img_direct_8u.shape), 0, 255)
shadow_img = np.clip(img_oblique_8u.astype(float) * 0.35 + np.random.normal(0, 1.5, img_oblique_8u.shape), 0, 255)

m_dir, s_dir = np.mean(direct_img), np.std(direct_img)
m_shd, s_shd = np.mean(shadow_img), np.std(shadow_img)

fig, axes = plt.subplots(2, 2, figsize=(9.5, 7.5))

axes[0, 0].imshow(direct_img, cmap="gray", vmin=0, vmax=255)
axes[0, 0].axhline(80, color="yellow", linestyle="--", lw=1.2, label="Row 80")
axes[0, 0].set_title(f"(e) Direct Illumination (Mean={m_dir:.1f}, Std={s_dir:.1f})", fontweight='bold')
axes[0, 0].legend(loc="upper right", fontsize=8)

axes[0, 1].imshow(shadow_img, cmap="gray", vmin=0, vmax=255)
axes[0, 1].axhline(80, color="yellow", linestyle="--", lw=1.2, label="Row 80")
axes[0, 1].set_title(f"(e) Shadowed Condition (Mean={m_shd:.1f}, Std={s_shd:.1f})", fontweight='bold')
axes[0, 1].legend(loc="upper right", fontsize=8)

axes[1, 0].hist(direct_img.ravel(), bins=40, range=(0, 255), color="gold", alpha=0.7, edgecolor="black", label="Direct")
axes[1, 0].hist(shadow_img.ravel(), bins=40, range=(0, 255), color="navy", alpha=0.7, edgecolor="black", label="Shadow")
axes[1, 0].set_title("(b) Intensity Distribution (Histograms)", fontweight='bold')
axes[1, 0].set_xlabel("Pixel Value (0-255)"); axes[1, 0].set_ylabel("Count")
axes[1, 0].legend(fontsize=8); axes[1, 0].grid(True, linestyle="--", alpha=0.6)

axes[1, 1].plot(direct_img[80, :], color="darkorange", lw=1.8, label="Direct Illumination")
axes[1, 1].plot(shadow_img[80, :], color="darkblue", lw=1.8, label="Shadowed Condition")
axes[1, 1].set_title("(d) Intensity Variation Profile (Row 80)", fontweight='bold')
axes[1, 1].set_xlabel("Pixel Index"); axes[1, 1].set_ylabel("Intensity")
axes[1, 1].legend(fontsize=8); axes[1, 1].grid(True, linestyle="--", alpha=0.6)

plt.tight_layout()
plt.savefig('figures/part_b_investigation.png', bbox_inches='tight')
plt.close()
print("Saved figures/part_b_investigation.png")
