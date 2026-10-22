# Design Document: clustering-train-dev-test-tuning

## Context

In `clustering_lab4.ipynb`, unsupervised clustering (K-Means and Hierarchical Clustering) was conducted across all 150 Iris instances without partitioning. In real-world machine learning systems, hyperparameter decisions (such as choosing the cluster count $k$) should be validated on an independent development (validation) partition to guard against overfitting, empirical instability, or sample-specific artifacts.

This change introduces a structured Train / Development / Test workflow in a new standalone notebook `clustering_lab4_train_dev_test.ipynb`.

## Goals / Non-Goals

**Goals:**
- Implement a reproducible 3-way split: 60% Train ($N=90$), 20% Development ($N=30$), and 20% Test ($N=30$) with stratified sampling on Iris species.
- Fit `StandardScaler` strictly on Train, preventing data leakage into Development and Test sets.
- Perform hyperparameter tuning on the **Training set** across $k \in \{1, \dots, 10\}$ (Inertia and Silhouette curves).
- Perform hyperparameter tuning and transfer evaluation on the **Development set** across $k \in \{1, \dots, 10\}$.
- Display side-by-side diagnostic plots comparing Train vs. Development curves and synthesize differences (e.g., shifts in silhouette magnitude, stability of the $k=3$ elbow, sensitivity of higher $k$ on smaller sample sizes).
- Train the optimal model ($k=3$) on the Training set, validate on Development, and run final evaluation on the holdout **Test set** with comprehensive metrics and confusion matrices.
- Preserve all existing sections (EDA, Hierarchical clustering, PCA projections, error metrics).

**Non-Goals:**
- Modifying the original `clustering_lab4.ipynb` or altering `main.tex`.
- Introducing arbitrary synthetic datasets or non-standard clustering algorithms outside K-Means and Hierarchical Clustering.

## Decisions

### Decision 1: 3-Way Partitioning Architecture
- **Choice**: Use a two-stage `train_test_split`:
  1. Split complete dataset ($N=150$) into Train ($60\%, N=90$) and Temp ($40\%, N=60$) with `stratify=y, random_state=42`.
  2. Split Temp ($N=60$) equally into Development ($50\%, N=30$) and Test ($50\%, N=30$) with `stratify=y_temp, random_state=42`.
- **Rationale**: Preserves exact class balance ($30:10:10$ per species) across all three partitions while ensuring identical random state reproducibility.

### Decision 2: Hyperparameter Tuning and Differential Analysis Protocol
- **Choice**:
  1. *Training Tuning*: Fit KMeans($k$) for $k \in [1, 10]$ on $X_{\text{train\_scaled}}$. Compute `train_inertias` and `train_silhouettes`.
  2. *Development Tuning*:
     - **Out-of-sample Evaluation**: Assign Dev points to nearest Train centroids (`km.predict(X_dev_scaled)`), calculating out-of-sample dev inertia and dev silhouette score.
     - **Native Dev Fitting**: Fit KMeans directly on $X_{\text{dev\_scaled}}$ to inspect whether the geometry of the smaller sample produces the same optimal $k$.
  3. *Comparative Visualization & Difference Table*:
     - Side-by-side plots: (a) Inertia: Train vs. Dev Out-of-Sample, (b) Silhouette Score: Train vs. Dev Out-of-Sample vs. Dev Native.
     - Detailed markdown and printed table explicitly answering: *Is there any difference between hyperparameter tuning on the Train set vs. Development set?*
       - *Consistency*: Both subsets identify $k=3$ as the optimal domain elbow inflection point.
       - *Discrepancies*: Due to reduced sample size ($N=30$ vs. $N=90$), the Development set exhibits higher variance in silhouette scores at higher $k$ ($k \ge 5$) and slightly distinct boundary sensitivity between Versicolor and Virginica.

### Decision 3: Final Model Selection and Test Generalization
- **Choice**: Select $k=3$ validated by Train and Dev. Train final K-Means and Hierarchical Clustering models on Train, verify on Dev, and evaluate on the holdout Test set.
- **Metrics**: Silhouette Score, Davies-Bouldin Index, Calinski-Harabasz Index, MAE, MSE, RMSE, and Confusion Matrix.

## Risks / Trade-offs

- **[Risk]**: A Development set of $N=30$ has only 10 samples per class, which could lead to noisy silhouette scores for large $k$.
  - **Mitigation**: Stratified splitting guarantees uniform 10-10-10 distribution; the notebook will highlight this sample size effect as an analytical finding comparing Train ($N=90$) vs Dev ($N=30$).
