#include <stdio.h>
#include <stdlib.h>
#include <omp.h>

// Partition function using two pointers
int partition(int arr[], int low, int high) {
    int pivot = arr[low]; // Pivot is the first element
    int p = low + 1; // Pointer moving from left to right
    int q = high;    // Pointer moving from right to left

    while (p <= q) {
        // Find element greater than pivot from the left side
        while (p <= high && arr[p] <= pivot) {
            p++;
        }
        // Find element smaller than pivot from the right side
        while (q >= low && arr[q] > pivot) {
            q--;
        }
        // Swap elements if pointers have not crossed
        if (p < q) {
            int temp = arr[p];
            arr[p] = arr[q];
            arr[q] = temp;
        }
    }
    // Place the pivot at its correct position
    int temp = arr[low];
    arr[low] = arr[q];
    arr[q] = temp;

    return q; // Return the pivot index
}

// Sequential Quick Sort
void quick_sort(int arr[], int low, int high) {
    if (low < high) {
        int pi = partition(arr, low, high);

        // Recursively sort elements before and after partition
        quick_sort(arr, low, pi - 1);
        quick_sort(arr, pi + 1, high);
    }
}

// Parallel Quick Sort using OpenMP
void parallel_quick_sort(int arr[], int low, int high, int depth) {
    if (low < high) {
        int pi = partition(arr, low, high);

        if (depth > 0)
        {
            #pragma omp task
            parallel_quick_sort(arr, low, pi - 1, depth - 1);

            #pragma omp task
            parallel_quick_sort(arr, pi + 1, high, depth - 1);
        }

        if (depth <= 0) {
            quick_sort(arr, low, pi - 1);
            quick_sort(arr, pi + 1, high);
        }
    }
}

// Function to generate an array of random integers
void generate_array(int arr[], int size) {
    for (int i = 0; i < size; i++) {
        arr[i] = rand() % 1000;
    }
}

// Function to check if the array is sorted
int is_sorted(int arr[], int size) {
    for (int i = 1; i < size; i++) {
        if (arr[i] < arr[i - 1]) {
            return 0;
        }
    }
    return 1;
}

int main() {
    int N = 2000000; // Array size
    int *arr_seq = (int *)malloc(N * sizeof(int));
    int *arr_par = (int *)malloc(N * sizeof(int));

    generate_array(arr_seq, N);
    for (int i = 0; i < N; i++) {
        arr_par[i] = arr_seq[i];
    }

    // Sequential Quick Sort
    double start_time = omp_get_wtime();
    quick_sort(arr_seq, 0, N - 1);
    double seq_time = omp_get_wtime() - start_time;
    printf("Sequential Quick Sort Time: %f seconds\n", seq_time);

    // Parallel Quick Sort
    start_time = omp_get_wtime();
    #pragma omp parallel
    {
        #pragma omp single
        parallel_quick_sort(arr_par, 0, N - 1, 4); // Depth 4 for parallel recursion
    }
    double par_time = omp_get_wtime() - start_time;
    printf("Parallel Quick Sort Time: %f seconds\n", par_time);

    // Verify correctness
    if (is_sorted(arr_seq, N) && is_sorted(arr_par, N)) {
        printf("Both arrays are sorted correctly!\n");
    } else {
        printf("Error in sorting!\n");
    }

    free(arr_seq);
    free(arr_par);

    return 0;
}

