#include <stdio.h>
#include <stdlib.h>
#include <omp.h>

#define N 10000000    // 10 million datapoints (3D dataspace: x1, x2, y)
#define EPOCHS 20
#define LR 0.01

// Sequential Gradient Descent
void linear_regression_seq(double *x1, double *x2, double *y, int n, int epochs, double lr, double *w1_out, double *w2_out, double *b_out) {
    double w1 = 0.0, w2 = 0.0, b = 0.0;
    for (int epoch = 0; epoch < epochs; epoch++) {
        double dw1 = 0.0, dw2 = 0.0, db = 0.0;
        for (int i = 0; i < n; i++) {
            double pred = w1 * x1[i] + w2 * x2[i] + b;
            double diff = pred - y[i];
            dw1 += diff * x1[i];
            dw2 += diff * x2[i];
            db += diff;
        }
        w1 -= (lr / n) * dw1;
        w2 -= (lr / n) * dw2;
        b  -= (lr / n) * db;
    }
    *w1_out = w1; *w2_out = w2; *b_out = b;
}

// Parallel Gradient Descent using OpenMP
void linear_regression_omp(double *x1, double *x2, double *y, int n, int epochs, double lr, double *w1_out, double *w2_out, double *b_out) {
    double w1 = 0.0, w2 = 0.0, b = 0.0;
    for (int epoch = 0; epoch < epochs; epoch++) {
        double dw1 = 0.0, dw2 = 0.0, db = 0.0;
        #pragma omp parallel for reduction(+:dw1, dw2, db) schedule(static)
        for (int i = 0; i < n; i++) {
            double pred = w1 * x1[i] + w2 * x2[i] + b;
            double diff = pred - y[i];
            dw1 += diff * x1[i];
            dw2 += diff * x2[i];
            db += diff;
        }
        w1 -= (lr / n) * dw1;
        w2 -= (lr / n) * dw2;
        b  -= (lr / n) * db;
    }
    *w1_out = w1; *w2_out = w2; *b_out = b;
}

int main() {
    printf("=== Linear Regression with OpenMP ===\n");
    printf("Datapoints (N): %d | Epochs: %d | Learning Rate: %.2f\n", N, EPOCHS, LR);

    // Allocate 3-dimensional dataspace: (x1, x2) features and y label
    double *x1 = (double *)malloc(N * sizeof(double));
    double *x2 = (double *)malloc(N * sizeof(double));
    double *y  = (double *)malloc(N * sizeof(double));

    if (!x1 || !x2 || !y) {
        fprintf(stderr, "Memory allocation failed!\n");
        return 1;
    }

    // Generate synthetic data (True weights: w1=2.0, w2=3.0, b=1.0)
    #pragma omp parallel for schedule(static)
    for (int i = 0; i < N; i++) {
        x1[i] = (double)(i % 100) / 100.0;
        x2[i] = (double)((i * 3) % 100) / 100.0;
        y[i]  = 2.0 * x1[i] + 3.0 * x2[i] + 1.0;
    }

    double w1_seq = 0, w2_seq = 0, b_seq = 0;
    double w1_par = 0, w2_par = 0, b_par = 0;

    // 1. Sequential Run
    double t_seq_start = omp_get_wtime();
    linear_regression_seq(x1, x2, y, N, EPOCHS, LR, &w1_seq, &w2_seq, &b_seq);
    double t_seq = omp_get_wtime() - t_seq_start;

    // 2. Parallel Run
    double t_par_start = omp_get_wtime();
    linear_regression_omp(x1, x2, y, N, EPOCHS, LR, &w1_par, &w2_par, &b_par);
    double t_par = omp_get_wtime() - t_par_start;

    // Results & Performance Comparison
    printf("\n--- Sequential Performance ---\n");
    printf("Time: %.4f seconds\n", t_seq);
    printf("Learned Parameters: w1 = %.4f, w2 = %.4f, b = %.4f\n", w1_seq, w2_seq, b_seq);

    printf("\n--- OpenMP Parallel Performance (%d threads) ---\n", omp_get_max_threads());
    printf("Time: %.4f seconds\n", t_par);
    printf("Learned Parameters: w1 = %.4f, w2 = %.4f, b = %.4f\n", w1_par, w2_par, b_par);

    printf("\n--- Summary ---\n");
    printf("Speedup: %.2fx\n", t_seq / t_par);

    free(x1);
    free(x2);
    free(y);
    return 0;
}
