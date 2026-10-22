## Purpose

Provides sequential and OpenMP-parallelized multi-variable linear regression implementations with a 3-dimensional data space (2D features, 1D target) to evaluate gradient descent performance on large sample sizes.

## ADDED Requirements

### Requirement: 3D Data Space Representation
The system SHALL represent and process linear regression datasets with two input features ($X_1, X_2$) and one continuous label ($Y$), forming an overall 3-dimensional dataspace with hypothesis $\hat{y} = w_0 + w_1 x_1 + w_2 x_2$.

#### Scenario: Synthetic 3D dataset generation
- **WHEN** synthetic training data is generated for $N$ samples
- **THEN** each sample $i$ contains feature values $(x_{i,1}, x_{i,2})$ and target value $y_i$ generated with known model parameters and noise.

### Requirement: OpenMP Parallelized Gradient Descent
The system SHALL parallelize the batch gradient descent computation across $N$ data points using OpenMP reduction clauses to compute partial derivatives for weights $w_0, w_1, w_2$ and mean squared error loss per epoch.

#### Scenario: Parallel gradient convergence and accuracy
- **WHEN** parallel gradient descent executes with multiple OpenMP threads
- **THEN** the converged weights and final loss match the sequential baseline within numerical precision tolerances.

### Requirement: Sequential vs Parallel Performance Comparison
The system SHALL benchmark execution time for both sequential and multi-threaded OpenMP gradient descent runs on a large number of data points ($N \ge 1{,}000{,}000$) and output execution times, speedup factors, and thread scaling statistics.

#### Scenario: Performance benchmarking output
- **WHEN** the benchmarking binary is executed
- **THEN** it outputs per-run execution time (seconds), speedup relative to sequential execution, and final converged parameters across tested thread configurations.

### Requirement: Self-Contained Minimal Lab2 Structure
All source code, build scripts, and execution artifacts for the linear regression experiment SHALL be placed inside the `Lab2/` folder, maintaining a simple and concise codebase without unnecessary files.

#### Scenario: Build and execute from Lab2
- **WHEN** the build command is invoked within the `Lab2/` directory
- **THEN** the executable builds cleanly with `-fopenmp` and runs the benchmark end-to-end.
