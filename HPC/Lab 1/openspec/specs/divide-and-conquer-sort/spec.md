# divide-and-conquer-sort Specification

## Purpose
Implements divide-and-conquer sorting (Merge Sort) for a dynamically allocated array of integers provided by the user.

## Requirements

### Requirement: Dynamic Array Allocation and Input
The program SHALL prompt for array length $n$, dynamically allocate an array of $n$ integers, and read the values from standard input.

#### Scenario: Array input
- **WHEN** user enters size $n$ followed by $n$ integers
- **THEN** an array of $n$ elements is dynamically allocated and populated

### Requirement: Divide-and-Conquer Sorting
The program SHALL sort the array in non-decreasing order using a divide-and-conquer algorithm (Merge Sort).

#### Scenario: Unsorted array sorted accurately
- **WHEN** input array is `[38, 27, 43, 3, 9, 82, 10]`
- **THEN** sorted output is `[3, 9, 10, 27, 38, 43, 82]`

### Requirement: Memory Management
The program SHALL free all dynamically allocated memory buffers before program exit.

#### Scenario: Proper memory release
- **WHEN** sorting finishes and sorted array is displayed
- **THEN** memory allocated for the array is freed cleanly
