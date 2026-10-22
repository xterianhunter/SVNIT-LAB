import numpy as np
import matplotlib.pyplot as plt

def run_illumination_experiments():
    # Source Radiant Intensity (in Watts/sr or Candela)
    I = 100.0  

    # 1. Define experimental ranges
    distances = np.linspace(1.0, 10.0, 100)        # Distance d from 1m to 10m
    areas = np.array([0.5, 1.0, 2.0, 4.0, 8.0])     # Sample areas in m^2

    # Discrete test points for tabular observations
    sample_distances = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
    sample_areas = np.array([0.5, 1.0, 2.0, 4.0])

    print("=" * 65)
    print("EXPERIMENTAL OBSERVATIONS: Total Received Flux Phi (Watts/Lumens)")
    print(f"Radiation Source Intensity I = {I} W/sr")
    print("=" * 65)
    header = f"{'Distance (d)':<15}" + "".join([f"Area={a}m²{'':<6}" for a in sample_areas])
    print(header)
    print("-" * 65)

    for d in sample_distances:
        row = f"{d:<15.1f}"
        for a in sample_areas:
            phi = (I * a) / (d ** 2)
            row += f"{phi:<14.2f}"
        print(row)
    print("=" * 65)

    # 2. Multi-panel Visualization
    fig = plt.figure(figsize=(15, 10))
    plt.suptitle("Investigation of Illumination vs. Distance and Surface Area", fontsize=16, fontweight='bold')

    # Subplot 1: Irradiance (E) vs Distance (Inverse Square Law)
    ax1 = fig.add_subplot(2, 2, 1)
    irradiance = I / (distances ** 2)
    ax1.plot(distances, irradiance, 'b-', linewidth=2.5, label=r'$E = \frac{I}{d^2}$')
    ax1.set_title("1. Illuminance / Irradiance vs. Distance", fontsize=12, fontweight='bold')
    ax1.set_xlabel("Distance d (m)", fontsize=10)
    ax1.set_ylabel("Illuminance E (W/m² or Lux)", fontsize=10)
    ax1.grid(True, linestyle='--', alpha=0.6)
    ax1.legend()

    # Subplot 2: Total Received Flux vs. Distance for different Areas
    ax2 = fig.add_subplot(2, 2, 2)
    for a in areas:
        flux = (I * a) / (distances ** 2)
        ax2.plot(distances, flux, linewidth=2, label=f'Area = {a} m²')
    ax2.set_title("2. Received Flux vs. Distance (Various Areas)", fontsize=12, fontweight='bold')
    ax2.set_xlabel("Distance d (m)", fontsize=10)
    ax2.set_ylabel("Total Received Flux Φ (Watts or Lumens)", fontsize=10)
    ax2.grid(True, linestyle='--', alpha=0.6)
    ax2.legend()

    # Subplot 3: Total Received Flux vs. Surface Area for different Distances
    ax3 = fig.add_subplot(2, 2, 3)
    continuous_areas = np.linspace(0.1, 10.0, 100)
    for d in [1.0, 2.0, 3.0, 5.0]:
        flux_area = (I * continuous_areas) / (d ** 2)
        ax3.plot(continuous_areas, flux_area, linewidth=2, label=f'd = {d} m')
    ax3.set_title("3. Received Flux vs. Surface Area (Various Distances)", fontsize=12, fontweight='bold')
    ax3.set_xlabel("Surface Area A (m²)", fontsize=10)
    ax3.set_ylabel("Total Received Flux Φ (Watts or Lumens)", fontsize=10)
    ax3.grid(True, linestyle='--', alpha=0.6)
    ax3.legend()

    # Subplot 4: 3D Surface Plot showing Phi as a function of (Area, Distance)
    ax4 = fig.add_subplot(2, 2, 4, projection='3d')
    A_grid, D_grid = np.meshgrid(np.linspace(0.5, 8.0, 30), np.linspace(1.0, 8.0, 30))
    Phi_grid = (I * A_grid) / (D_grid ** 2)
    
    surf = ax4.plot_surface(D_grid, A_grid, Phi_grid, cmap='viridis', edgecolor='none', alpha=0.85)
    ax4.set_title("4. 3D Surface: Received Flux Φ(d, A)", fontsize=12, fontweight='bold')
    ax4.set_xlabel("Distance d (m)", fontsize=9)
    ax4.set_ylabel("Area A (m²)", fontsize=9)
    ax4.set_zlabel("Flux Φ (W)", fontsize=9)
    fig.colorbar(surf, ax=ax4, shrink=0.5, aspect=10, label='Flux Φ')

    plt.tight_layout()
    output_image = "illumination_experiment_results.png"
    plt.savefig(output_image, dpi=300)
    print(f"\nVisualization saved successfully as '{output_image}'.")
    plt.show()

if __name__ == "__main__":
    run_illumination_experiments()
