# min-max-dynamic-array Specification

## Purpose
Provides a minimal C console program to allocate memory dynamically for an array and determine its minimum and maximum elements.

## Requirements

### Requirement: Dynamic Array Allocation and Input
The program SHALL prompt for array size `n`, dynamically allocate memory for `n` integers, and read the elements from standard input.

#### Scenario: Valid array size and elements
- **WHEN** user inputs size `5` followed by integers `10 2 45 8 1`
- **THEN** memory for 5 integers is dynamically allocated and populated with the values

### Requirement: Single-Pass Minimum and Maximum Computation
The program SHALL determine the minimum and maximum values of the dynamically allocated array.

#### Scenario: Computing min and max for positive and negative numbers
- **WHEN** the array contains `[10, -5, 30, 2, 0]`
- **THEN** the computed minimum SHALL be `-5` and maximum SHALL be `30`

### Requirement: Memory Management
The program SHALL deallocate the dynamically allocated memory before program exit to avoid memory leaks.

#### Scenario: Memory freed on termination
- **WHEN** output is displayed and program terminates
- **THEN** previously allocated dynamic memory is freed using standard library deallocation
