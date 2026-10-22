#include <stdio.h>
#include <stdlib.h>

// Define constants
#define N 5           // Number of data points
#define ALPHA 0.01    // Learning rate
#define ITERATIONS 10000  // Number of gradient descent steps

// Function to perform Linear Regression using Gradient Descent
void linear_regression(double X[], double Y[], double *w, double *b) {
    for (int iter = 0; iter < ITERATIONS; iter++) {
        double dw = 0, db = 0;

        // Compute gradients
        for (int i = 0; i < N; i++) {
            double y_pred = (*w) * X[i] + (*b);  // Predicted value
            double error = Y[i] - y_pred;
            dw += -2.0 * X[i] * error;
            db += -2.0 * error;
        }

        // Average gradients
        dw /= N;
        db /= N;

        // Update weights
        *w -= ALPHA * dw;
        *b -= ALPHA * db;
    }
}

void main() {
    // Sample dataset: (X, Y) pairs
    double X[N] = {1, 2, 3, 4, 5};
    double Y[N] = {2, 4, 6, 8, 10};  // y = 2x (perfect line)

    // Initialize parameters
    double w = 0.0, b = 0.0;

    // Perform Linear Regression
    linear_regression(X, Y, &w, &b);

    // Output final parameters
    printf("Final values after training:\n");
    printf("w = %f, b = %f\n", w, b);

}
