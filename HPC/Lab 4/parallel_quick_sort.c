#include <stdio.h>
#include <stdlib.h>
#include <omp.h>

#define SIZE 1000000

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
    swap(&a[i+1],&a[high]);
    return i+1;

}

void sequentialQuickSort(int a[], int low, int high)
{
    if (low >= high)
        return;
    int p = partition(a, low, high);

    sequentialQuickSort(a, low, p-1);
    sequentialQuickSort(a, p+1, high);
}

void parallelQuickSort(int a[], int low, int high)
{
    if (low >= high)
        return;

    int p = partition(a, low, high);

    #pragma omp task
    parallelQuickSort(a, low, p-1);

    #pragma omp task
    parallelQuickSort(a, p+1, high);

    #pragma omp taskwait
}

int main()
{
    int n = SIZE;
    
    int *a = malloc(n*sizeof(int));
    int *b = malloc(n*sizeof(int));

    for (int i = 0; i<n; i++)
    {
        a[i] = rand();
        b[i] = a[i];
    }
    
    double start, end;

    start = omp_get_wtime();
    sequentialQuickSort(a, 0, n-1);
    end = omp_get_wtime();

    double sequentialTime = end - start;

    start = omp_get_wtime();
    #pragma omp parallel
    {
        #pragma omp single
        parallelQuickSort(b, 0, n-1);
    }
    end = omp_get_wtime();
    double parallelTime = end - start;

    printf("Number of elements : %d\n", n);
    printf("Threads  : %d\n", omp_get_max_threads());
    printf("sequentialTime : %.6f sec\n", sequentialTime);
    printf("parallelTime  : %.6f sec\n", parallelTime);
    printf("speedup    : %.2fx\n", sequentialTime / parallelTime);

    free(a);
    free(b);
    return 0;
}





