#include <stdio.h>
#include <omp.h>

#define N 400
#define NUM_THREADS 4

double A[N][N], B[N][N], C[N][N];

void init_matrices() {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            A[i][j] = 1.0;
            B[i][j] = 2.0;
            C[i][j] = 0.0;
        }
    }
}

int verify_result() {
    double expected = 2.0 * N;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            if (C[i][j] != expected) return 0;
        }
    }
    return 1;
}

// Coarse-grained: Outer loop (rows) partitioned across threads
void coarse_grained() {
    #pragma omp parallel for num_threads(NUM_THREADS)
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            double sum = 0.0;
            for (int k = 0; k < N; k++) {
                sum += A[i][k] * B[k][j];
            }
            C[i][j] = sum;
        }
    }
}

// Fine-grained: Inner loop parallelized repeatedly per row
void fine_grained() {
    for (int i = 0; i < N; i++) {
        #pragma omp parallel for num_threads(NUM_THREADS)
        for (int j = 0; j < N; j++) {
            double sum = 0.0;
            for (int k = 0; k < N; k++) {
                sum += A[i][k] * B[k][j];
            }
            C[i][j] = sum;
        }
    }
}

int main() {
    printf("Matrix Multiplication (%d x %d), Threads: %d\n", N, N, NUM_THREADS);

    init_matrices();
    double t_start = omp_get_wtime();
    coarse_grained();
    double t_coarse = omp_get_wtime() - t_start;
    int ok_c = verify_result();

    init_matrices();
    t_start = omp_get_wtime();
    fine_grained();
    double t_fine = omp_get_wtime() - t_start;
    int ok_f = verify_result();

    printf("Coarse-grained Time: %f s [%s]\n", t_coarse, ok_c ? "CORRECT" : "FAILED");
    printf("Fine-grained Time:   %f s [%s]\n", t_fine, ok_f ? "CORRECT" : "FAILED");

    return 0;
}
