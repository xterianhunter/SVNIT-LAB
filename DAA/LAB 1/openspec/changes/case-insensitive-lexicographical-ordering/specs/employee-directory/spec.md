## Purpose

Defines natural dictionary-order lexicographical sorting (case-insensitive primary comparison with deterministic tie-breaking) and duplicate detection for comma-separated employee directory names without using built-in sorting functions.

## ADDED Requirements

### Requirement: Comma-Separated User Input Parsing
The system SHALL accept a comma-separated list of employee names from user input, split by commas, trim leading and trailing whitespace from each name, and ignore empty tokens.

#### Scenario: Input parsing with mixed cases and spacing
- **WHEN** user inputs `"amit, Amit, rahul, Neha, Neha, Rahul"`
- **THEN** system extracts `["amit", "Amit", "rahul", "Neha", "Neha", "Rahul"]`

#### Scenario: Empty or whitespace-only input
- **WHEN** user inputs an empty string or whitespace `""`
- **THEN** system reports that the list is empty and terminates gracefully

---

### Requirement: Natural Dictionary Lexicographical Sorting
The system SHALL sort the employee names in natural dictionary order using a custom sorting algorithm without built-in sort functions. Comparison SHALL compare characters case-insensitively ('a'/'A' < 'b'/'B' ... < 'z'/'Z'). If two strings are case-insensitively identical, a deterministic secondary tie-breaker SHALL be applied.

#### Scenario: Alphabetical grouping across differing cases
- **WHEN** user inputs `"amit, Amit, rahul, Neha, Neha, Rahul"`
- **THEN** system outputs names grouped alphabetically: `["amit", "Amit", "Neha", "Neha", "rahul", "Rahul"]`

#### Scenario: Distinct alphabetical names
- **WHEN** user inputs `"Rahul, Amit, Karan, Neha"`
- **THEN** system outputs `["Amit", "Karan", "Neha", "Rahul"]`

---

### Requirement: Duplicate Name Detection and Reporting
The system SHALL scan the sorted employee directory to identify duplicate occurrences. Exact identical names occurring more than once SHALL be reported with their frequency. If no duplicate names exist, the system SHALL explicitly report `"No duplicate names exist."`

#### Scenario: List with duplicate occurrences
- **WHEN** user inputs `"amit, Amit, rahul, Neha, Neha, Rahul"`
- **THEN** system detects and reports `'Neha'` occurring 2 times

#### Scenario: List with no duplicates
- **WHEN** user inputs `"Amit, Karan, Neha, Rahul, Priya"`
- **THEN** system reports `"No duplicate names exist."`
