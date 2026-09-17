## 1. Notebook Scaffold & Data Preparation

- [x] 1.1 Initialize `knn_vs_decision_tree_analysis.ipynb` with environment imports (`numpy`, `pandas`, `matplotlib`, `seaborn`, `sklearn`) and verify all libraries import cleanly.
- [x] 1.2 Implement dataset loading (`load_breast_cancer`) with concise summary statistics and verify 569 samples and 30 numerical features are loaded.
- [x] 1.3 Implement stratified train-test splitting (75/25) and feature scaling via `StandardScaler` for KNN while retaining unscaled features for Decision Tree. Verify subset shapes and scaling statistics.

## 2. Decision Tree Classifier Implementation & Evaluation

- [x] 2.1 Add theory markdown cell with LaTeX mathematical formulas for Entropy, Information Gain, and Gini Impurity. Verify LaTeX equation rendering.
- [x] 2.2 Fit `DecisionTreeClassifier` with `criterion='entropy'` and visualize tree diagram using `plot_tree` with filled nodes and feature names. Verify visual output.
- [x] 2.3 Plot annotated confusion matrix heatmap, calculate classification report metrics (Accuracy, Precision, Recall, F1), and report misclassification error. Verify correct metric calculation.
- [x] 2.4 Calculate and plot misclassification error rate vs. `max_depth` (depths 1 through 15) to analyze underfitting and overfitting. Verify curve is rendered with axis labels.

## 3. K-Nearest Neighbors Classifier Implementation & Evaluation

- [x] 3.1 Add theory markdown cell with LaTeX mathematical formulas for Euclidean, Manhattan, and Minkowski distances and the majority voting rule. Verify LaTeX equation rendering.
- [x] 3.2 Fit `KNeighborsClassifier` on standardized features, plot annotated confusion matrix heatmap, and compute classification report and error metrics. Verify prediction performance.
- [x] 3.3 Compute and plot test misclassification error rate vs. $K$ ($K \in [1, 30]$) and annotate the optimal $K$ value. Verify curve clearly depicts neighborhood sensitivity.

## 4. Model Comparison & Verification

- [x] 4.1 Assemble a comparative performance table contrasting Accuracy, Precision, Recall, and F1-Score of both models alongside an analytical summary of trade-offs. Verify table output.
- [x] 4.2 Execute the notebook end-to-end to ensure all cells run sequentially without errors and generate expected plots and outputs.
