#include <stdio.h>
#include <omp.h>

int main(void) {
    printf("Demonstrating OpenMP Tasks\n\n");

    #pragma omp parallel
    {
        #pragma omp single
        {
            printf("Thread %d (single) generating tasks...\n\n", omp_get_thread_num());

            for (int i = 1; i <= 6; i++) {
                #pragma omp task firstprivate(i)
                {
                    printf("Task %d executed by Thread %d of %d\n",
                           i, omp_get_thread_num(), omp_get_num_threads());
                }
            }

            printf("\nMaster/single thread waiting for tasks to complete...\n");
            #pragma omp taskwait
            printf("All tasks completed at taskwait barrier!\n");
        }
    }

    printf("\nParallel region exited.\n");
    return 0;
}
