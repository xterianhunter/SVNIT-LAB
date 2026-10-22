#include <stdio.h>
#include <omp.h>

int main() {
    printf("Using omp sections to divide tasks among threads:\n");

    #pragma omp parallel
    {
        #pragma omp sections
        {
            #pragma omp section
            {
                printf("Thread %d: Executing section 1\n", omp_get_thread_num());
            }

            #pragma omp section
            {
                printf("Thread %d: Executing section 2\n", omp_get_thread_num());
            }

            #pragma omp section
            {
                printf("Thread %d: Executing section 3\n", omp_get_thread_num());
            }
        }
    }

    return 0;
}
