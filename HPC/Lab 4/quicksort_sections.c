#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <omp.h>

#define N 100000
#define DEPTH 4

void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

int partition(int arr[], int low, int high) {
    int pivot = arr[high];
    int i = low - 1;
    for (int j = low; j < high; j++) {
        if (arr[j] <= pivot) {
            i++;
            swap(&arr[i], &arr[j]);
        }
    }
    swap(&arr[i + 1], &arr[high]);
    return i + 1;
}

void quicksort_sequential(int arr[], int low, int high) {
    if (low < high) {
        int pi = partition(arr, low, high);
        quicksort_sequential(arr, low, pi - 1);
        quicksort_sequential(arr, pi + 1, high);
    }
}

void quicksort_parallel(int arr[], int low, int high, int depth) {
    if (low < high) {
        int pi = partition(arr, low, high);

        if (depth > 0) {
            #pragma omp parallel sections
            {
                #pragma omp section
                {
                    quicksort_parallel(arr, low, pi - 1, depth - 1);
                }
                #pragma omp section
                {
                    quicksort_parallel(arr, pi + 1, high, depth - 1);
                }
            }
        } else {
            quicksort_sequential(arr, low, pi - 1);
            quicksort_sequential(arr, pi + 1, high);
        }
    }
}

int main() {
    int *arr1 = (int *)malloc(N * sizeof(int));
    int *arr2 = (int *)malloc(N * sizeof(int));

    srand(42);
    for (int i = 0; i < N; i++)
        arr1[i] = rand() % N;

    memcpy(arr2, arr1, N * sizeof(int));

    // Sequential QuickSort
    double start = omp_get_wtime();
    quicksort_sequential(arr1, 0, N - 1);
    double end = omp_get_wtime();
    printf("Sequential QuickSort Time: %f seconds\n", end - start);

    // Parallel QuickSort (sections with depth limit)
    start = omp_get_wtime();
    quicksort_parallel(arr2, 0, N - 1, DEPTH);
    end = omp_get_wtime();
    printf("Parallel   QuickSort Time: %f seconds\n", end - start);

    free(arr1);
    free(arr2);
    return 0;
}
