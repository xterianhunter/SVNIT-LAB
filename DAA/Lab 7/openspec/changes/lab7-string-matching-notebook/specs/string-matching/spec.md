## Purpose

Provides simple, educational implementations and empirical comparative analysis for Naive, KMP, and Rabin-Karp string matching algorithms in Python.

## ADDED Requirements

### Requirement: Naive String Matching Implementation
The system SHALL implement the Naive String Matching algorithm to find all starting indices of pattern $P$ in text $T$ and record the exact number of character comparisons performed.

#### Scenario: Basic pattern matching with count
- **WHEN** text is "AABAACAADAABAABA" and pattern is "AABA"
- **THEN** the algorithm returns occurrences at indices [0, 9, 12] and reports the total character comparisons performed

#### Scenario: Worst-case behavior demonstration
- **WHEN** text consists of repeated characters (e.g., "AAAAAA") and pattern ends with a different character (e.g., "AAAB")
- **THEN** the algorithm demonstrates maximum character comparisons close to $(n - m + 1) \times m$

### Requirement: Knuth-Morris-Pratt (KMP) Implementation
The system SHALL compute the Longest Proper Prefix which is also Suffix (LPS) array without built-in matching functions and use it to find all pattern occurrences in text while recording character comparisons.

#### Scenario: LPS array computation
- **WHEN** the pattern is "ABABCABAB"
- **THEN** the system correctly computes the LPS array [0, 0, 1, 2, 0, 1, 2, 3, 4]

#### Scenario: Search using LPS array and comparison tracking
- **WHEN** searching pattern $P$ in text $T$ using KMP
- **THEN** all occurrence indices are returned and the total character comparisons are significantly fewer than Naive in repetitive patterns

### Requirement: Rabin-Karp String Matching Implementation
The system SHALL compute rolling hashes for the pattern and sliding windows of the text using an integer base and prime modulus, performing character-by-character verification on hash match and tracking both hash matches and verification operations.

#### Scenario: Successful search and verification count
- **WHEN** pattern $P$ occurs in text $T$
- **THEN** the algorithm returns matching indices, records the number of hash matches, and records character-by-character verifications

#### Scenario: Spurious hash collision demonstration
- **WHEN** evaluating two distinct substrings having identical hash values under a chosen modulus
- **THEN** the algorithm records a hash match but reports a verification mismatch without false positive match reporting

### Requirement: Experimental Benchmarks and Visualizations
The system SHALL run automated empirical tests across varying text lengths and pattern lengths, logging runtime and comparison statistics, and plotting graphs using matplotlib.

#### Scenario: Generate execution time vs input size
- **WHEN** benchmark is executed across increasing text sizes
- **THEN** a matplotlib line plot comparing runtime for Naive, KMP, and Rabin-Karp is generated and rendered

#### Scenario: Generate execution time vs pattern length
- **WHEN** benchmark is executed across increasing pattern lengths
- **THEN** a matplotlib line plot comparing runtime for Naive, KMP, and Rabin-Karp is generated and rendered

#### Scenario: Generate comparison count vs input size
- **WHEN** benchmark is executed across increasing text sizes
- **THEN** a matplotlib line plot comparing comparison counts for Naive vs KMP is generated and rendered
