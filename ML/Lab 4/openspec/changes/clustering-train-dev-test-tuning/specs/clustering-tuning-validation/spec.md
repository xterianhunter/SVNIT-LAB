## Purpose

Defines requirements for Train-Development-Test partitioning and multi-stage hyperparameter tuning comparison in unsupervised clustering workflows.

## ADDED Requirements

### Requirement: Stratified 3-Way Partitioning and Preprocessing Isolation
The system SHALL split the Iris dataset into three disjoint partitions: Training set (60%), Development/Validation set (20%), and Test set (20%), utilizing stratified sampling across species classes, and SHALL fit the `StandardScaler` strictly on the Training set to prevent data leakage.

#### Scenario: Split proportions and scaler fitting
- **WHEN** the dataset splitting and scaling pipeline executes
- **THEN** exactly 90 instances are allocated to Train (30 per species), 30 to Development (10 per species), and 30 to Test (10 per species), with the scaler fitted only on the 90 training instances.

### Requirement: Training Set Hyperparameter Sweeps
The system SHALL perform a comprehensive hyperparameter sweep for K-Means clustering over $k \in \{1, 2, \dots, 10\}$ on the standardized Training partition, calculating and logging Within-Cluster Sum of Squares (Inertia) and Silhouette Scores.

#### Scenario: Train sweep execution
- **WHEN** the training set hyperparameter sweep is conducted
- **THEN** an array of 10 Inertia values and 9 Silhouette scores ($k \ge 2$) is computed strictly using training data points.

### Requirement: Development Set Validation and Comparative Difference Analysis
The system SHALL execute hyperparameter evaluation across candidate $k \in \{1, \dots, 10\}$ on the Development partition, plot Train vs. Development curves side-by-side, and output an explicit comparative difference analysis.

#### Scenario: Train vs Dev comparison curves
- **WHEN** generating hyperparameter tuning diagnostics
- **THEN** the system displays side-by-side plots of Train vs. Dev Inertia curves and Train vs. Dev Silhouette score profiles, identifying any divergence, scale differences, or shift in the optimal $k$ inflection point.

### Requirement: Model Finalization and Test Set Generalization Evaluation
The system SHALL fit the chosen optimal K-Means model ($k=3$) and Hierarchical Agglomerative model on the Training set, confirm suitability on the Development set, and evaluate final generalization performance on the unseen Test set.

#### Scenario: Test set evaluation metrics
- **WHEN** evaluating the finalized models on the Test partition
- **THEN** the system calculates Silhouette Score, Davies-Bouldin Index, Calinski-Harabasz Index, MAE, MSE, RMSE, and aligned confusion matrices for both K-Means and Hierarchical Clustering.

### Requirement: Standalone Executed Jupyter Notebook
The system SHALL provide the complete implementation, markdown commentary, mathematical explanations, and executed outputs in a dedicated notebook named `clustering_lab4_train_dev_test.ipynb`.

#### Scenario: Notebook structure and execution
- **WHEN** `clustering_lab4_train_dev_test.ipynb` is inspected
- **THEN** all code cells have sequential execution counts, rendered matplotlib/seaborn plots, and tabular text outputs reflecting the 3-way partition analysis.
