## Context

See `proposal.md` for background and motivation. The existing Lab 4 workspace contains `clustering_lab4.ipynb` (which explored K-Means and Hierarchical clustering on the standard Iris dataset) and `clustering_lab4_train_dev_test.ipynb` (which implemented a complex 3-way split with validation tuning). The user specifically requested a new, clean Jupyter notebook that focuses on Fuzzy C-Means (FCM) and DBSCAN, keeping things simple without development set partitioning.

## Goals / Non-Goals

**Goals:**
- Provide a clean, standalone, fully executable Jupyter notebook `clustering_lab4_fcm_dbscan.ipynb`.
- Implement a vectorized, self-contained `FuzzyCMeans` class in NumPy/SciPy adhering to standard Bezdek objective minimization.
- Implement DBSCAN using `sklearn.cluster.DBSCAN` with systematic k-distance knee analysis for determining $\epsilon$.
- Provide Hungarian algorithm mapping for optimal cluster-to-class alignment (with explicit handling of DBSCAN noise points).
- Compute and contrast unsupervised metrics (Silhouette, Davies-Bouldin, Calinski-Harabasz) and error metrics (MAE, MSE, RMSE, ARI, NMI, confusion matrices).
- Produce informative, aesthetic visualizations (EDA, hyperparameter diagnostics, 2D feature and PCA scatter plots, membership distributions, confusion matrices).

**Non-Goals:**
- No train/dev/test splits or cross-validation pipelines (explicitly requested to keep things simple).
- No external package installation requirements (such as `skfuzzy`), keeping execution frictionless within the existing environment.
- No modifications to existing notebooks or report files.

## Decisions

### 1. Vectorized Pure-NumPy Fuzzy C-Means Class vs. External `skfuzzy`
- **Choice**: Implement a standalone `FuzzyCMeans` class with methods `fit(X)`, `predict(X)`, `predict_proba(X)` using pure NumPy and SciPy.
- **Rationale**: The user environment does not have `skfuzzy` pre-installed, whereas `numpy` and `scipy` are readily available. A pure NumPy implementation gives full mathematical transparency (Bezdek objective $J_m$, distance calculations, membership updates, convergence threshold $\epsilon=10^{-5}$) and avoids dependency issues.
- **Alternatives Considered**: Using `pip install scikit-fuzzy` was rejected to avoid altering the user's environment dependencies when pure NumPy is straightforward and fast on small/medium tabular datasets.

### 2. DBSCAN Parameter Selection via k-Distance (Elbow) Graph
- **Choice**: Use `sklearn.neighbors.NearestNeighbors` to calculate the distance to the $k$-th nearest neighbor ($k = \text{min\_samples}$, evaluating $k=4$ or $k=5$) sorted in ascending order.
- **Rationale**: Identifies the threshold where density drops sharply (the "elbow" or "knee"), providing an empirical, principled foundation for selecting $\epsilon \approx 0.5-0.6$.
- **Alternatives Considered**: Arbitrary grid search without visualization was rejected because density-based clustering requires understanding neighborhood scale.

### 3. Handling DBSCAN Noise Points (-1) in Metrics & Label Alignment
- **Choice**: For the Hungarian algorithm, match non-noise points to true class labels to establish cluster mapping; map noise points to an explicit designated label or assign them as errors in MAE/MSE/RMSE. Compute Silhouette score for valid clusters ($k \ge 2$, filtering out noise or passing sample labels to `silhouette_score`).
- **Rationale**: DBSCAN inherently identifies outliers as noise (label -1). Properly accounting for noise prevents runtime errors and avoids misleading evaluation scores.

### 4. Structure of the Notebook
- **Choice**: Organize into clean, numbered sections mirroring the original Lab 4 structure:
  1. Imports & Environment Setup
  2. Dataset Loading & Minimal Preprocessing (StandardScaler)
  3. Exploratory Data Analysis (Feature distributions & correlations)
  4. Hyperparameter Analysis (FCM objective & fuzziness sweeps; DBSCAN k-distance plot & grid sweep)
  5. Model Training (Fitting FCM with $c=3, m=2.0$ and calibrated DBSCAN)
  6. Hungarian Cluster Alignment with Ground Truth
  7. Visualizations (2D feature space with centroids/core points, 2D PCA projections, FCM soft membership distributions)
  8. Unsupervised & Supervised Metrics Evaluation (Structured comparison table & bar charts)
  9. Confusion Matrices & Key Observations

## Risks / Trade-offs

- **[Risk]** DBSCAN on the Iris dataset typically merges Iris-versicolor and Iris-virginica because their density regions overlap closely in continuous feature space, yielding 2 dense clusters plus noise.
  - **Mitigation**: Highlight this fundamental behavioral distinction in markdown notes; explain that DBSCAN identifies arbitrary density shapes and separates the well-isolated Iris-setosa cluster cleanly, while density-overlap makes virginica/versicolor a single contiguous density region.
- **[Risk]** Division by zero in FCM membership computation if a sample coincides exactly with a cluster centroid.
  - **Mitigation**: Add a small numerical stabilization constant ($\epsilon = 10^{-10}$) or explicit check in the distance-to-membership calculation.
- **[Risk]** Silhouette score requires at least 2 distinct clusters and at most $n-1$ clusters. If DBSCAN parameters yield 1 cluster or only noise, `silhouette_score` raises a ValueError.
  - **Mitigation**: Guard metric computations with a check on the number of unique clusters found ($\text{len}(\text{set}(\text{labels})) - (1 \text{ if } -1 \in \text{labels} \text{ else } 0) \ge 2$).
