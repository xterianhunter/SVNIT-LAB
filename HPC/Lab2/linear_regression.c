#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <omp.h>

#define DEFAULT_N       2000000   // 2 Million datapoints for large dataspace
#define DEFAULT_EPOCHS  100       // Number of Gradient Descent iterations
#define DEFAULT_ALPHA   0.1       // Learning rate

// Synthetic ground truth parameters: y = w0 + w1*x1 + w2*x2
#define TRUE_W0  2.0
#define TRUE_W1  3.5
#define TRUE_W2 -1.5

// 3D Data Generation (2D features X1, X2 and 1D label Y)
void generate_data(double *x1, double *x2, double *y, size_t n) {
    #pragma omp parallel for schedule(static)
    for (size_t i = 0; i < n; i++) {
        // Deterministic pseudo-random generation per sample for reproducibility
        unsigned int seed = (unsigned int)(i + 1337);
        double r1 = (double)rand_r(&seed) / (double)RAND_MAX;
        double r2 = (double)rand_r(&seed) / (double)RAND_MAX;
        double noise = ((double)rand_r(&seed) / (double)RAND_MAX - 0.5) * 0.05;

        x1[i] = r1;
        x2[i] = r2;
        y[i] = TRUE_W0 + TRUE_W1 * r1 + TRUE_W2 * r2 + noise;
    }
}

// Compute Mean Squared Error (MSE) Loss
double compute_loss(const double *x1, const double *x2, const double *y, size_t n,
                    double w0, double w1, double w2) {
    double total_loss = 0.0;
    #pragma omp parallel for reduction(+:total_loss) schedule(static)
    for (size_t i = 0; i < n; i++) {
        double pred = w0 + w1 * x1[i] + w2 * x2[i];
        double err = pred - y[i];
        total_loss += err * err;
    }
    return total_loss / (2.0 * (double)n);
}

// Sequential Batch Gradient Descent
void gradient_descent_seq(const double *x1, const double *x2, const double *y,
                          size_t n, int epochs, double alpha,
                          double *w0, double *w1, double *w2, double *time_taken) {
    *w0 = 0.0;
    *w1 = 0.0;
    *w2 = 0.0;

    double t_start = omp_get_wtime();

    for (int epoch = 0; epoch < epochs; epoch++) {
        double dw0 = 0.0;
        double dw1 = 0.0;
        double dw2 = 0.0;

        for (size_t i = 0; i < n; i++) {
            double err = (*w0 + *w1 * x1[i] + *w2 * x2[i]) - y[i];
            dw0 += err;
            dw1 += err * x1[i];
            dw2 += err * x2[i];
        }

        dw0 /= (double)n;
        dw1 /= (double)n;
        dw2 /= (double)n;

        *w0 -= alpha * dw0;
        *w1 -= alpha * dw1;
        *w2 -= alpha * dw2;
    }

    *time_taken = omp_get_wtime() - t_start;
}

// OpenMP Parallelized Batch Gradient Descent
void gradient_descent_omp(const double *x1, const double *x2, const double *y,
                          size_t n, int epochs, double alpha, int num_threads,
                          double *w0, double *w1, double *w2, double *time_taken) {
    *w0 = 0.0;
    *w1 = 0.0;
    *w2 = 0.0;

    double t_start = omp_get_wtime();

    for (int epoch = 0; epoch < epochs; epoch++) {
        double dw0 = 0.0;
        double dw1 = 0.0;
        double dw2 = 0.0;

        #pragma omp parallel for num_threads(num_threads) schedule(static) reduction(+:dw0, dw1, dw2)
        for (size_t i = 0; i < n; i++) {
            double err = (*w0 + *w1 * x1[i] + *w2 * x2[i]) - y[i];
            dw0 += err;
            dw1 += err * x1[i];
            dw2 += err * x2[i];
        }

        dw0 /= (double)n;
        dw1 /= (double)n;
        dw2 /= (double)n;

        *w0 -= alpha * dw0;
        *w1 -= alpha * dw1;
        *w2 -= alpha * dw2;
    }

    *time_taken = omp_get_wtime() - t_start;
}

