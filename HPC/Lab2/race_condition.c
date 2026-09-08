#include <stdio.h>
#include <omp.h>

#define NUM_THREADS 4
#define ITERS_PER_THREAD 500000

int main() {
    volatile int counter = 0;
    int expected = NUM_THREADS * ITERS_PER_THREAD;

    #pragma omp parallel num_threads(NUM_THREADS)
    {
        for (int i = 0; i < ITERS_PER_THREAD; i++) {
            counter++; // Unsynchronized concurrent write (race condition)
        }
    }

    printf("--- Race Condition Demonstration ---\n");
    printf("Threads:  %d\n", NUM_THREADS);
    printf("Expected: %d\n", expected);
    printf("Actual:   %d (lost updates: %d)\n", counter, expected - counter);

    return 0;
}
