#include <stdio.h>
#include <stdlib.h>
#include <omp.h>
#include "common.h"

// Shared resource accessed concurrently without synchronization
volatile long long shared_counter = 0;

int main(int argc, char* argv[]) {
    int num_threads = omp_get_max_threads();
    long long iterations_per_thread = 10000000LL;

    if (argc >= 2) {
        num_threads = atoi(argv[1]);
        if (num_threads <= 0) num_threads = 1;
    }
    if (argc >= 3) {
        iterations_per_thread = atoll(argv[2]);
        if (iterations_per_thread <= 0) iterations_per_thread = 10000000LL;
    }

    long long expected_total = (long long)num_threads * iterations_per_thread;

    printf("==============================================================\n");
    printf("   OpenMP Demonstration: Unsynchronized Race Condition       \n");
    printf("==============================================================\n");
    printf("Configured Threads      : %d\n", num_threads);
    printf("Iterations per Thread   : %lld\n", iterations_per_thread);
    printf("Expected Final Total    : %lld\n", expected_total);
    printf("--------------------------------------------------------------\n");
    printf("Executing parallel increment without synchronization...\n");

    shared_counter = 0;
    double start_time = omp_get_wtime();

    #pragma omp parallel num_threads(num_threads)
    {
        for (long long i = 0; i < iterations_per_thread; i++) {
            // Data race: concurrent read-modify-write without mutual exclusion
            shared_counter++;
        }
    }

    double end_time = omp_get_wtime();
    double elapsed_time = end_time - start_time;

    long long actual_total = shared_counter;
    long long lost_updates = expected_total - actual_total;
    double loss_percentage = ((double)lost_updates / (double)expected_total) * 100.0;

    printf("--------------------------------------------------------------\n");
    printf("Execution Time          : %.6f seconds\n", elapsed_time);
    printf("Actual Final Total      : %lld\n", actual_total);
    printf("Lost Updates            : %lld\n", lost_updates);
    printf("Error Rate              : %.2f%%\n", loss_percentage);
    printf("--------------------------------------------------------------\n");

    if (num_threads > 1 && lost_updates != 0) {
        printf("RESULT: [RACE CONDITION DETECTED] Multiple threads interleaved\n");
        printf("        un-atomically, resulting in lost updates.\n");
    } else if (num_threads == 1) {
        printf("RESULT: Single-threaded execution produced deterministic count.\n");
    } else {
        printf("RESULT: No lost updates observed in this run (rare timing coincidence).\n");
    }
    printf("==============================================================\n");

    return 0;
}
