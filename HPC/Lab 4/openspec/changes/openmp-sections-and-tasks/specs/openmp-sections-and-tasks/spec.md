## Purpose

Demonstrates the syntax and runtime behavior of OpenMP `sections` and OpenMP `task` pragmas in C through concise, separate showcase programs.

## ADDED Requirements

### Requirement: OpenMP Sections Demonstration
The system SHALL provide a standalone C demonstration program (`sections_demo.c`) showcasing non-iterative work-sharing across parallel threads using `#pragma omp parallel sections` and `#pragma omp section`.

#### Scenario: Compile and execute sections demonstration
- **WHEN** compiled with an OpenMP-capable C compiler and executed with multiple threads
- **THEN** each defined section block executes concurrently or distinctively across available threads, printing the executing thread ID and designated section message without data races.

### Requirement: OpenMP Task Demonstration
The system SHALL provide a standalone C demonstration program (`task_demo.c`) showcasing dynamic asynchronous task creation and synchronization using `#pragma omp parallel`, `#pragma omp single`, `#pragma omp task`, and `#pragma omp taskwait`.

#### Scenario: Compile and execute task demonstration
- **WHEN** compiled with an OpenMP-capable C compiler and executed with multiple threads
- **THEN** asynchronous tasks created inside a single region are executed dynamically by available worker threads, synchronized at taskwait, and print the executing thread ID and task identifier.
