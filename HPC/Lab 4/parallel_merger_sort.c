#include<stdio.h>
#include<omp.h>
#include<stdlib.h>

#define size 1000000
#define MAX_DEPTH 4

void merge(int a[], int l, int m, int r)
{
	int *temp = malloc((r - l + 1) * sizeof(int));
	int i = l, j = m+1, k = 0;

	while(i <= m && j <=r)
		temp[k++] = (a[i] < a[j]) ? a[i++] : a[j++];

	while(i <= m)
		temp[k++] = a[i++];

	while(j <= r)
		temp[k++] = a[j++];
	for(i=l, k=0; i<=r; i++, k++)
		a[i] = temp[k];
    free(temp);
}


void mergeSortSequential(int a[], int l, int r)
{
	if(l >= r)
		return;
	int m = (l + r)/ 2;

	mergeSortSequential(a, l, m);
	mergeSortSequential(a, m+1, r);

	merge(a, l, m, r);
}

void mergeSortParallel(int a[], int l, int r, int depth)
{
    if (l>=r)
        return;

    if (depth < 0)
    {
        mergeSortSequential(a, l, r);
        return;
    }
    
	int m = (l+r)/2; 
	#pragma omp parallel sections 
	{
		#pragma omp section
		mergeSortParallel(a, l, m, depth - 1);

		#pragma omp section
		mergeSortParallel(a, m+1, r, depth - 1);
	}
	merge(a, l, m, r);
}

int main(){
	int n = size;
	
	int *a = malloc(n* sizeof(int));
	int *b = malloc(n*sizeof(int));

	for(int i=0; i<n; i++)
    {
		a[i] = rand();
        b[i] = a[i];
    }
    
	double start, end;

	start = omp_get_wtime();
	mergeSortSequential(a, 0, n-1);
	end = omp_get_wtime();

	double sequential_time = end - start;
	
	start = omp_get_wtime();

	mergeSortParallel(b,0,n-1, 4);
	end = omp_get_wtime();

	double parallel_time = end - start;

	printf("Number of elements: %d\n", n);
    printf("Number of threads: %d\n", omp_get_max_threads());
	printf("Sequential time: %f seconds\n", sequential_time);
	printf("parallel time: %f seconds\n", parallel_time);
    
    printf("Speed up : %f\n", sequential_time / parallel_time);

    printf("Efficiency : %f\n", (sequential_time / parallel_time) / omp_get_max_threads());

    free(a);
    free(b);

    return 0;
}



