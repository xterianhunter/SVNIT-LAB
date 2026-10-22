#include <stdio.h>
#include <omp.h>

int main(void) {
    printf("Demonstrating OpenMP Sections\n\n");

    #pragma omp parallel sections
    {
        #pragma omp section
        {
            printf("Section A executed by Thread %d of %d\n", 
                   omp_get_thread_num(), omp_get_num_threads());
        }

        #pragma omp section
        {
            printf("Section B executed by Thread %d of %d\n", 
                   omp_get_thread_num(), omp_get_num_threads());
        }

        #pragma omp section
        {
            printf("Section C executed by Thread %d of %d\n", 
                   omp_get_thread_num(), omp_get_num_threads());
        }

        #pragma omp section
        {
            printf("Section D executed by Thread %d of %d\n", 
                   omp_get_thread_num(), omp_get_num_threads());
        }
    }

    printf("\nAll sections completed. Implicit barrier passed.\n");
    return 0;
}
