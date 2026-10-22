#include <omp.h>
#include <stdio.h>
void main()
{
#pragma omp parallel
{

/* Get the total number of OMP threads */
int numt = omp_get_num_threads() ;

/* Get the thread id of this thread */
int tid = omp_get_thread_num() ;

/* Print "Hello World" along with thread id and number of threads */
printf( "Hello World from thread %d of %d.\n", tid, numt ) ;

}
}
