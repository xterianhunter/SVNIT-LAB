## Why

In machine learning coursework and practical experimentation, students and practitioners require clear, concise, and rigorous implementations comparing instance-based models (K-Nearest Neighbors) with rule-based tree models (Decision Tree). This change introduces a self-contained, well-structured Jupyter Notebook that loads an optimal dataset from `sklearn.datasets`, applies minimal necessary preprocessing, and performs full training, mathematical formula exposition, visualization (confusion matrices, tree structure, error curves), and error/metric evaluation for both models.

## What Changes

- Create a focused, end-to-end Jupyter Notebook (`knn_vs_decision_tree_analysis.ipynb`).
- Load a well-suited classification dataset (Breast Cancer Wisconsin or Wine from `sklearn.datasets`) requiring minimal preprocessing without unnecessary EDA clutter.
- Perform necessary preprocessing: train-test split (stratified) and feature scaling (`StandardScaler` required for distance-sensitive KNN, contrasted with unscaled/scaled tree behavior).
- Build, visualize, and evaluate the Decision Tree Classifier:
  - Theoretical exposition with LaTeX formulas for node splitting criteria (Entropy, Information Gain, and Gini Impurity).
  - Visualization of the fitted tree graph (`plot_tree`).
  - Confusion matrix heatmap and classification report (Accuracy, Precision, Recall, F1-score).
  - Error analysis across varying tree depths (misclassification error vs. `max_depth`).
- Build, visualize, and evaluate the K-Nearest Neighbors (KNN) Classifier:
  - Theoretical exposition with LaTeX formulas for distance metrics (Euclidean, Manhattan, Minkowski) and majority voting.
  - Confusion matrix heatmap and classification report.
  - Error rate vs. $K$ parameter curve (misclassification rate vs. neighbor count) to find optimal $K$.
- Comparison synthesis highlighting differences in model performance, sensitivity to scaling, and decision boundaries.

## Capabilities

### New Capabilities
- `classification-lab-notebook`: End-to-end classification lab notebook covering dataset ingestion, minimal preprocessing, Decision Tree & KNN modeling, mathematical formulation, confusion matrix plotting, tree graph visualization, and parametric error curve evaluation.

### Modified Capabilities

## Impact

- Adds `knn_vs_decision_tree_analysis.ipynb` in the lab workspace.
- Requires standard ML libraries: `numpy`, `pandas`, `scikit-learn`, `matplotlib`, and `seaborn`.
