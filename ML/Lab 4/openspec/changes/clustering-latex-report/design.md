# Design Document: clustering-latex-report

## Context

See `proposal.md` for background and motivation. The Iris unsupervised clustering experiments have been executed in `clustering_lab4.ipynb`. The notebook contains:
1. Dataset loading, summary statistics, and pairwise feature distributions.
2. Hyperparameter sweeps across $k \in \{1, \dots, 10\}$ generating Inertia (Elbow) and Silhouette curves.
3. K-Means model training with $k=3$, cluster centroids, and contingency alignment with true Iris species.
4. Hierarchical Agglomerative clustering with multiple linkage strategies (Ward, Complete, Average) and truncated dendrogram visualizations.
5. Quantitative benchmark comparison (Inertia, Silhouette Score, Davies-Bouldin Index).

The LaTeX report must follow the specific SVNIT styling requested by the user, incorporating `fancyhdr`, custom `code` and `output` listing environments, Times-style font (`newtxtext`), and figure environments.

## Goals / Non-Goals

**Goals:**
- Implement a script to export all EDA and clustering visualization figures to `figures/*.png` at high resolution (300 DPI).
- Create a complete, self-contained `main.tex` file structured logically into numbered sections covering theory, EDA, model training, hierarchical clustering, quantitative comparisons, and insights.
- Embed exact code listings (`lstlisting[style=code]`) and verbatim outputs (`lstlisting[style=output]`).
- Format theoretical mathematical foundations using standard LaTeX math environments ($W(C)$, Euclidean distance, Ward's minimum variance criterion, Silhouette width $s(i)$, Davies-Bouldin index $R_{ij}$).

**Non-Goals:**
- Modifying the underlying model training or evaluation logic in `clustering_lab4.ipynb`.
- Introducing third-party LaTeX styles or deviating from the user-specified preamble and geometry.

## Decisions

### Decision 1: Figure Generation and Export Strategy
- **Choice**: Use a targeted Python script that loads the Iris dataset, runs the notebook's plotting pipelines, and saves each plot directly to `figures/<name>.png`.
- **Rationale**: Ensures deterministic, vector/high-DPI PNGs are present on disk for LaTeX `\includegraphics` commands without relying on manual notebook exports.
- **Figures to Export**:
  1. `eda_correlation_heatmap.png`: Correlation matrix of Iris morphological features.
  2. `eda_feature_pairplot.png`: Pairwise feature relationships and ground-truth class separation.
  3. `kmeans_elbow_curve.png`: WCSS / Inertia vs. Number of Clusters $k$.
  4. `kmeans_silhouette_curve.png`: Mean Silhouette Score vs. $k$.
  5. `kmeans_pca_clusters.png`: 2D PCA projection of K-Means ($k=3$) clusters with centroids.
  6. `hierarchical_dendrograms.png`: Comparative dendrograms for Ward, Complete, and Average linkages.
  7. `hierarchical_clusters_pca.png`: 2D PCA cluster visualization of Agglomerative Clustering ($k=3$).

### Decision 2: Document Structure and Section Flow
- **Choice**: Structure `main.tex` into the following cohesive sections:
  1. **Document Header**: SVNIT Department of CSE, M.Tech. I Semester I, CSDS105, Assignment 4, Student details.
  2. **Section 1: Introduction and Theoretical Background**: Formulations of K-Means, distance metrics, linkage criteria (Ward, Single, Complete, Average), and evaluation metrics (Silhouette, Davies-Bouldin).
  3. **Section 2: Environment Setup and Dataset Exploration**: Libraries, Iris dataset characteristics, feature statistics, pairplots, and correlation analysis.
  4. **Section 3: K-Means Clustering -- Hyperparameter Tuning and Model Training**: Elbow method, Silhouette score optimization, final $k=3$ model training, centroids, and PCA cluster visualization.
  5. **Section 4: Hierarchical Clustering -- Dendrograms and Agglomerative Models**: Agglomerative hierarchy, dendrogram analysis across linkages, threshold cuts, and cluster assignments.
  6. **Section 5: Quantitative Comparison and Cluster Validation**: Summary metrics table (Silhouette, Davies-Bouldin), contingency matrix comparison against ground-truth labels, and failure/overlap analysis.
  7. **Section 6: Discussion and Conclusion**: Interpretations of geometry vs. density, linkage tradeoffs, and key findings.

## Risks / Trade-offs

- **[Risk]**: Local machine may not have a complete TeX Live distribution (`pdflatex`) installed.
  - **Mitigation**: Author `main.tex` to be fully standards-compliant and syntax-verified so that it compiles without error in any standard TeX distribution (TeX Live, MacTeX, MiKTeX, or Overleaf).
- **[Risk]**: Code and output listings might exceed page margins or wrap awkwardly.
  - **Mitigation**: Utilize `listings` settings `breaklines=true`, `breakatwhitespace=false`, and `columns=fullflexible` as specified in the template, while wrapping long text lines in the `.tex` source.
