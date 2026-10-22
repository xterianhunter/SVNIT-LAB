#include <stdio.h>
#include <stdlib.h>

int main() {
    int n;
    printf("Enter size of vectors: ");
    if (scanf("%d", &n) != 1 || n <= 0) {
        printf("Invalid size\n");
        return 1;
    }

    int *a = (int *)malloc(n * sizeof(int));
    int *b = (int *)malloc(n * sizeof(int));

    if (a == NULL || b == NULL) {
        printf("Memory allocation failed\n");
        return 1;
    }

    printf("Enter elements of first vector:\n");
    for (int i = 0; i < n; i++) {
        scanf("%d", &a[i]);
    }

    printf("Enter elements of second vector:\n");
    for (int i = 0; i < n; i++) {
        scanf("%d", &b[i]);
    }

    long long dot_product = 0;
    for (int i = 0; i < n; i++) {
        dot_product += (long long)a[i] * b[i];
    }

    printf("Dot Product: %lld\n", dot_product);

    free(a);
    free(b);
    return 0;
}
