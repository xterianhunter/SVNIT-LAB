## Purpose

Provides high-performance sequential and OpenMP parallel implementations of linear regression gradient descent on a 3-dimensional dataspace (2D features, 1D label) with runtime benchmarking.

## ADDED Requirements

### Requirement: 3D Dataspace Generation
The system SHALL generate or ingest a dataset containing 2 feature dimensions ($x_1, x_2$) and 1 target dimension ($y$) with a configurable number of samples ($N \ge 1,000,000$).

#### Scenario: Generate synthetic 3D dataset
- **WHEN** the program initializes with $N$ samples
- **THEN** arrays for features $x_1$, $x_2$ and target $y$ are allocated and populated with synthetic values following a linear relationship with noise.

### Requirement: Sequential Gradient Descent
The system SHALL compute gradient descent updates sequentially across all training samples over a specified number of epochs.

#### Scenario: Run sequential gradient descent
- **WHEN** sequential gradient descent is executed
- **THEN** model weights ($w_1, w_2$) and bias ($b$) are updated iteratively and execution time is recorded.

### Requirement: OpenMP Parallel Gradient Descent
The system SHALL compute gradient descent updates in parallel using OpenMP multi-threading across training samples with reduction for partial gradients.

#### Scenario: Run OpenMP parallel gradient descent
- **WHEN** parallel gradient descent is executed with multiple threads
- **THEN** sample evaluations and gradient accumulations are distributed across threads, producing equivalent model weights and recorded execution time.

### Requirement: Performance Comparison
The system SHALL benchmark and output the elapsed execution time and speedup of OpenMP parallel gradient descent compared to the sequential version.

#### Scenario: Output benchmarking metrics
- **WHEN** both sequential and parallel training runs complete
- **THEN** the console outputs sequential time, parallel time, speedup factor, and final model parameters.
