## Purpose

Determines whether an employee directory is sorted, identifies all adjacent ordering violations ($A[i] > A[i+1]$) without sorting the array, and determines whether exchanging exactly two names can restore the sorted ordering.

## ADDED Requirements

### Requirement: Sortedness Determination Without Array Sorting
The system SHALL verify whether an input list of $n$ employee names is sorted in non-decreasing lexicographical order by performing a single linear pass of adjacent comparisons ($A[i] \le A[i+1]$) in $O(n)$ time without calling any full array sorting routines.

#### Scenario: Already sorted directory
- **WHEN** list is `["Amit", "Karan", "Neha", "Priya", "Rahul"]`
- **THEN** system determines there are 0 violations and reports `"The employee directory is already sorted."`

#### Scenario: Directory with 0 or 1 name
- **WHEN** list is `["Amit"]` or `[]`
- **THEN** system confirms the directory is vacuously sorted

---

### Requirement: Ordering Violation Identification
When an unsorted list is provided, the system SHALL identify and report all adjacent positions $i$ where $A[i] > A[i+1]$, including the names at those positions.

#### Scenario: Single adjacent violation
- **WHEN** list is `["Amit", "Karan", "Neha", "Rahul", "Priya"]`
- **THEN** system reports 1 violation at position 3 (0-indexed) where `"Rahul" > "Priya"`

#### Scenario: Multiple ordering violations
- **WHEN** list is `["Amit", "Neha", "Karan", "Rahul", "Priya"]`
- **THEN** system reports 2 violations: at position 1 (`"Neha" > "Karan"`) and position 3 (`"Rahul" > "Priya"`)

---

### Requirement: Single-Swap Fixability Determination and Reporting
The system SHALL determine whether exchanging exactly two names can make the complete list sorted.
- If exchanging two names restores sorted order, the system SHALL report the two positions $(x, y)$ and the corresponding employee names.
- If exchanging two names cannot restore sorted order, the system SHALL report that exchanging two names is insufficient.

#### Scenario: Fixable by adjacent swap
- **WHEN** list is `["Amit", "Karan", "Neha", "Rahul", "Priya"]`
- **THEN** system determines swapping position 3 (`"Rahul"`) and position 4 (`"Priya"`) yields `["Amit", "Karan", "Neha", "Priya", "Rahul"]` and reports success with positions `(3, 4)`

#### Scenario: Fixable by non-adjacent swap
- **WHEN** list is `["Rahul", "Karan", "Neha", "Priya", "Amit"]`
- **THEN** system determines swapping position 0 (`"Rahul"`) and position 4 (`"Amit"`) yields `["Amit", "Karan", "Neha", "Priya", "Rahul"]` and reports success with positions `(0, 4)`

#### Scenario: Unfixable by a single swap
- **WHEN** list is `["Amit", "Neha", "Karan", "Rahul", "Priya"]`
- **THEN** system determines a single swap cannot sort the list and reports `"Exchanging only two names cannot make the list sorted."`
