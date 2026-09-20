/**
 * High Performance Computing Lab 5b: Parallel Sorting with OpenMP
 * 
 * Algorithms Implemented:
 * 1. Sequential Merge Sort
 * 2. Parallel Merge Sort using OpenMP Sections (#pragma omp section)
 * 3. Sequential Quick Sort
 * 4. Parallel Quick Sort using OpenMP Tasks (#pragma omp task)
 * 5. Parallel Quick Sort with Depth Cutoff (Depth 4 and 8) + Insertion Sort
 * 6. Parallel Quick Sort with Depth 8 + Sequential QS & Insertion Cutoff (<= 32)
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <omp.h>

#define MAX_SECTION_DEPTH 3
#define INSERTION_THRESHOLD 32

/* ========================================================================= */
/* Utility Functions                                                         */
/* ========================================================================= */

static inline void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

bool is_sorted(const int *arr, int n) {
    for (int i = 0; i < n - 1; i++) {
        if (arr[i] > arr[i + 1]) {
            return false;
        }
    }
    return true;
}

void generate_random_array(int *arr, int n, unsigned int seed) {
    srand(seed);
    for (int i = 0; i < n; i++) {
        arr[i] = rand() % 1000000;
    }
}

void copy_array(const int *src, int *dst, int n) {
    memcpy(dst, src, (size_t)n * sizeof(int));
}

/* ========================================================================= */
/* 1. Sequential & Parallel Merge Sort (OpenMP Sections)                     */
/* ========================================================================= */

void merge(int *arr, int l, int m, int r, int *temp) {
    int i = l, j = m + 1, k = l;
    while (i <= m && j <= r) {
        if (arr[i] <= arr[j]) {
            temp[k++] = arr[i++];
        } else {
            temp[k++] = arr[j++];
        }
    }
    while (i <= m) temp[k++] = arr[i++];
    while (j <= r) temp[k++] = arr[j++];
    for (i = l; i <= r; i++) {
        arr[i] = temp[i];
    }
}

void merge_sort_seq_internal(int *arr, int l, int r, int *temp) {
    if (l < r) {
        int m = l + (r - l) / 2;
        merge_sort_seq_internal(arr, l, m, temp);
        merge_sort_seq_internal(arr, m + 1, r, temp);
        merge(arr, l, m, r, temp);
    }
}

void merge_sort_seq(int *arr, int n) {
    int *temp = (int *)malloc((size_t)n * sizeof(int));
    if (!temp) {
        fprintf(stderr, "Memory allocation error in merge_sort_seq\n");
        return;
    }
    merge_sort_seq_internal(arr, 0, n - 1, temp);
    free(temp);
}

void merge_sort_sections_internal(int *arr, int l, int r, int *temp, int depth) {
    if (l < r) {
        int m = l + (r - l) / 2;
        if (depth < MAX_SECTION_DEPTH && (r - l) > 1000) {
            #pragma omp parallel sections
            {
                #pragma omp section
                merge_sort_sections_internal(arr, l, m, temp, depth + 1);

                #pragma omp section
                merge_sort_sections_internal(arr, m + 1, r, temp, depth + 1);
            }
        } else {
            merge_sort_seq_internal(arr, l, m, temp);
            merge_sort_seq_internal(arr, m + 1, r, temp);
        }
        merge(arr, l, m, r, temp);
    }
}

void merge_sort_parallel_sections(int *arr, int n) {
    int *temp = (int *)malloc((size_t)n * sizeof(int));
    if (!temp) {
        fprintf(stderr, "Memory allocation error in merge_sort_parallel_sections\n");
        return;
    }
    omp_set_max_active_levels(MAX_SECTION_DEPTH + 1);
    merge_sort_sections_internal(arr, 0, n - 1, temp, 0);
    free(temp);
}

/* ========================================================================= */
/* 2. Sequential & Parallel Quick Sort (OpenMP Tasks)                        */
/* ========================================================================= */

