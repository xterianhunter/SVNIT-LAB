## Purpose

Provides a clean, educational Jupyter Notebook that benchmarks K-Nearest Neighbors and Decision Tree classifiers on a standard classification dataset with theoretical formulas, tree and confusion matrix visualizations, and parametric error curves.

## ADDED Requirements

### Requirement: Dataset Loading and Minimal Preprocessing
The notebook SHALL load a standard multi-feature classification dataset directly from `sklearn.datasets` and apply only necessary preprocessing operations without extraneous or redundant exploratory data analysis.

#### Scenario: Dataset ingestion and feature scaling
- **WHEN** the dataset loading and preprocessing cells are executed
- **THEN** the dataset is loaded into feature matrix $X$ and label vector $y$, split into stratified training and testing subsets, and transformed using `StandardScaler` for distance-sensitive modeling while keeping raw features for tree-based comparisons.

### Requirement: Decision Tree Classification and Splitting Formulation
The notebook SHALL present the formal mathematical definitions of decision tree node-splitting criteria and execute Decision Tree training, tree visualization, confusion matrix generation, and error evaluation.

#### Scenario: Mathematical exposition of splitting criteria
- **WHEN** the Decision Tree theory markdown cell is rendered
- **THEN** it displays LaTeX mathematical formulas for Entropy ($H(S) = -\sum p_i \log_2 p_i$), Gini Impurity ($Gini(S) = 1 - \sum p_i^2$), and Information Gain ($IG(S, A) = H(S) - \sum \frac{|S_v|}{|S|} H(S_v)$).

#### Scenario: Decision Tree visualization and evaluation
- **WHEN** the Decision Tree modeling cells are executed
- **THEN** the system fits a `DecisionTreeClassifier`, renders a graphical visualization of the tree using `sklearn.tree.plot_tree`, displays an annotated confusion matrix heatmap, outputs accuracy, precision, recall, F1-score, and plots a test error rate vs. maximum tree depth curve.

### Requirement: K-Nearest Neighbors Classification and Distance Formulation
The notebook SHALL present the formal mathematical definitions of distance metrics and execute KNN model training on scaled data, confusion matrix generation, and parametric error curve evaluation.

#### Scenario: Mathematical exposition of distance metrics
- **WHEN** the KNN theory markdown cell is rendered
- **THEN** it displays LaTeX mathematical formulas for Euclidean distance ($d(p, q) = \sqrt{\sum (p_i - q_i)^2}$), Manhattan distance ($d(p, q) = \sum |p_i - q_i|$), and Minkowski distance ($d(p, q) = (\sum |p_i - q_i|^p)^{1/p}$).

#### Scenario: KNN evaluation and error rate vs K curve
- **WHEN** the KNN modeling cells are executed
- **THEN** the system trains a `KNeighborsClassifier` on standardized features, displays an annotated confusion matrix heatmap, outputs accuracy, precision, recall, F1-score, and computes and plots the misclassification error rate across varying values of $k$ to identify the optimal neighbor count.

### Requirement: Comparative Summary
The notebook SHALL present a concise comparative performance table summarizing the metrics and trade-offs between the Decision Tree and KNN models.

#### Scenario: Comparison table generation
- **WHEN** the comparison cell is executed
- **THEN** a summary table is displayed comparing accuracy, precision, recall, and F1-score for both models alongside a brief concluding synthesis.
