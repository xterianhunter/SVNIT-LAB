#include <stdio.h>
#include <stdlib.h>

int main() {
    int r1, c1, r2, c2;

    printf("Enter rows and columns of Matrix A: ");
    if (scanf("%d %d", &r1, &c1) != 2 || r1 <= 0 || c1 <= 0) {
        printf("Invalid dimensions\n");
        return 1;
    }

    printf("Enter rows and columns of Matrix B: ");
    if (scanf("%d %d", &r2, &c2) != 2 || r2 <= 0 || c2 <= 0) {
        printf("Invalid dimensions\n");
        return 1;
    }

    if (c1 != r2) {
        printf("Multiplication not possible: columns of A must equal rows of B\n");
        return 1;
    }

    // Allocate Matrix A
    int **A = (int **)malloc(r1 * sizeof(int *));
    for (int i = 0; i < r1; i++) {
        A[i] = (int *)malloc(c1 * sizeof(int));
    }

    // Allocate Matrix B
    int **B = (int **)malloc(r2 * sizeof(int *));
    for (int i = 0; i < r2; i++) {
        B[i] = (int *)malloc(c2 * sizeof(int));
    }

    // Allocate Result Matrix C
    int **C = (int **)malloc(r1 * sizeof(int *));
    for (int i = 0; i < r1; i++) {
        C[i] = (int *)malloc(c2 * sizeof(int));
    }

    printf("Enter elements of Matrix A:\n");
    for (int i = 0; i < r1; i++) {
        for (int j = 0; j < c1; j++) {
            scanf("%d", &A[i][j]);
        }
    }

    printf("Enter elements of Matrix B:\n");
    for (int i = 0; i < r2; i++) {
        for (int j = 0; j < c2; j++) {
            scanf("%d", &B[i][j]);
        }
    }

    // Multiply matrices
    for (int i = 0; i < r1; i++) {
        for (int j = 0; j < c2; j++) {
            C[i][j] = 0;
            for (int k = 0; k < c1; k++) {
                C[i][j] += A[i][k] * B[k][j];
            }
        }
    }

    printf("Resultant Matrix:\n");
    for (int i = 0; i < r1; i++) {
        for (int j = 0; j < c2; j++) {
            printf("%d ", C[i][j]);
        }
        printf("\n");
    }

    // Free memory
    for (int i = 0; i < r1; i++) free(A[i]);
    free(A);

    for (int i = 0; i < r2; i++) free(B[i]);
    free(B);

    for (int i = 0; i < r1; i++) free(C[i]);
    free(C);

    return 0;
}
