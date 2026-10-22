## Purpose

Provides capabilities to parse user-provided comma-separated employee names, arrange them in lexicographical order using custom sorting without built-in sort utilities, and detect and display duplicate names (or report their absence).

## ADDED Requirements

### Requirement: Comma-Separated User Input Parsing
The system SHALL prompt the user to input employee names as a comma-separated string, split the string by commas, trim leading and trailing whitespace from each name, and ignore empty entries.

#### Scenario: Valid comma-separated names
- **WHEN** user inputs `"Amit, Neha, Amit, Rahul, Neha, Karan, Rahul"`
- **THEN** system extracts the list `["Amit", "Neha", "Amit", "Rahul", "Neha", "Karan", "Rahul"]`

#### Scenario: Input with irregular whitespace
- **WHEN** user inputs `"  Amit  , Neha ,   Karan  "`
- **THEN** system trims whitespace and extracts `["Amit", "Neha", "Karan"]`

#### Scenario: Empty input
- **WHEN** user inputs an empty string or whitespace only `""`
- **THEN** system reports that the list is empty and terminates gracefully without error

---

### Requirement: Custom Lexicographical Sorting
The system SHALL sort the employee names in lexicographical (dictionary) order using a custom comparison-based sorting algorithm implemented from scratch without using any built-in sorting functions.

#### Scenario: Sorting distinct mixed names
- **WHEN** user provides names `["Rahul", "Amit", "Karan", "Neha"]`
- **THEN** system outputs the sorted list `["Amit", "Karan", "Neha", "Rahul"]`

#### Scenario: Case-defined character ordering
- **WHEN** user provides names with mixed casing such as `["amit", "Amit", "AMIT"]`
- **THEN** system sorts them following standard ASCII lexicographical rules (`'A'` < `'a'`, ordering: `"AMIT"`, `"Amit"`, `"amit"`)

---

### Requirement: Duplicate Name Detection and Reporting
The system SHALL examine the employee names, identify all names that occur more than once, and display them. If no duplicate names exist in the input, the system SHALL explicitly display a message stating that no duplicate names exist.

#### Scenario: List containing multiple duplicates
- **WHEN** user provides `"Amit, Neha, Amit, Rahul, Neha, Karan, Rahul"`
- **THEN** system displays the sorted list and reports duplicate names: `"Amit"`, `"Neha"`, and `"Rahul"` (with their frequencies or as a unique list of duplicate names)

#### Scenario: List with no duplicates
- **WHEN** user provides `"Amit, Karan, Neha, Rahul, Priya"`
- **THEN** system displays the sorted list and explicitly reports `"No duplicate names exist."`

#### Scenario: All elements identical
- **WHEN** user provides `"Amit, Amit, Amit"`
- **THEN** system displays the sorted list and reports `"Amit"` as a duplicate occurring 3 times
