## 1. Notebook Architecture & Data Partitioning

- [x] 1.1 Create `clustering_lab4_train_dev_test.ipynb` notebook structure with library imports, dataset loading, and exploratory data analysis
- [x] 1.2 Implement stratified 3-way dataset splitting (60% Train, 20% Development, 20% Test) and fit `StandardScaler` strictly on the Training set

## 2. Training and Development Hyperparameter Tuning

- [x] 2.1 Implement K-Means hyperparameter sweeps across $k \in \{1 \dots 10\}$ on the Training set, recording Inertia and Silhouette scores
- [x] 2.2 Implement hyperparameter evaluation on the Development set (out-of-sample prediction using Train centroids as well as native Dev fitting)
- [x] 2.3 Implement comparative visualization plots and discrepancy tables contrasting Train vs. Development tuning curves and document observed differences

## 3. Final Model Training, Dendrograms & Test Evaluation

- [x] 3.1 Fit final optimal K-Means ($k=3$) and Hierarchical Agglomerative clustering models on the Training set
- [x] 3.2 Compute hierarchical linkage matrices and plot dendrograms with threshold cut analysis
- [x] 3.3 Project clusters and learned centroids into 2D feature space and 2D PCA space across Train, Dev, and Test sets
- [x] 3.4 Execute comprehensive evaluation on the holdout Test set (Silhouette, Davies-Bouldin, Calinski-Harabasz, MAE, MSE, RMSE, and confusion matrices)

## 4. Execution & Verification

- [x] 4.1 Run end-to-end execution of `clustering_lab4_train_dev_test.ipynb` to verify error-free execution and output generation
