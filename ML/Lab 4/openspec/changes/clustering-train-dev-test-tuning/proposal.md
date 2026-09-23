# Change Proposal: clustering-train-dev-test-tuning

## Why

In unsupervised clustering workflows, algorithms and hyperparameter choices are frequently evaluated on the complete dataset without verifying cluster stability or generalization across disjoint subsets. Introducing an explicit Train / Development (Validation) / Test protocol allows rigorous hyperparameter tuning ($k \in 1 \dots 10$) first on the training partition and subsequently on the development partition. This empirically demonstrates whether hyperparameter selection (Elbow inflection, Silhouette score peaks) remains consistent or exhibits variance across independent splits, while providing an unbiased final assessment on the holdout test set.

## What Changes

- Create a new notebook `clustering_lab4_train_dev_test.ipynb` replicating the comprehensive workflow of `clustering_lab4.ipynb` (EDA, visualizations, K-Means, Hierarchical clustering, PCA projections, error metrics, and confusion matrices).
- Introduce a 3-way data partition (e.g., 60% Train, 20% Development, 20% Test) with stratified sampling and proper preprocessing isolation (StandardScaler fitted strictly on Train).
- Execute hyperparameter sweeps for K-Means ($k=1 \dots 10$) first independently on the **Training set**, recording Inertia and Silhouette scores.
- Execute the identical hyperparameter sweep on the **Development set** (evaluating both native clustering on Dev and transfer evaluation of Train centroids on Dev).
- Plot side-by-side comparison curves (Train vs. Development Inertia and Silhouette scores) and present a structured comparative analysis highlighting differences, inflection shifts, or stability.
- Train the optimal model ($k=3$) on the Training set, confirm behavior on the Development set, and perform final evaluation on the unseen **Test set** with complete performance metrics and confusion matrices.

## Capabilities

### New Capabilities
- `clustering-tuning-validation`: Implementation of a 3-way (Train/Dev/Test) unsupervised clustering pipeline in `clustering_lab4_train_dev_test.ipynb`, contrasting hyperparameter tuning sweeps between Train and Development sets and evaluating final model generalization on Test.

### Modified Capabilities
*(None)*

## Impact

- **New Files**:
  - `clustering_lab4_train_dev_test.ipynb`: Dedicated notebook with full execution, comparative plots, and output logs.
- **Dependencies**: Uses existing Python environment (`numpy`, `pandas`, `scikit-learn`, `matplotlib`, `seaborn`, `scipy`).
- **Backward Compatibility**: Leaves original `clustering_lab4.ipynb` and `main.tex` completely intact.
