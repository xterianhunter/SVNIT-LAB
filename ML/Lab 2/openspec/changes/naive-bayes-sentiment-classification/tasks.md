## 1. Environment & Data Exploration (Task 1)

- [x] 1.1 Create Jupyter Notebook `assignment_2_naive_bayes.ipynb` with environment setup and implement data loading from `aclImdb/` directory, verifying total document counts (25,000 train, 25,000 test).
- [x] 1.2 Implement data exploration cells computing class distribution, calculating average review document lengths, and generating a frequency chart of the top 20 most frequent words.

## 2. Text Preprocessing Pipeline & Comparison (Task 2)

- [x] 2.1 Implement the text preprocessing pipeline (lowercasing, punctuation/special character removal, tokenization, stopword removal, lemmatization) and verify tokenization outputs on sample reviews.
- [x] 2.2 Implement dataset comparison before and after preprocessing, displaying sample review transformations and vocabulary size reduction metrics.

## 3. Feature Extraction (Task 3)

- [x] 3.1 Implement Bag-of-Words feature extraction using `CountVectorizer` to generate term-frequency matrices for Multinomial NB and binary indicator matrices for Bernoulli NB, verifying matrix shapes and sparsity.

## 4. Naive Bayes Classification & Model Comparison (Tasks 4 & 5)

- [x] 4.1 Train Multinomial Naive Bayes and Binary (Bernoulli) Naive Bayes models, predict test set labels, and compute accuracy, precision, recall, and F1-score.
- [x] 4.2 Generate and plot confusion matrices for both classifiers and display a structured performance comparison table.

## 5. Smoothing Analysis & Error Diagnostics (Tasks 6 & 7)

- [x] 5.1 Implement additive smoothing ($\alpha$) hyperparameter sweep across a range of values ($10^{-3}$ to $10^2$), plotting accuracy and F1 score curves to analyze the effect of smoothing.
- [x] 5.2 Implement error analysis extracting at least 10 misclassified test documents (5 false positives and 5 false negatives), showing actual label, predicted label, influential features, and detailed misclassification root causes.
- [x] 5.3 Provide concluding analytical report explaining which model performs best and why based on empirical and theoretical Naive Bayes principles.

## 6. End-to-End Notebook Execution & Verification

- [x] 6.1 Run the complete notebook non-interactively or verify cell execution to ensure all cells execute without errors and all figures render properly.
