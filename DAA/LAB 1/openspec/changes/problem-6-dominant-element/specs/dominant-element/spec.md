## Purpose

Identifies whether a dominant (majority) element (> n/2 occurrences) exists in an integer array of size $n$ using two distinct approaches (repeated comparisons and Boyer-Moore voting algorithm) and compares their performance.

## ADDED Requirements

### Requirement: Comma-Separated Input Array Parsing
The system SHALL parse a comma-separated string of integers into an integer list, trimming whitespace and validating numerical values.

#### Scenario: Standard integer sequence
- **WHEN** user inputs `"2, 2, 1, 2, 3, 2, 2"`
- **THEN** system produces integer list `[2, 2, 1, 2, 3, 2, 2]`

#### Scenario: Empty integer sequence
- **WHEN** user inputs an empty or whitespace-only string
- **THEN** system reports that the array is empty and terminates gracefully

---

### Requirement: Dominant Element Detection (Approach 1: Repeated Counting)
The system SHALL evaluate each element by counting its occurrences across the entire array. If any element occurs strictly more than $\lfloor n/2 \rfloor$ times, the system SHALL report it as the dominant element.

#### Scenario: Array with a dominant element
- **WHEN** array is `[2, 2, 1, 2, 3, 2, 2]` (size 7, threshold 3)
- **THEN** system determines that element `2` occurs 5 times ($5 > 3$) and returns `2`

#### Scenario: Array with no dominant element
- **WHEN** array is `[1, 2, 3, 4]` (size 4, threshold 2)
- **THEN** system reports `"No dominant element exists."`

---

### Requirement: Dominant Element Detection (Approach 2: Boyer-Moore Voting Algorithm)
The system SHALL find the majority candidate using Boyer-Moore voting logic in $O(n)$ time and $O(1)$ space, verify the candidate in a second linear pass, and return the dominant element if count $> \lfloor n/2 \rfloor$.

#### Scenario: Single linear-time candidate identification
- **WHEN** array is `[2, 2, 1, 2, 3, 2, 2]`
- **THEN** system identifies candidate `2` in pass 1, verifies count `5 > 3` in pass 2, and returns `2`

#### Scenario: Candidate fails verification
- **WHEN** array is `[1, 2, 3]`
- **THEN** system selects a candidate in pass 1, observes count $1 \le 1$ in pass 2, and reports `"No dominant element exists."`

---

### Requirement: Algorithmic Equivalence and Comparison
Both approaches SHALL produce identical results for every valid input, and the system SHALL present time complexity ($O(n^2)$ vs $O(n)$) and auxiliary space complexity ($O(1)$ vs $O(1)$) comparisons.

#### Scenario: Single-element array
- **WHEN** array is `[42]`
- **THEN** both approaches identify `42` as the dominant element
