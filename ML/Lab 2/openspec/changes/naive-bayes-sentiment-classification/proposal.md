## Why

Text sentiment classification using probabilistic models is a fundamental NLP and machine learning task. This project implements the end-to-end sentiment classification workflow outlined in Assignment 2 on the IMDb movie review dataset (`aclImdb`), comparing Multinomial Naive Bayes and Binary/Bernoulli Naive Bayes classifiers, evaluating smoothing effects, and performing detailed error analysis using clean, modular code in a Jupyter Notebook.

## What Changes

- Create a clean, well-structured Jupyter Notebook (`assignment_2_naive_bayes.ipynb`) addressing all 7 assignment tasks.
- Implement data exploration on the `aclImdb` dataset (dataset size, class distribution, average document length, top 20 most frequent words).
- Implement a reusable NLP preprocessing pipeline (lowercasing, punctuation/special characters removal, tokenization, stopword removal, lemmatization/stemming) and compare dataset statistics before and after preprocessing.
- Implement Bag-of-Words feature extraction for frequency and binary representations.
- Train and evaluate Multinomial Naive Bayes and Binary (Bernoulli) Naive Bayes classifiers with accuracy, precision, recall, F1-score, and confusion matrix visualizations.
- Perform model comparison across all evaluation metrics.
- Conduct smoothing hyperparameter analysis ($\alpha$ parameter sweep) to study the impact of Laplace/Lidstone smoothing.
- Perform detailed qualitative and quantitative error analysis on at least 10 misclassified reviews, detailing actual/predicted labels, prominent features, and misclassification reasons.

## Capabilities

### New Capabilities
- `sentiment-classification`: End-to-end sentiment analysis pipeline on the IMDb dataset covering data exploration, preprocessing, BoW vectorization, Multinomial and Bernoulli Naive Bayes training/evaluation, smoothing parameter ablation, and error diagnostics.

### Modified Capabilities
*(None)*

## Impact

- Adds an interactive notebook `assignment_2_naive_bayes.ipynb` in the workspace root.
- Requires standard scientific Python libraries: `numpy`, `pandas`, `matplotlib`, `seaborn`, `nltk` (or `spacy`), and `scikit-learn`.
- Reads data from the local `aclImdb/` directory.
