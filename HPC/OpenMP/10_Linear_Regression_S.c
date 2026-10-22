#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define N 100000        // Number of data points
#define ALPHA 0.01   // Learning rate
#define ITERATIONS 10000 // Number of gradient descent steps

// Function to generate synthetic data: y = 2x + 3 + noise
void generate_data(double *X, double *Y) {
    for (int i = 0; i < N; i++) {
        X[i] = (double)i / N;  
        Y[i] = 2 * X[i] + 3 ;
    }
}

// Function to perform Linear Regression using Gradient Descent
void linear_regression(double *X, double *Y, double *w, double *b) {
    for (int iter = 0; iter < ITERATIONS; iter++) {
        double dw = 0, db = 0;

        // Compute gradients
        for (int i = 0; i < N; i++) {
            double y_pred = (*w) * X[i] + (*b);
            double error = Y[i] - y_pred;
	    dw += (-2.0 * X[i] * error) / N;
	    db += (-2.0 * error) / N;
        }

        // Update parameters
        *w -= ALPHA * dw;
        *b -= ALPHA * db;
    }
}

void main() {

    // Allocate memory for large dataset
    double *X = (double *)malloc(N * sizeof(double));
    double *Y = (double *)malloc(N * sizeof(double));

    // Generate dataset
    generate_data(X, Y);

    // Initialize weights
    double w = 0.0, b = 0.0;

    // Start timing
    clock_t start = clock();

    // Perform Linear Regression
    linear_regression(X, Y, &w, &b);

    // End timing
    clock_t end = clock();
    double time_spent = (double)(end - start) / CLOCKS_PER_SEC;

    // Output results
    printf("Final values after training:\n");
    printf("w = %f, b = %f\n", w, b);
    printf("Execution Time: %f seconds\n", time_spent);

    // Free allocated memory
    free(X);
    free(Y);

}

