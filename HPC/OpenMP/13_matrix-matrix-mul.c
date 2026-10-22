#include <stdio.h>
#include <stdlib.h>
#include <omp.h>

// Function to multiply matrices sequentially
void sequential_matrix_multiply(int **A, int **B, int **C, int N) {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            C[i][j] = 0;
            for (int k = 0; k < N; k++) {
                C[i][j] += A[i][k] * B[k][j];
            }
        }
    }
}

// Function to multiply matrices in parallel using OpenMP
void parallel_matrix_multiply(int **A, int **B, int **C, int N) {
    #pragma omp parallel for
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            C[i][j] = 0;
            for (int k = 0; k < N; k++) {
                C[i][j] += A[i][k] * B[k][j];
            }
        }
    }
}

// Function to allocate a 2D matrix dynamically
int **allocate_matrix(int N) {
    int **matrix = (int **)malloc(N * sizeof(int *));
    for (int i = 0; i < N; i++) {
        matrix[i] = (int *)malloc(N * sizeof(int));
    }
    return matrix;
}

// Function to free a 2D matrix
void free_matrix(int **matrix, int N) {
    for (int i = 0; i < N; i++) {
        free(matrix[i]);
    }
    free(matrix);
}

// Main function
int main() {
    int N = 1500; // Matrix size

    // Allocate matrices
    int **A = allocate_matrix(N);
    int **B = allocate_matrix(N);
    int **C_seq = allocate_matrix(N);
    int **C_par = allocate_matrix(N);

    // Initialize matrices A and B
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            A[i][j] = rand() % 100;
            B[i][j] = rand() % 100;
        }
    }

    // Sequential multiplication
    double start_time = omp_get_wtime();
    sequential_matrix_multiply(A, B, C_seq, N);
    double seq_time = omp_get_wtime() - start_time;
    printf("Sequential time: %f seconds\n", seq_time);

    // Parallel multiplication
    start_time = omp_get_wtime();
    parallel_matrix_multiply(A, B, C_par, N);
    double par_time = omp_get_wtime() - start_time;
    printf("Parallel time: %f seconds\n", par_time);

    // Verify correctness
    int correct = 1;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            if (C_seq[i][j] != C_par[i][j]) {
                correct = 0;
                break;
            }
        }
        if (!correct) break;
    }
    if (correct) {
        printf("Matrices match!\n");
    } else {
        printf("Error in parallel computation!\n");
    }

    // Free matrices
    free_matrix(A, N);
    free_matrix(B, N);
    free_matrix(C_seq, N);
    free_matrix(C_par, N);

    return 0;
}