int main(int argc, char *argv[]) {
    size_t n = (argc > 1) ? (size_t)atol(argv[1]) : DEFAULT_N;
    int epochs = (argc > 2) ? atoi(argv[2]) : DEFAULT_EPOCHS;
    double alpha = DEFAULT_ALPHA;

    printf("========================================================================\n");
    printf("         OpenMP Parallel Linear Regression (3D Dataspace: X1, X2 -> Y)   \n");
    printf("========================================================================\n");
    printf("Datapoints (N)  : %zu\n", n);
    printf("Epochs          : %d\n", epochs);
    printf("Learning Rate   : %.3f\n", alpha);
    printf("Ground Truth    : y = %.2f + %.2f*x1 + %.2f*x2\n", TRUE_W0, TRUE_W1, TRUE_W2);
    printf("Available Cores : %d\n", omp_get_max_threads());
    printf("------------------------------------------------------------------------\n");

    // Allocate contiguous arrays (Structure-of-Arrays)
    double *x1 = (double *)malloc(n * sizeof(double));
    double *x2 = (double *)malloc(n * sizeof(double));
    double *y  = (double *)malloc(n * sizeof(double));

    if (!x1 || !x2 || !y) {
        fprintf(stderr, "Error: Memory allocation failed for %zu samples.\n", n);
        free(x1); free(x2); free(y);
        return 1;
    }

    printf("Generating synthetic 3D dataset... ");
    fflush(stdout);
    generate_data(x1, x2, y, n);
    printf("Done.\n\n");

    // 1. Sequential Benchmark
    double seq_w0 = 0.0, seq_w1 = 0.0, seq_w2 = 0.0, seq_time = 0.0;
    printf("Running Sequential Gradient Descent... ");
    fflush(stdout);
    gradient_descent_seq(x1, x2, y, n, epochs, alpha, &seq_w0, &seq_w1, &seq_w2, &seq_time);
    double seq_loss = compute_loss(x1, x2, y, n, seq_w0, seq_w1, seq_w2);
    printf("Done in %.4f s\n\n", seq_time);

    // 2. OpenMP Parallel Benchmarks across thread configurations
    int thread_counts[] = {1, 2, 4, 8};
    int num_tests = sizeof(thread_counts) / sizeof(thread_counts[0]);

    printf("%-12s | %-10s | %-8s | %-10s | %-32s | %-10s\n",
           "Threads", "Time (s)", "Speedup", "Efficiency", "Converged Weights (w0, w1, w2)", "MSE Loss");
    printf("-------------------------------------------------------------------------------------------------------------\n");
    printf("%-12s | %10.4f | %8.2fx | %9.1f%% | (w0=%.3f, w1=%.3f, w2=%.3f)    | %10.6f\n",
           "Sequential", seq_time, 1.0, 100.0, seq_w0, seq_w1, seq_w2, seq_loss);

    for (int t = 0; t < num_tests; t++) {
        int threads = thread_counts[t];
        double par_w0 = 0.0, par_w1 = 0.0, par_w2 = 0.0, par_time = 0.0;

        gradient_descent_omp(x1, x2, y, n, epochs, alpha, threads,
                             &par_w0, &par_w1, &par_w2, &par_time);

        double par_loss = compute_loss(x1, x2, y, n, par_w0, par_w1, par_w2);
        double speedup = seq_time / par_time;
        double efficiency = (speedup / (double)threads) * 100.0;

        // Verify accuracy matches sequential within small floating-point tolerance
        double diff = fabs(par_w0 - seq_w0) + fabs(par_w1 - seq_w1) + fabs(par_w2 - seq_w2);
        char thread_label[16];
        snprintf(thread_label, sizeof(thread_label), "%d threads", threads);

        printf("%-12s | %10.4f | %8.2fx | %9.1f%% | (w0=%.3f, w1=%.3f, w2=%.3f)    | %10.6f\n",
               thread_label, par_time, speedup, efficiency, par_w0, par_w1, par_w2, par_loss);

        if (diff > 1e-4) {
            fprintf(stderr, "Warning: Result mismatch on %d threads (diff = %e)\n", threads, diff);
        }
    }

    printf("=============================================================================================================\n");

    // Clean up
    free(x1);
    free(x2);
    free(y);

    return 0;
}
