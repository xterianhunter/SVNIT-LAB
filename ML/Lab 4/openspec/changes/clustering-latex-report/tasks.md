## 1. Asset Preparation & Figure Extraction

- [x] 1.1 Create a Python figure export script to execute visualization pipelines from `clustering_lab4.ipynb` and save 300 DPI figures to `figures/`
- [x] 1.2 Verify that all required plot assets (`eda_correlation_heatmap.png`, `eda_feature_pairplot.png`, `kmeans_elbow_curve.png`, `kmeans_silhouette_curve.png`, `kmeans_pca_clusters.png`, `hierarchical_dendrograms.png`, `hierarchical_clusters_pca.png`) exist in `figures/`

## 2. LaTeX Document Preamble & Theoretical Formulation

- [x] 2.1 Initialize `main.tex` with the specified SVNIT header, geometry, Times-style font (`newtxtext`), `fancyhdr` metadata, and listing styles (`code`, `output`)
- [x] 2.2 Author Section 1 (Introduction and Theoretical Formulation) containing mathematical definitions of K-Means WCSS, distance metrics, linkage formulations (Ward, Complete, Average), and evaluation metrics (Silhouette width, Davies-Bouldin index)

## 3. Experimental Sections, Code Listings & Figures

- [x] 3.1 Author Section 2 (Dataset Description and Exploratory Data Analysis) with code listings, summary output listings, and embedded EDA figures
- [x] 3.2 Author Section 3 (K-Means Clustering: Optimization & Model Training) including hyperparameter sweep code, Elbow and Silhouette curves, optimal model fitting, centroid outputs, and 2D PCA cluster figure
- [x] 3.3 Author Section 4 (Hierarchical Agglomerative Clustering) with linkage code listings, comparative dendrogram figure, agglomerative model fitting, and cluster visualization figure

## 4. Comparative Benchmarking, Synthesis & Review

- [x] 4.1 Author Section 5 (Quantitative Evaluation and Cluster Validation) featuring a structured LaTeX table comparing Silhouette Scores, Davies-Bouldin Indices, and Ground-Truth Contingency Matrices
- [x] 4.2 Author Section 6 (Discussion and Analytical Insights) highlighting cluster geometry, sensitivity to outliers, linkage tradeoffs, and key findings
- [x] 4.3 Perform end-to-end verification of `main.tex` for syntax completeness, balanced environments, figure references, and template adherence
