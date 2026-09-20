#include <stdio.h>
#include <stdlib.h>
#include <omp.h>

#define SIZE 1000000
#define MAX_DEPTH 3

void merge(int a[], int l, int m, int r)
{
    int *temp = malloc((r - l + 1) * sizeof(int));

    int i = l, j = m + 1, k = 0;

    while (i <= m && j <= r)
        temp[k++] = (a[i] < a[j]) ? a[i++] : a[j++];

    while (i <= m)
        temp[k++] = a[i++];

    while (j <= r)
        temp[k++] = a[j++];

    for (i = l, k = 0; i <= r; i++, k++)
        a[i] = temp[k];

    free(temp);
}

/* Sequential Merge Sort */
void mergeSort(int a[], int l, int r)
{
    if (l >= r)
        return;

    int m = (l + r) / 2;

    mergeSort(a, l, m);
    mergeSort(a, m + 1, r);

    merge(a, l, m, r);
}

/* Parallel Merge Sort using sections and depth */
void parallelMergeSort(int a[], int l, int r, int depth)
{
    if (l >= r)
        return;

    /* Stop creating parallel sections after MAX_DEPTH */
    if (depth >= MAX_DEPTH)
    {
        mergeSort(a, l, r);
        return;
    }

    int m = (l + r) / 2;

    #pragma omp parallel sections
    {
        #pragma omp section
        {
            parallelMergeSort(a, l, m, depth + 1);
        }

        #pragma omp section
        {
            parallelMergeSort(a, m + 1, r, depth + 1);
        }
    }

    merge(a, l, m, r);
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

    /* Sequential */
    start = omp_get_wtime();

    mergeSort(a, 0, n - 1);

    end = omp_get_wtime();

    double sequential_time = end - start;

    /* Parallel */
    start = omp_get_wtime();

    parallelMergeSort(b, 0, n - 1, 0);

    end = omp_get_wtime();

    double parallel_time = end - start;

    printf("Number of elements : %d\n", n);
    printf("Threads            : %d\n", omp_get_max_threads());
    printf("Maximum depth      : %d\n", MAX_DEPTH);
    printf("Sequential Time    : %.6f seconds\n", sequential_time);
    printf("Parallel Time      : %.6f seconds\n", parallel_time);
    printf("Speedup            : %.2fx\n",
           sequential_time / parallel_time);

    free(a);
    free(b);

    return 0;
}