"""Benchmarking suite for Linear Search and Binary Search algorithms.
"""

from dataclasses import asdict, dataclass
from pathlib import Path
import time
from typing import Callable, Dict, List, Sequence, Tuple

from src.searching import binary_search, linear_search


@dataclass
class BenchmarkResult:
    algorithm: str
    input_size: int
    case_name: str
    target_value: int
    found_index: int
    comparisons: int
    time_ns: float
    time_us: float


def get_test_targets(arr: Sequence[int]) -> Dict[str, int]:
    """Extract representative search target values for 4 standard cases:
    - Beginning (first element)
    - Middle (median element)
    - End (last element)
    - Absent (value not in the array)
    """
    n = len(arr)
    if n == 0:
        raise ValueError("Cannot extract targets from an empty array")

    return {
        "Beginning": arr[0],
        "Middle": arr[n // 2],
        "End": arr[-1],
        "Absent": max(arr) + 1000,
    }


def measure_search_performance(
    algo_fn: Callable[[Sequence[int], int], Tuple[int, int]],
    arr: Sequence[int],
    target: int,
    iterations: int = 10000,
    warmup: int = 500,
) -> Tuple[int, int, float]:
    """Measure single search execution with warmup and high-resolution timing.

    Returns:
        (found_index, comparisons, average_time_in_nanoseconds)
    """
    # Verify correctness and record index/comparisons
    found_idx, comparisons = algo_fn(arr, target)

    # Warmup cycles
    for _ in range(warmup):
        algo_fn(arr, target)

    # High-precision benchmark
    start_ns = time.perf_counter_ns()
    for _ in range(iterations):
        algo_fn(arr, target)
    end_ns = time.perf_counter_ns()

    avg_time_ns = (end_ns - start_ns) / iterations
    return found_idx, comparisons, avg_time_ns


def run_benchmarks(
    datasets: Dict[int, List[int]],
    iterations: int = 10000,
) -> List[BenchmarkResult]:
    """Run full benchmarking suite over all datasets and algorithms."""
    results: List[BenchmarkResult] = []
    algorithms = [
        ("Linear Search", linear_search),
        ("Binary Search", binary_search),
    ]

    for size in sorted(datasets.keys()):
        arr = datasets[size]
        targets = get_test_targets(arr)

        for algo_name, algo_fn in algorithms:
            for case_name, target_val in targets.items():
                found_idx, comps, avg_ns = measure_search_performance(
                    algo_fn, arr, target_val, iterations=iterations
                )
                results.append(
                    BenchmarkResult(
                        algorithm=algo_name,
                        input_size=size,
                        case_name=case_name,
                        target_value=target_val,
                        found_index=found_idx,
                        comparisons=comps,
                        time_ns=round(avg_ns, 2),
                        time_us=round(avg_ns / 1000.0, 4),
                    )
                )

    return results


def format_console_table(results: List[BenchmarkResult]) -> str:
    """Format benchmark results into a clean ASCII table."""
    headers = [
        "Algorithm",
        "Size (N)",
        "Case",
        "Target",
        "Index",
        "Comparisons",
        "Time (ns)",
        "Time (µs)",
    ]
    col_widths = [15, 10, 12, 10, 8, 13, 12, 12]

    header_row = " | ".join(h.ljust(w) for h, w in zip(headers, col_widths))
    separator = "-+-".join("-" * w for w in col_widths)

    rows = []
    for r in results:
        row_vals = [
            r.algorithm,
            str(r.input_size),
            r.case_name,
            str(r.target_value),
            str(r.found_index),
            str(r.comparisons),
            f"{r.time_ns:.2f}",
            f"{r.time_us:.4f}",
        ]
        rows.append(" | ".join(v.ljust(w) for v, w in zip(row_vals, col_widths)))

    return f"{header_row}\n{separator}\n" + "\n".join(rows)


def export_markdown_table(
    results: List[BenchmarkResult],
    filepath: Path | str = "results/results_table.md",
) -> Path:
    """Export benchmark results into a formatted GitHub Markdown table."""
    path = Path(filepath)
    path.parent.mkdir(parents=True, exist_ok=True)

    headers = [
        "Algorithm",
        "Input Size ($N$)",
        "Test Case",
        "Target Value",
        "Found Index",
        "Comparisons",
        "Execution Time (ns)",
        "Execution Time (µs)",
    ]
    lines = [
        "# Problem 1: Experimental Analysis of Searching Algorithms",
        "",
        "## Benchmark Results Table",
        "",
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join(["---"] * len(headers)) + " |",
    ]

    for r in results:
        row = [
            r.algorithm,
            str(r.input_size),
            r.case_name,
            str(r.target_value),
            str(r.found_index),
            str(r.comparisons),
            f"{r.time_ns:.2f}",
            f"{r.time_us:.4f}",
        ]
        lines.append("| " + " | ".join(row) + " |")

    lines.append("")
    lines.append("### Summary Observations")
    lines.append("- **Linear Search**: Execution time and comparison count grow linearly ($O(n)$) with input size for end/absent cases, while beginning case is instantaneous ($O(1)$).")
    lines.append("- **Binary Search**: Execution time and comparison count grow logarithmically ($O(\\log n)$), taking at most $\\approx \\lceil\\log_2 N\\rceil$ comparisons across all sizes.")

    with path.open("w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")

    return path


def export_csv(
    results: List[BenchmarkResult],
    filepath: Path | str = "results/metrics.csv",
) -> Path:
    """Export benchmark results into a CSV file."""
    import csv

    path = Path(filepath)
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(asdict(results[0]).keys()))
        writer.writeheader()
        for r in results:
            writer.writerow(asdict(r))

    return path
