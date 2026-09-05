## Purpose

Identifies the first unique employee name in an access log sequence using two distinct algorithmic approaches (in-place repeated comparisons and auxiliary frequency map) and provides comparative metrics.

## ADDED Requirements

### Requirement: Comma-Separated Access Log Parsing
The system SHALL accept a comma-separated string representing employee access records, parse individual employee names, trim surrounding whitespace, and discard empty entries.

#### Scenario: Standard access sequence
- **WHEN** user inputs `"Amit, Neha, Amit, Rahul, Neha, Karan, Rahul"`
- **THEN** system extracts the list `["Amit", "Neha", "Amit", "Rahul", "Neha", "Karan", "Rahul"]`

#### Scenario: Empty access sequence
- **WHEN** user inputs an empty or whitespace-only string `""`
- **THEN** system indicates the list is empty and terminates gracefully

---

### Requirement: First Unique Employee Identification (Approach 1: Repeated Comparisons)
The system SHALL iterate through the employee sequence and count occurrences of each employee by comparing against all elements in the list. The first employee whose total occurrence count equals 1 SHALL be returned as the first unique employee.

#### Scenario: Access log with unique employee
- **WHEN** sequence is `["Amit", "Neha", "Amit", "Rahul", "Neha", "Karan", "Rahul"]`
- **THEN** system identifies `"Karan"` as the first unique employee

#### Scenario: Access log with no unique employees
- **WHEN** sequence is `["Amit", "Neha", "Amit", "Neha"]`
- **THEN** system reports `"No unique employee found."`

---

### Requirement: First Unique Employee Identification (Approach 2: Auxiliary Data Structure)
The system SHALL compute employee occurrence counts using an auxiliary frequency map / dictionary, then iterate through the original sequence in order to find and return the first name with a frequency of 1.

#### Scenario: Identification using frequency map
- **WHEN** sequence is `["Amit", "Neha", "Amit", "Rahul", "Neha", "Karan", "Rahul"]`
- **THEN** system constructs frequency map `{"Amit": 2, "Neha": 2, "Rahul": 2, "Karan": 1}` and identifies `"Karan"` as the first unique employee

#### Scenario: Single-element sequence
- **WHEN** sequence is `["Karan"]`
- **THEN** system identifies `"Karan"` as the unique employee

---

### Requirement: Algorithmic Equivalence and Comparison
Both approaches SHALL produce identical results for any valid input, and the system SHALL present time complexity ($O(n^2)$ vs $O(n)$) and auxiliary space complexity ($O(1)$ vs $O(n)$) comparisons.

#### Scenario: All elements unique
- **WHEN** sequence is `["Amit", "Neha", "Karan"]`
- **THEN** both approaches identify `"Amit"` as the first unique employee
