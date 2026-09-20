#include <stdio.h>
#include <stdlib.h>
#include <omp.h>

#define SIZE 10000
#define DEPTH 8

void swap(int *a, int *b)
{
    int temp = *a;
    *a = *b;
    *b = temp;
}

int partition(int a[], int low, int high)
{
    int pivot = a[high];
    int i = low - 1;

    for (int j = low; j < high; j++)
    {
        if (a[j] < pivot)
        {
            i++;
            swap(&a[i], &a[j]);
        }
    }

    swap(&a[i + 1], &a[high]);

    return i + 1;
}

/* Insertion Sort */
void insertionSort(int a[], int low, int high)
{
    for (int i = low + 1; i <= high; i++)
    {
        int key = a[i];
        int j = i - 1;

        while (j >= low && a[j] > key)
        {
            a[j + 1] = a[j];
            j--;
        }

        a[j + 1] = key;
    }
}

/* Sequential Quick Sort */
void quickSort(int a[], int low, int high)
{
    if (low >= high)
        return;

    int p = partition(a, low, high);

    quickSort(a, low, p - 1);
    quickSort(a, p + 1, high);
}

/* Parallel Quick Sort with depth */
void parallelQuickSort(int a[], int low, int high, int depth)
{
    if (low >= high)
        return;

    /* When depth becomes zero, use insertion sort */
    if (depth == 0)
    {
        insertionSort(a, low, high);
        return;
    }

    int p = partition(a, low, high);

    #pragma omp task
    parallelQuickSort(a, low, p - 1, depth - 1);

    #pragma omp task
    parallelQuickSort(a, p + 1, high, depth - 1);

    #pragma omp taskwait
}

int main()
{
    int n = SIZE;

    int *a = malloc(n * sizeof(int));
    int *b = malloc(n * sizeof(int));

    /* Same input for both */
    for (int i = 0; i < n; i++)
    {
        a[i] = rand();
        b[i] = a[i];
    }

    double start, end;

    /* Sequential Quick Sort */
    start = omp_get_wtime();

    quickSort(a, 0, n - 1);

    end = omp_get_wtime();

    double sequential_time = end - start;

    /* Parallel Quick Sort */
    start = omp_get_wtime();

    #pragma omp parallel
    {
        #pragma omp single
        {
            parallelQuickSort(b, 0, n - 1, DEPTH);
        }
    }

    end = omp_get_wtime();

    double parallel_time = end - start;

    printf("Number of elements : %d\n", n);
    printf("Threads            : %d\n", omp_get_max_threads());
    printf("Initial depth      : %d\n", DEPTH);
    printf("Sequential Time    : %.6f seconds\n", sequential_time);
    printf("Parallel Time      : %.6f seconds\n", parallel_time);
    printf("Speedup            : %.2fx\n",
           sequential_time / parallel_time);

    free(a);
    free(b);

    return 0;
}