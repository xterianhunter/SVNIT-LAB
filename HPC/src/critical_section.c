#include <stdio.h>
#include <stdlib.h>
#include <omp.h>
#include "common.h"

// Shared resource accessed concurrently with mutual exclusion
volatile long long shared_counter = 0;

int main(int argc, char* argv[]) {
    int num_threads = omp_get_max_threads();
    // Default iterations scaled for critical section overhead (locking per iteration)
    long long iterations_per_thread = 1000000LL;

    if (argc >= 2) {
        num_threads = atoi(argv[1]);
        if (num_threads <= 0) num_threads = 1;
    }
    if (argc >= 3) {
        iterations_per_thread = atoll(argv[2]);
        if (iterations_per_thread <= 0) iterations_per_thread = 1000000LL;
    }

    long long expected_total = (long long)num_threads * iterations_per_thread;

    printf("==============================================================\n");
    printf("   OpenMP Synchronization: Critical Section (#pragma omp critical)\n");
    printf("==============================================================\n");
    printf("Configured Threads      : %d\n", num_threads);
    printf("Iterations per Thread   : %lld\n", iterations_per_thread);
    printf("Expected Final Total    : %lld\n", expected_total);
    printf("--------------------------------------------------------------\n");
    printf("Executing synchronized parallel increment with critical section...\n");

    shared_counter = 0;
    double start_time = omp_get_wtime();

    #pragma omp parallel num_threads(num_threads)
    {
        for (long long i = 0; i < iterations_per_thread; i++) {
            // Critical section ensures atomic update via mutual exclusion
            #pragma omp critical (counter_lock)
            {
                shared_counter++;
            }
        }
    }

    double end_time = omp_get_wtime();
    double elapsed_time = end_time - start_time;

    long long actual_total = shared_counter;
    long long discrepancy = expected_total - actual_total;

    printf("--------------------------------------------------------------\n");
    printf("Execution Time          : %.6f seconds\n", elapsed_time);
    printf("Actual Final Total      : %lld\n", actual_total);
    printf("Discrepancy (Errors)    : %lld\n", discrepancy);
    printf("--------------------------------------------------------------\n");

    if (discrepancy == 0) {
        printf("RESULT: [VERIFICATION PASSED] Mutual exclusion guaranteed.\n");
        printf("        All %lld updates completed without race condition.\n", expected_total);
    } else {
        printf("RESULT: [VERIFICATION FAILED] Discrepancy observed (%lld).\n", discrepancy);
    }
    printf("==============================================================\n");

    return (discrepancy == 0) ? 0 : 1;
}
