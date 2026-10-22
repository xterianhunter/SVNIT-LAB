// Explanation

//  Task 1: Computes C = A + B. It produces C as output (depend(out: C)).
//  Task 2: Computes D = A * B. It produces D as output (depend(out: D)).
//  Task 3: Prints the first 5 elements of C and D. It depends on both C and D being completed (depend(in: C, D)).


#include <stdio.h>
#include <omp.h>

#define SIZE 100

int main() {
    int A[SIZE], B[SIZE], C[SIZE], D[SIZE];

    // Initialize arrays
    for (int i = 0; i < SIZE; i++) {
        A[i] = i;
        B[i] = i * 2;
    }

    #pragma omp parallel
    {
        #pragma omp single
        {
            // Task 1: Compute C = A + B
            #pragma omp task depend(out: C)
            {
                for (int i = 0; i < SIZE; i++) {
                    C[i] = A[i] + B[i];
                }
                printf("Task 1 completed: C = A + B\n");
            }

            // Task 2: Compute D = A * B
            #pragma omp task depend(out: D)
            {
                for (int i = 0; i < SIZE; i++) {
                    D[i] = A[i] * B[i];
                }
                printf("Task 2 completed: D = A * B\n");
            }

            // Task 3: Print the first 5 elements of C and D (depends on Task 1 and Task 2)
            #pragma omp task depend(in: C, D)
            {
                printf("Task 3 completed: First 5 elements of C and D\n");
                for (int i = 0; i < 5; i++) {
                    printf("C[%d] = %d, D[%d] = %d\n", i, C[i], i, D[i]);
                }
            }
        }
    }

    return 0;
}

