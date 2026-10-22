#include<stdio.h>
#include<omp.h>
#define ARR_SIZE 11
int main( int *arg, char *argv[] )
{
int j, tid ;
int a[ARR_SIZE] ;
#pragma omp parallel private( tid)
{
tid = omp_get_thread_num() ;
#pragma omp for ordered
for( j = 0 ; j < ARR_SIZE ; j++ )
{
a[j] = 1 ;
#pragma omp ordered
printf( "Thread %d, iteration %d\n", tid, j ) ;
}
}
return 0;
}
