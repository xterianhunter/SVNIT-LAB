#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <omp.h>
#include "common.h"

/**
 * Sequential baseline matrix-matrix multiplication: C = A * B
 */
void matmul_sequential(const double* A, const double* B, double* C, int n) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            double sum = 0.0;
            for (int k = 0; k < n; k++) {
                sum += A[i * n + k] * B[k * n + j];
            }
            C[i * n + j] = sum;
        }
    }
}

/**
 * Coarse-Grained Parallel Matrix Multiplication (Row-Level Decomposition).
 * Distributes outer loop iterations (rows) statically across threads.
 */
void matmul_coarse_grained(const double* A, const double* B, double* C, int n, int num_threads) {
    #pragma omp parallel for num_threads(num_threads) schedule(static)
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            double sum = 0.0;
            for (int k = 0; k < n; k++) {
                sum += A[i * n + k] * B[k * n + j];
            }
            C[i * n + j] = sum;
        }
    }
}

/**
 * Fine-Grained Parallel Matrix Multiplication (Element-Level Decomposition).
 * Distributes individual element computations dynamically with chunk size 1.
 */
void matmul_fine_grained(const double* A, const double* B, double* C, int n, int num_threads) {
    #pragma omp parallel for num_threads(num_threads) collapse(2) schedule(dynamic, 1)
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            double sum = 0.0;
            for (int k = 0; k < n; k++) {
                sum += A[i * n + k] * B[k * n + j];
            }
            C[i * n + j] = sum;
        }
    }
}

int main(int argc, char* argv[]) {
    int n = 1000;
    int num_threads = omp_get_max_threads();
    const char* mode = "all";

    if (argc >= 2) {
        n = atoi(argv[1]);
        if (n <= 0) n = 1000;
    }
    if (argc >= 3) {
        num_threads = atoi(argv[2]);
        if (num_threads <= 0) num_threads = 1;
    }
    if (argc >= 4) {
        mode = argv[3];
    }

    double memory_mb = 3.0 * (double)n * (double)n * sizeof(double) / (1024.0 * 1024.0);

    printf("========================================================================\n");
    printf("   OpenMP Parallel Matrix-Matrix Multiplication (C = A x B)             \n");
    printf("========================================================================\n");
    printf("Matrix Dimension (N x N): %d x %d\n", n, n);
    printf("Total Memory Required   : %.2f MB\n", memory_mb);
    printf("Total Operations (FLOPs): %.3e\n", 2.0 * (double)n * (double)n * (double)n);
    printf("Configured Threads      : %d\n", num_threads);
    printf("Execution Mode          : %s\n", mode);
    printf("------------------------------------------------------------------------\n");

    // Allocate matrices
    double* A = allocate_matrix(n);
    double* B = allocate_matrix(n);
    double* C_seq = allocate_matrix(n);
    double* C_coarse = allocate_matrix(n);
    double* C_fine = allocate_matrix(n);

    // Initialize input matrices with deterministic random numbers
    init_matrix_random(A, n, 42);
    init_matrix_random(B, n, 84);

    double t_seq = 0.0, t_coarse = 0.0, t_fine = 0.0;
    bool run_seq = (strcmp(mode, "all") == 0 || strcmp(mode, "seq") == 0);
    bool run_coarse = (strcmp(mode, "all") == 0 || strcmp(mode, "coarse") == 0);
    bool run_fine = (strcmp(mode, "all") == 0 || strcmp(mode, "fine") == 0);

    // 1. Sequential Baseline
    if (run_seq) {
        printf("[1/3] Running Sequential Baseline...\n");
        zero_matrix(C_seq, n);
        double start = omp_get_wtime();
        matmul_sequential(A, B, C_seq, n);
        t_seq = omp_get_wtime() - start;
        printf("      Sequential Time: %.4f s (%.2f GFLOPS)\n", t_seq, calculate_gflops(n, t_seq));
    }

    // 2. Coarse-Grained Decomposition
    if (run_coarse) {
        printf("[2/3] Running Coarse-Grained Decomposition (Row-Level static)...\n");
        zero_matrix(C_coarse, n);
        double start = omp_get_wtime();
        matmul_coarse_grained(A, B, C_coarse, n, num_threads);
        t_coarse = omp_get_wtime() - start;
        printf("      Coarse-Grained Time: %.4f s (%.2f GFLOPS)\n", t_coarse, calculate_gflops(n, t_coarse));

        if (run_seq) {
            printf("      ");
            verify_matrix(C_seq, C_coarse, n, 1e-9);
        }
    }

    // 3. Fine-Grained Decomposition
    if (run_fine) {
        printf("[3/3] Running Fine-Grained Decomposition (Element-Level dynamic(1))...\n");
        zero_matrix(C_fine, n);
        double start = omp_get_wtime();
        matmul_fine_grained(A, B, C_fine, n, num_threads);
        t_fine = omp_get_wtime() - start;
        printf("      Fine-Grained Time: %.4f s (%.2f GFLOPS)\n", t_fine, calculate_gflops(n, t_fine));

        if (run_seq) {
            printf("      ");
            verify_matrix(C_seq, C_fine, n, 1e-9);
        }
    }

    // Comparative Summary Table
    if (strcmp(mode, "all") == 0) {
        double s_coarse = (t_coarse > 0) ? (t_seq / t_coarse) : 0.0;
        double s_fine = (t_fine > 0) ? (t_seq / t_fine) : 0.0;
        double e_coarse = (num_threads > 0) ? (s_coarse / num_threads) * 100.0 : 0.0;
        double e_fine = (num_threads > 0) ? (s_fine / num_threads) * 100.0 : 0.0;

        printf("\n========================================================================\n");
        printf("                      PERFORMANCE COMPARISON REPORT                     \n");
        printf("========================================================================\n");
        printf("%-22s | %-12s | %-10s | %-10s | %-10s\n",
               "Decomposition Method", "Time (sec)", "GFLOPS", "Speedup", "Efficiency");
        printf("------------------------------------------------------------------------\n");
        printf("%-22s | %10.4f s | %10.2f | %10.2fx | %9.1f%%\n",
               "Sequential Baseline", t_seq, calculate_gflops(n, t_seq), 1.0, 100.0);
        printf("%-22s | %10.4f s | %10.2f | %10.2fx | %9.1f%%\n",
               "Coarse-Grained (Row)", t_coarse, calculate_gflops(n, t_coarse), s_coarse, e_coarse);
        printf("%-22s | %10.4f s | %10.2f | %10.2fx | %9.1f%%\n",
               "Fine-Grained (Element)", t_fine, calculate_gflops(n, t_fine), s_fine, e_fine);
        printf("========================================================================\n");

        if (t_coarse < t_fine) {
            double speed_diff = t_fine / t_coarse;
            printf("ANALYSIS: Coarse-grained decomposition is %.2fx faster than fine-grained.\n", speed_diff);
            printf("          Fine-grained decomposition suffers from heavy scheduling overhead\n");
            printf("          and cache thrashing due to dynamic scheduling of %d individual tasks.\n", n * n);
        } else {
            printf("ANALYSIS: Fine-grained decomposition performed comparably to coarse-grained.\n");
        }
        printf("========================================================================\n");
    }

    // Cleanup
    free_matrix(A);
    free_matrix(B);
    free_matrix(C_seq);
    free_matrix(C_coarse);
    free_matrix(C_fine);

    return 0;
}