int partition(int *arr, int low, int high) {
    int mid = low + (high - low) / 2;
    swap(&arr[mid], &arr[high]);
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

void quick_sort_seq_internal(int *arr, int low, int high) {
    if (low < high) {
        int p = partition(arr, low, high);
        quick_sort_seq_internal(arr, low, p - 1);
        quick_sort_seq_internal(arr, p + 1, high);
    }
}

void quick_sort_seq(int *arr, int n) {
    quick_sort_seq_internal(arr, 0, n - 1);
}

void quick_sort_tasks_internal(int *arr, int low, int high) {
    if (low < high) {
        int p = partition(arr, low, high);
        if ((high - low) > 1000) {
            #pragma omp task
            quick_sort_tasks_internal(arr, low, p - 1);

            #pragma omp task
            quick_sort_tasks_internal(arr, p + 1, high);

            #pragma omp taskwait
        } else {
            quick_sort_seq_internal(arr, low, p - 1);
            quick_sort_seq_internal(arr, p + 1, high);
        }
    }
}

void quick_sort_parallel_tasks(int *arr, int n) {
    #pragma omp parallel
    {
        #pragma omp single nowait
        {
            quick_sort_tasks_internal(arr, 0, n - 1);
        }
    }
}

/* ========================================================================= */
/* 3. Insertion Sort & Hybrid Quick Sort Variations                          */
/* ========================================================================= */

void insertion_sort(int *arr, int low, int high) {
    for (int i = low + 1; i <= high; i++) {
        int key = arr[i];
        int j = i - 1;
        while (j >= low && arr[j] > key) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = key;
    }
}

/* Variant A: Direct fallback to Insertion Sort once depth >= max_depth */
void quick_sort_hybrid_direct_internal(int *arr, int low, int high, int depth, int max_depth) {
    if (low >= high) return;

    if (depth >= max_depth || (high - low + 1) <= INSERTION_THRESHOLD) {
        insertion_sort(arr, low, high);
        return;
    }

    int p = partition(arr, low, high);

    #pragma omp task
    quick_sort_hybrid_direct_internal(arr, low, p - 1, depth + 1, max_depth);

    #pragma omp task
    quick_sort_hybrid_direct_internal(arr, p + 1, high, depth + 1, max_depth);

    #pragma omp taskwait
}

void quick_sort_hybrid_direct(int *arr, int n, int max_depth) {
    #pragma omp parallel
    {
        #pragma omp single nowait
        {
            quick_sort_hybrid_direct_internal(arr, 0, n - 1, 0, max_depth);
        }
    }
}

/* Variant B: Sequential Quick Sort with Insertion Sort cutoff (<= 32) after depth */
void quick_sort_hybrid_opt_internal(int *arr, int low, int high, int depth, int max_depth) {
    if (low >= high) return;

    if ((high - low + 1) <= INSERTION_THRESHOLD) {
        insertion_sort(arr, low, high);
        return;
    }

    int p = partition(arr, low, high);

    if (depth < max_depth) {
        #pragma omp task
        quick_sort_hybrid_opt_internal(arr, low, p - 1, depth + 1, max_depth);

        #pragma omp task
        quick_sort_hybrid_opt_internal(arr, p + 1, high, depth + 1, max_depth);

        #pragma omp taskwait
    } else {
        quick_sort_hybrid_opt_internal(arr, low, p - 1, depth + 1, max_depth);
        quick_sort_hybrid_opt_internal(arr, p + 1, high, depth + 1, max_depth);
    }
}

void quick_sort_hybrid_opt(int *arr, int n, int max_depth) {
    #pragma omp parallel
    {
        #pragma omp single nowait
        {
            quick_sort_hybrid_opt_internal(arr, 0, n - 1, 0, max_depth);
        }
    }
}

/* ========================================================================= */
/* Benchmark & Performance Reporting                                         */
/* ========================================================================= */

typedef struct {
    const char *name;
    double time_taken;
    double speedup;
    bool correct;
} BenchmarkResult;

void run_benchmarks(int n) {
    printf("\n================================================================================================\n");
    printf(" BENCHMARKING WITH ARRAY SIZE N = %d (THREADS = %d)\n", n, omp_get_max_threads());
    printf("================================================================================================\n");

    int *master = (int *)malloc((size_t)n * sizeof(int));
    int *work   = (int *)malloc((size_t)n * sizeof(int));

    if (!master || !work) {
        fprintf(stderr, "Failed to allocate memory for %d elements.\n", n);
        if (master) free(master);
        if (work) free(work);
        return;
    }

    generate_random_array(master, n, 42);

    BenchmarkResult results[7];
    double t_start, t_end;

    /* 1. Sequential Merge Sort */
    copy_array(master, work, n);
    t_start = omp_get_wtime();
    merge_sort_seq(work, n);
    t_end = omp_get_wtime();
    results[0] = (BenchmarkResult){
        "1. Sequential Merge Sort",
        t_end - t_start,
        1.00,
        is_sorted(work, n)
    };

    /* 2. Parallel Merge Sort (OpenMP Sections) */
    copy_array(master, work, n);
    t_start = omp_get_wtime();
    merge_sort_parallel_sections(work, n);
    t_end = omp_get_wtime();
    results[1] = (BenchmarkResult){
        "2. Parallel Merge Sort (Sections)",
        t_end - t_start,
        results[0].time_taken / (t_end - t_start),
        is_sorted(work, n)
    };

    /* 3. Sequential Quick Sort */
    copy_array(master, work, n);
    t_start = omp_get_wtime();
    quick_sort_seq(work, n);
    t_end = omp_get_wtime();
    results[2] = (BenchmarkResult){
        "3. Sequential Quick Sort",
        t_end - t_start,
        1.00,
        is_sorted(work, n)
    };

    /* 4. Parallel Quick Sort (OpenMP Tasks) */
    copy_array(master, work, n);
    t_start = omp_get_wtime();
    quick_sort_parallel_tasks(work, n);
    t_end = omp_get_wtime();
    results[3] = (BenchmarkResult){
        "4. Parallel Quick Sort (Tasks)",
        t_end - t_start,
        results[2].time_taken / (t_end - t_start),
        is_sorted(work, n)
    };

    /* 5. Parallel Quick Sort (Depth 4 + Direct Insertion) */
    copy_array(master, work, n);
    t_start = omp_get_wtime();
    quick_sort_hybrid_direct(work, n, 4);
    t_end = omp_get_wtime();
    results[4] = (BenchmarkResult){
        "5. Parallel Quick Sort (Depth 4 + Direct Insert)",
        t_end - t_start,
        results[2].time_taken / (t_end - t_start),
        is_sorted(work, n)
    };

    /* 6. Parallel Quick Sort (Depth 8 + Direct Insertion) */
    copy_array(master, work, n);
    t_start = omp_get_wtime();
    quick_sort_hybrid_direct(work, n, 8);
    t_end = omp_get_wtime();
    results[5] = (BenchmarkResult){
        "6. Parallel Quick Sort (Depth 8 + Direct Insert)",
        t_end - t_start,
        results[2].time_taken / (t_end - t_start),
        is_sorted(work, n)
    };

    /* 7. Parallel Quick Sort (Depth 8 + Seq QS & Insertion Cutoff) */
    copy_array(master, work, n);
    t_start = omp_get_wtime();
    quick_sort_hybrid_opt(work, n, 8);
    t_end = omp_get_wtime();
    results[6] = (BenchmarkResult){
        "7. Parallel Quick Sort (Depth 8 + Hybrid Cutoff)",
        t_end - t_start,
        results[2].time_taken / (t_end - t_start),
        is_sorted(work, n)
    };

    /* Print Comparison Table */
    printf("%-50s | %-12s | %-10s | %-8s\n", "Algorithm", "Time (sec)", "Speedup", "Status");
    printf("---------------------------------------------------+--------------+------------+----------\n");
    for (int i = 0; i < 7; i++) {
        printf("%-50s | %10.6f s | %8.2fx  | %s\n",
               results[i].name,
               results[i].time_taken,
               results[i].speedup,
               results[i].correct ? "PASS" : "FAIL");
    }
    printf("---------------------------------------------------+--------------+------------+----------\n");

    free(master);
    free(work);
}

int main(int argc, char *argv[]) {
    printf("================================================================================================\n");
    printf(" OpenMP Parallel Sorting Benchmark (HPC Lab 5b)\n");
    printf(" Available Cores/Threads: %d\n", omp_get_max_threads());
    printf("================================================================================================\n");

    int test_sizes[] = {100000, 250000, 500000};
    int num_tests = sizeof(test_sizes) / sizeof(test_sizes[0]);

    if (argc > 1) {
        int custom_n = atoi(argv[1]);
        if (custom_n > 0) {
            run_benchmarks(custom_n);
            return 0;
        }
    }

    for (int i = 0; i < num_tests; i++) {
        run_benchmarks(test_sizes[i]);
    }

    return 0;
}
