#!/bin/bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
BIN_DIR="${ROOT_DIR}/bin"
RESULTS_FILE="${ROOT_DIR}/benchmark_results.md"

echo "================================================================"
echo "    OpenMP Matrix Multiplication Automated Benchmark Suite      "
echo "================================================================"

# Ensure binaries are built
make -C "${ROOT_DIR}" all

SIZES=(500 1000 1500)
THREADS=(1 2 4 8)

cat << 'EOF' > "${RESULTS_FILE}"
# OpenMP Matrix Multiplication Performance Benchmark Results

## Environment & System Details
- **Compiler**: GCC with `-fopenmp -O3 -Wall -Wextra -std=c11`
- **Metric**: Wall-clock time (seconds), GFLOPS ($2N^3 / (t \times 10^9)$), Speedup ($S = T_{seq} / T_{par}$), Efficiency ($E = S / p \times 100\%$)

---

## Detailed Benchmark Results

EOF

for N in "${SIZES[@]}"; do
    echo ""
    echo "================================================================"
    echo " Benchmarking Matrix Size: ${N} x ${N}"
    echo "================================================================"

    MEM_MB=$(( 3 * N * N * 8 / 1024 / 1024 ))
    echo "### Matrix Dimension: ${N} x ${N} (${MEM_MB} MB Memory)" >> "${RESULTS_FILE}"
    echo "" >> "${RESULTS_FILE}"
    echo "| Threads (\$T\$) | Method | Time (s) | GFLOPS | Speedup | Efficiency |" >> "${RESULTS_FILE}"
    echo "|---------------|--------|----------|--------|---------|------------|" >> "${RESULTS_FILE}"

    # First get sequential baseline
    SEQ_OUTPUT=$("${BIN_DIR}/matrix_mult" "${N}" 1 seq)
    SEQ_TIME=$(echo "${SEQ_OUTPUT}" | grep "Sequential Time:" | awk '{print $3}')
    SEQ_GFLOPS=$(echo "${SEQ_OUTPUT}" | grep "Sequential Time:" | sed -E 's/.*\((.*) GFLOPS\)/\1/')

    echo "| 1 (Baseline) | Sequential | ${SEQ_TIME} s | ${SEQ_GFLOPS} | 1.00x | 100.0% |" >> "${RESULTS_FILE}"
    echo "Sequential baseline: ${SEQ_TIME} s (${SEQ_GFLOPS} GFLOPS)"

    for T in "${THREADS[@]}"; do
        echo "  Evaluating T=${T} threads..."

        # Coarse-grained
        COARSE_OUTPUT=$("${BIN_DIR}/matrix_mult" "${N}" "${T}" coarse)
        COARSE_TIME=$(echo "${COARSE_OUTPUT}" | grep "Coarse-Grained Time:" | awk '{print $3}')
        COARSE_GFLOPS=$(echo "${COARSE_OUTPUT}" | grep "Coarse-Grained Time:" | sed -E 's/.*\((.*) GFLOPS\)/\1/')
        COARSE_SPEEDUP=$(awk -v seq="${SEQ_TIME}" -v par="${COARSE_TIME}" 'BEGIN { if (par > 0) printf "%.2f", seq / par; else print "0.00" }')
        COARSE_EFF=$(awk -v sp="${COARSE_SPEEDUP}" -v th="${T}" 'BEGIN { if (th > 0) printf "%.1f", (sp / th) * 100; else print "0.0" }')

        # Fine-grained
        FINE_OUTPUT=$("${BIN_DIR}/matrix_mult" "${N}" "${T}" fine)
        FINE_TIME=$(echo "${FINE_OUTPUT}" | grep "Fine-Grained Time:" | awk '{print $3}')
        FINE_GFLOPS=$(echo "${FINE_OUTPUT}" | grep "Fine-Grained Time:" | sed -E 's/.*\((.*) GFLOPS\)/\1/')
        FINE_SPEEDUP=$(awk -v seq="${SEQ_TIME}" -v par="${FINE_TIME}" 'BEGIN { if (par > 0) printf "%.2f", seq / par; else print "0.00" }')
        FINE_EFF=$(awk -v sp="${FINE_SPEEDUP}" -v th="${T}" 'BEGIN { if (th > 0) printf "%.1f", (sp / th) * 100; else print "0.0" }')

        echo "    -> Coarse: ${COARSE_TIME}s (${COARSE_SPEEDUP}x) | Fine: ${FINE_TIME}s (${FINE_SPEEDUP}x)"
        echo "| ${T} | Coarse-Grained (Row) | ${COARSE_TIME} s | ${COARSE_GFLOPS} | ${COARSE_SPEEDUP}x | ${COARSE_EFF}% |" >> "${RESULTS_FILE}"
        echo "| ${T} | Fine-Grained (Element) | ${FINE_TIME} s | ${FINE_GFLOPS} | ${FINE_SPEEDUP}x | ${FINE_EFF}% |" >> "${RESULTS_FILE}"
    done

    echo "" >> "${RESULTS_FILE}"
done

cat << 'EOF' >> "${RESULTS_FILE}"
---

## Summary & Comparative Performance Analysis

### 1. Coarse-Grained Data Decomposition (Row-Level Partitioning)
- **Workload Distribution**: Each thread is assigned a contiguous slice of rows ($N/T$) of the output matrix $C$.
- **Overhead**: Thread creation and loop scheduling occur only once per matrix multiplication. Thread communication overhead during execution is virtually non-existent.
- **Cache Locality**: High data reuse. Row elements of matrix $A$ remain resident in L1/L2 cache while computing the dot product across matrix $B$.
- **Scaling Behavior**: Scales near-linearly with thread count, achieving maximum throughput and high parallel efficiency.

### 2. Fine-Grained Data Decomposition (Element-Level Dynamic Partitioning)
- **Workload Distribution**: Each individual cell $C[i][j]$ is scheduled dynamically as a standalone work unit (`schedule(dynamic, 1)`).
- **Overhead**: For an $N \times N$ matrix, the OpenMP runtime must manage and dispatch $N^2$ separate tasks (e.g., 1,000,000 tasks for $N=1000$), causing heavy thread synchronization and lock contention on runtime queues.
- **Cache Locality**: Poor spatial locality. Threads jump across memory addresses without reusing previously cached cache lines.
- **Scaling Behavior**: Significantly lower performance and lower parallel efficiency compared to coarse-grained decomposition.

### 3. Key Takeaway & Conclusion
For regular, dense, compute-intensive workloads like matrix multiplication, coarse-grained decomposition is vastly superior due to negligible synchronization overhead and optimal cache line utilization. Fine-grained decomposition introduces severe scheduling bottlenecks and should only be reserved for highly irregular, non-uniform workloads where dynamic load balancing is strictly necessary.
EOF

echo ""
echo "================================================================"
echo "Benchmarks completed successfully! Results written to:"
echo "${RESULTS_FILE}"
echo "================================================================"
