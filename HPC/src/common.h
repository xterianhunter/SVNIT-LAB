#ifndef COMMON_H
#define COMMON_H

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <math.h>
#include <time.h>
#include <omp.h>
#include <string.h>

/**
 * Allocate a contiguous 1D array representing an N x N matrix of doubles.
 */
static inline double* allocate_matrix(int n) {
    size_t size = (size_t)n * (size_t)n * sizeof(double);
    double* mat = (double*)malloc(size);
    if (!mat) {
        fprintf(stderr, "Error: Memory allocation failed for %dx%d matrix (%.2f MB)\n",
                n, n, (double)size / (1024.0 * 1024.0));
        exit(EXIT_FAILURE);
    }
    return mat;
}

/**
 * Free an allocated matrix.
 */
static inline void free_matrix(double* mat) {
    if (mat) {
        free(mat);
    }
}

/**
 * Initialize matrix with pseudo-random values between 0.0 and 1.0.
 */
static inline void init_matrix_random(double* mat, int n, unsigned int seed) {
    #pragma omp parallel
    {
        unsigned int thread_seed = seed + (unsigned int)omp_get_thread_num() * 1013;
        #pragma omp for schedule(static)
        for (int i = 0; i < n * n; i++) {
            mat[i] = (double)rand_r(&thread_seed) / (double)RAND_MAX;
        }
    }
}

/**
 * Zero out all elements of an N x N matrix.
 */
static inline void zero_matrix(double* mat, int n) {
    memset(mat, 0, (size_t)n * (size_t)n * sizeof(double));
}

/**
 * Verify whether two N x N matrices match within a tolerance threshold.
 */
static inline bool verify_matrix(const double* ref, const double* test, int n, double tol) {
    double max_diff = 0.0;
    int error_count = 0;
    
    for (int i = 0; i < n * n; i++) {
        double diff = fabs(ref[i] - test[i]);
        if (diff > max_diff) {
            max_diff = diff;
        }
        if (diff > tol) {
            error_count++;
            if (error_count <= 5) {
                int r = i / n;
                int c = i % n;
                fprintf(stderr, "Mismatch at [%d, %d]: Ref = %.8f, Test = %.8f (Diff = %.2e)\n",
                        r, c, ref[i], test[i], diff);
            }
        }
    }
    
    if (error_count > 0) {
        fprintf(stderr, "Verification FAILED: %d errors found. Max diff = %.2e (tolerance = %.2e)\n",
                error_count, max_diff, tol);
        return false;
    }
    
    printf("Verification PASSED: Outputs match within tolerance (Max diff = %.2e)\n", max_diff);
    return true;
}

/**
 * Calculate GFLOPS for standard N x N matrix multiplication (2 * N^3 operations).
 */
static inline double calculate_gflops(int n, double time_sec) {
    if (time_sec <= 0.0) return 0.0;
    double operations = 2.0 * (double)n * (double)n * (double)n;
    return (operations * 1e-9) / time_sec;
}

/**
 * Print a small portion of an N x N matrix.
 */
static inline void print_matrix_sample(const char* name, const double* mat, int n, int max_dim) {
    printf("Matrix %s (%dx%d):\n", name, n, n);
    int display_rows = (n < max_dim) ? n : max_dim;
    int display_cols = (n < max_dim) ? n : max_dim;
    for (int i = 0; i < display_rows; i++) {
        printf("  [ ");
        for (int j = 0; j < display_cols; j++) {
            printf("%8.4f ", mat[i * n + j]);
        }
        if (n > display_cols) printf("... ");
        printf("]\n");
    }
    if (n > display_rows) {
        printf("  [ ... ]\n");
    }
}

#endif // COMMON_H
