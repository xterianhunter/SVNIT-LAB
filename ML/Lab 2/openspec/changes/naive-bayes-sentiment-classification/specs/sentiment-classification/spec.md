## Purpose

Provides end-to-end sentiment classification capabilities on the IMDb movie review dataset using Naive Bayes classifiers, covering data exploration, text preprocessing, feature extraction, model training, evaluation, smoothing analysis, and qualitative error diagnostics.

## ADDED Requirements

### Requirement: Dataset Loading and Exploration
The system SHALL load the train and test splits from the `aclImdb` dataset directory and compute exploratory data statistics including document counts, class balance, document lengths, and corpus-wide word frequencies.

#### Scenario: Exploration statistics generation
- **WHEN** the exploration pipeline processes the IMDb dataset
- **THEN** it reports total document count (50,000 total: 25,000 train, 25,000 test), class distributions (balanced pos/neg), average document length in words, and the top 20 most frequent raw words.

### Requirement: Text Preprocessing Pipeline
The system SHALL provide a modular text preprocessing pipeline that converts text to lowercase, removes punctuation and special characters, tokenizes sentences into words, removes English stopwords, and applies lemmatization or stemming.

#### Scenario: Preprocessing review texts
- **WHEN** raw review texts containing punctuation, uppercase characters, HTML tags, and stopwords are passed through the pipeline
- **THEN** cleaned, normalized tokens are returned, and a before/after comparison table is presented showing text transformations and vocabulary reduction.

### Requirement: Bag-of-Words Feature Extraction
The system SHALL transform preprocessed review texts into numerical feature vectors using Bag-of-Words representations for both term frequency counts and binary word occurrences.

#### Scenario: Vectorizing train and test sets
- **WHEN** preprocessed train and test token collections are passed to the vectorizer
- **THEN** it generates count matrices for Multinomial Naive Bayes and binary presence/absence matrices for Bernoulli Naive Bayes without data leakage across splits.

### Requirement: Naive Bayes Model Training and Evaluation
The system SHALL train Multinomial Naive Bayes and Binary (Bernoulli) Naive Bayes classifiers on the training data and evaluate them on the test set.

#### Scenario: Model evaluation and metrics
- **WHEN** trained classifiers predict sentiment labels on the test set
- **THEN** the system computes accuracy, precision, recall, F1-score, and renders confusion matrices for both models.

### Requirement: Model Performance Comparison
The system SHALL compare the classification performance of Multinomial Naive Bayes and Binary Naive Bayes in a structured comparative table and chart.

#### Scenario: Comparative performance analysis
- **WHEN** both classifiers complete evaluation on the test set
- **THEN** a side-by-side comparison of accuracy, precision, recall, and F1-score is generated highlighting the superior model.

### Requirement: Laplace Smoothing Sensitivity Analysis
The system SHALL evaluate the impact of the additive smoothing parameter ($\alpha$) on model performance across a range of values.

#### Scenario: Smoothing parameter variation
- **WHEN** the smoothing parameter $\alpha$ is varied over multiple orders of magnitude (e.g., $10^{-3}$ to $10^1$)
- **THEN** test accuracy and F1-scores are plotted against $\alpha$ to show the optimal smoothing level and its effect on unseen words.

### Requirement: Misclassification Error Analysis
The system SHALL identify at least 10 misclassified test documents and analyze the contributing features and reasons for misclassification.

#### Scenario: Diagnostic breakdown of errors
- **WHEN** error analysis is performed on test set predictions
- **THEN** at least 10 misclassified reviews (including false positives and false negatives) are displayed with their actual label, predicted label, top contributing word features, and diagnosed reasons (e.g., negation, sarcasm, mixed sentiments).
