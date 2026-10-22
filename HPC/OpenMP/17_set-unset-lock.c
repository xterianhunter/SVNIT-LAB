#include <stdio.h>
#include <omp.h>

int main() {
    int sum = 0;
    omp_lock_t lock;

    // Initialize the lock
    omp_init_lock(&lock);

    #pragma omp parallel for
    for (int i = 0; i < 10; i++) {
        omp_set_lock(&lock); // Acquire the lock
        sum += i; // Update sum
        printf("Thread %d added %d, sum = %d\n", omp_get_thread_num(), i, sum);
        omp_unset_lock(&lock); // Release the lock
    }

    // Destroy the lock
    omp_destroy_lock(&lock);

    printf("Final sum = %d\n", sum);
    return 0;
}

