## Purpose

Provides OpenMP programs demonstrating multi-threaded data race conditions on shared resources and their resolution via OpenMP critical sections (`#pragma omp critical`).

## ADDED Requirements

### Requirement: Demonstration of Unsynchronized Race Condition
The system SHALL provide an OpenMP program where multiple concurrent threads execute updates on a shared counter/resource without synchronization primitives, thereby demonstrating a data race condition and non-deterministic final state.

#### Scenario: Multi-threaded concurrent execution without synchronization
- **WHEN** the unsynchronized race condition program is executed with multiple OpenMP threads (e.g., `OMP_NUM_THREADS >= 2`) where each thread performs a large number of increments on a shared counter
- **THEN** the final value of the shared counter SHALL deviate from the expected theoretical total (`num_threads * iterations_per_thread`) due to race conditions

#### Scenario: Single-threaded baseline execution
- **WHEN** the unsynchronized race condition program is executed with a single OpenMP thread (`OMP_NUM_THREADS=1`)
- **THEN** the final value of the shared counter SHALL equal the exact expected theoretical total

### Requirement: Thread-Safe Synchronization using Critical Section
The system SHALL provide an OpenMP program that synchronizes concurrent updates to the shared counter/resource using `#pragma omp critical`, preventing data races and guaranteeing correct mutual exclusion.

#### Scenario: Multi-threaded concurrent execution with critical section
- **WHEN** the critical section program is executed with multiple OpenMP threads (e.g., `OMP_NUM_THREADS = 2, 4, 8, ...`)
- **THEN** the final value of the shared counter SHALL match the exact expected theoretical total (`num_threads * iterations_per_thread`) across every run

#### Scenario: Verification under varying thread counts
- **WHEN** the critical section program is evaluated across different thread counts
- **THEN** the program SHALL report the configured thread count, the execution time, and confirm that the final counter matches the expected theoretical result
