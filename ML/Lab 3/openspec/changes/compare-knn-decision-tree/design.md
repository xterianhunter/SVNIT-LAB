## Context

The lab environment requires an educational, executable Jupyter Notebook demonstrating and contrasting K-Nearest Neighbors (KNN) and Decision Tree classification algorithms. Existing notebooks in the workspace are either incomplete Kaggle-based exports or cluttered with extraneous exploratory steps. This design establishes a focused architecture for the notebook structure, dataset selection, mathematical formulations, and evaluation plotting.

## Goals / Non-Goals

**Goals:**
- Provide a clean, standalone, executable `.ipynb` notebook without external CSV dependencies.
- Select an optimal dataset from `sklearn.datasets` that illustrates both algorithms effectively.
- Apply minimal, purposeful preprocessing (stratified splitting, standard scaling).
- Present explicit LaTeX mathematical formulations for tree node splitting (Entropy, Information Gain, Gini Impurity) and KNN distance metrics (Euclidean, Manhattan, Minkowski).
- Generate visualizations: graphical decision tree plot, confusion matrix heatmaps, error vs. `max_depth` plot for Decision Tree, and error rate vs. $K$ plot for KNN.
- Produce a comparative performance summary table.

**Non-Goals:**
- Exhaustive exploratory data analysis (EDA), pairplots of 30+ features, or outlier clipping.
- Hyperparameter search over unrelated algorithms (e.g., Random Forests, SVMs).
- Web application or model deployment scripts.

## Decisions

### 1. Dataset Selection: Breast Cancer Wisconsin Diagnostic
- **Decision**: Use `sklearn.datasets.load_breast_cancer()`.
- **Rationale**: It contains 569 samples with 30 continuous numerical features and well-defined binary diagnostic classes (Malignant vs. Benign). It serves as the gold-standard benchmark for both tree-based thresholding and multi-dimensional metric-based neighborhood distance calculations.
- **Alternatives Considered**:
  - *Iris Dataset*: 4 features and 3 classes; too trivial and over-used, makes tree depth error curves less expressive.
  - *Wine Dataset*: 13 features and 3 classes; viable, but binary cancer classification offers clearer medical-grade precision/recall trade-off interpretations.

### 2. Minimal Preprocessing Architecture
- **Decision**:
  - Split: 75% train / 25% test stratified split (`random_state=42`).
  - Scaling: Fit `StandardScaler` on training features and transform test features for KNN; keep unscaled features available to demonstrate tree invariance to monotonic feature transformations.
- **Rationale**: KNN computes distances across dimensions; without scaling, features with large variances dominate the distance metric. Decision Trees split one feature at a time and are scale-invariant.

### 3. Mathematical Exposition Style
- **Decision**: Dedicate distinct markdown cells before each model block with formatted LaTeX equations:
  - *Decision Tree*:
    - Entropy: $H(S) = -\sum_{i=1}^c p_i \log_2 p_i$
    - Information Gain: $IG(S, A) = H(S) - \sum_{v \in \text{Values}(A)} \frac{|S_v|}{|S|} H(S_v)$
    - Gini Impurity: $Gini(S) = 1 - \sum_{i=1}^c p_i^2$
  - *KNN*:
    - Euclidean Distance: $d(p, q) = \sqrt{\sum_{i=1}^n (p_i - q_i)^2}$
    - Manhattan Distance: $d(p, q) = \sum_{i=1}^n |p_i - q_i|$
    - Minkowski Distance: $d(p, q) = \left(\sum_{i=1}^n |p_i - q_i|^p\right)^{1/p}$
    - Majority Voting: $\hat{y} = \arg\max_{c} \sum_{i \in N_K(x)} I(y_i = c)$

### 4. Visualizations and Error Calculations
- **Decision**:
  - Decision Tree: Limit visual tree depth to `max_depth=3` or `4` for legible graph rendering via `sklearn.tree.plot_tree`. Plot test error vs. tree depths $1 \le \text{depth} \le 15$ to demonstrate underfitting vs. overfitting.
  - KNN: Plot misclassification error rate ($1 - \text{accuracy}$) vs. $K$ for $1 \le K \le 30$ with annotated minimum error point.
  - Confusion Matrices: Plot side-by-side or dedicated annotated heatmaps with true vs. predicted counts and normalized percentages.

## Risks / Trade-offs

- **[Risk]** Large tree depth makes `plot_tree` unreadable.
  - **Mitigation**: Train a primary interpretable tree with `max_depth=3` or `4` for the graphical plot, while evaluating full/variable depths in the parametric error curve.
- **[Risk]** Scaling mismatch between models.
  - **Mitigation**: Explicitly maintain `X_train_scaled`/`X_test_scaled` for KNN and `X_train`/`X_test` for the Decision Tree, explaining why scaling is mandatory for KNN but optional for Decision Trees.
