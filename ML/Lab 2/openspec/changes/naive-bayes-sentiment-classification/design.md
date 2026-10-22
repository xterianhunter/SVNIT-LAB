## Context

The assignment requires implementing a complete text classification experiment on the IMDb movie review dataset (`aclImdb`) using Naive Bayes classifiers. See `proposal.md` for motivation and `specs/sentiment-classification/spec.md` for functional requirements.

The dataset contains 25,000 training reviews (12.5k positive, 12.5k negative) and 25,000 test reviews (12.5k positive, 12.5k negative) in raw `.txt` files under `aclImdb/train` and `aclImdb/test`.

## Goals / Non-Goals

**Goals:**
- Provide a clean, modular, self-contained Jupyter Notebook (`assignment_2_naive_bayes.ipynb`) answering all 7 tasks in sequence.
- Write concise, readable, and well-commented Python code without unnecessary bloat or complexity.
- Support end-to-end execution with visual plots (confusion matrices, smoothing curves, top word frequency bar plots).
- Provide insightful qualitative error analysis explaining root causes for misclassification on at least 10 instances.

**Non-Goals:**
- Training heavy deep learning models (e.g., RNNs, BERT) or complex ensembles outside the scope of Naive Bayes.
- Building a standalone web application or deployment service.

## Decisions

### 1. Data Ingestion & Representation
- **Decision**: Load files directly from `aclImdb/train/{pos,neg}` and `aclImdb/test/{pos,neg}` into pandas DataFrames containing `text` and binary integer `label` (1 for positive, 0 for negative).
- **Rationale**: Pandas DataFrames offer clean slicing, exploration, and column transformations.
- **Alternatives Considered**: Ingesting as raw lists or custom generator classes; DataFrames provide superior exploration utilities for Task 1.

### 2. Preprocessing Strategy
- **Decision**: Implement a streamlined pipeline function `preprocess_text(text)` that:
  1. Strips HTML markup (`<br />` tags).
  2. Converts to lowercase.
  3. Strips punctuation and digits using regex `[^a-z\s]`.
  4. Tokenizes by whitespace.
  5. Filters standard English stopwords.
  6. Applies WordNet lemmatization (with PorterStemmer as an alternate option).
- **Rationale**: Keeps the pipeline transparent, fast, and directly maps to the assignment's required steps.

### 3. Vectorization & Feature Extraction
- **Decision**: Use `sklearn.feature_extraction.text.CountVectorizer` configured with custom or preprocessed tokens, generating count matrices for Multinomial Naive Bayes and binary occurrences (`binary=True`) for Bernoulli Naive Bayes.
- **Rationale**: Utilizes fast C-based sparse matrix representations, preventing high memory overhead on the 50k corpus.

### 4. Classification Models & Smoothing Study
- **Decision**: Use `MultinomialNB` and `BernoulliNB` from `sklearn.naive_bayes`. Sweep Laplace smoothing parameter $\alpha \in [10^{-3}, 10^2]$ to record accuracy and macro F1 scores, plotting the performance curve.
- **Rationale**: Directly answers Tasks 4, 5, and 6 with standard, robust implementations.

### 5. Error Analysis & Feature Attribution
- **Decision**: Filter test predictions where $y_{\text{true}} \neq y_{\text{pred}}$, sample 5 False Positives and 5 False Negatives, and compute log-likelihood ratios of the most influential tokens in those documents to explain the misclassification reason.
- **Rationale**: Gives rigorous, evidence-based explanations of why the Naive Bayes assumption failed (e.g., negations like "not good", sarcastic phrasing, or mixed sentiment words).

## Risks / Trade-offs

- **[Risk] Preprocessing speed on 50,000 documents** → **Mitigation**: Use efficient compiled regex patterns and list comprehensions; optionally limit vocabulary size (e.g., `max_features=10000` or `min_df=5`) to keep vectorization and smoothing sweeps fast.
- **[Risk] Missing NLTK corpora (stopwords, wordnet)** → **Mitigation**: Add automatic `nltk.download()` calls with exception handling / fallback stopword list in the first cell of the notebook.
