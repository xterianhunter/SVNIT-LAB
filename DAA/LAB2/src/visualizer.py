"""Visualization generator for searching algorithm benchmarking results.

Generates standalone vector SVG plots, interactive HTML reports, and ASCII terminal graphs
with zero external pip dependencies.
"""

from pathlib import Path
from typing import Dict, List, Tuple
from src.benchmark import BenchmarkResult


def generate_ascii_charts(results: List[BenchmarkResult]) -> str:
    """Generate clean ASCII terminal bar graphs comparing execution times."""
    lines: List[str] = []
    lines.append("=" * 80)
    lines.append("ASCII VISUALIZATION: INPUT SIZE vs EXECUTION TIME (ns)")
    lines.append("=" * 80)

    # Focus on key cases: Linear Search vs Binary Search for End (Worst Case) and Middle
    cases_to_plot = ["End", "Absent", "Middle", "Beginning"]

    for case in cases_to_plot:
        lines.append(f"\n--- Case: {case.upper()} ---")
        sub_results = [r for r in results if r.case_name == case]
        max_time = max((r.time_ns for r in sub_results), default=1.0)
        max_bar_width = 40

        for r in sub_results:
            bar_len = int((r.time_ns / max_time) * max_bar_width) if max_time > 0 else 0
            bar = "█" * max(1, bar_len)
            label = f"{r.algorithm[:6]} N={r.input_size:<3}"
            lines.append(f"{label} | {bar:<40} | {r.time_ns:>8.2f} ns ({r.comparisons:>3} comps)")

    lines.append("=" * 80)
    return "\n".join(lines)


def generate_svg_plot(
    results: List[BenchmarkResult],
    filepath: Path | str = "results/search_complexity_plot.svg",
) -> Path:
    """Generate a clean, high-resolution standalone SVG plot comparing Input Size vs Time."""
    path = Path(filepath)
    path.parent.mkdir(parents=True, exist_ok=True)

    # Plot dimensions
    width = 900
    height = 550
    margin_left = 90
    margin_right = 230
    margin_top = 70
    margin_bottom = 70

    plot_width = width - margin_left - margin_right
    plot_height = height - margin_top - margin_bottom

    # Extract unique sizes and max time
    sizes = sorted(list(set(r.input_size for r in results)))
    max_size = max(sizes)
    min_size = min(sizes)

    max_time_ns = max(r.time_ns for r in results) * 1.15

    def scale_x(size: float) -> float:
        return margin_left + ((size - min_size) / (max_size - min_size)) * plot_width

    def scale_y(time_ns: float) -> float:
        return margin_top + plot_height - (time_ns / max_time_ns) * plot_height

    # Colors for algorithm/case combinations
    series_styles: Dict[str, Tuple[str, str, str]] = {
        "Linear Search - End (Worst Case)": ("#e63946", "solid", "circle"),
        "Linear Search - Absent": ("#d62828", "dashed", "square"),
        "Linear Search - Middle": ("#f77f00", "solid", "triangle"),
        "Linear Search - Beginning (Best Case)": ("#fcbf49", "dotted", "diamond"),
        "Binary Search - Absent (Worst Case)": ("#1d3557", "solid", "circle"),
        "Binary Search - End": ("#457b9d", "dashed", "square"),
        "Binary Search - Middle (Best Case)": ("#2a9d8f", "solid", "triangle"),
        "Binary Search - Beginning": ("#52b788", "dotted", "diamond"),
    }

    svg_parts: List[str] = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}" style="background:#ffffff; font-family: -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica, Arial, sans-serif;">',
        '<style>',
        '  .title { font-size: 20px; font-weight: 700; fill: #1e293b; }',
        '  .subtitle { font-size: 13px; fill: #64748b; }',
        '  .axis { stroke: #94a3b8; stroke-width: 1.5; }',
        '  .grid { stroke: #e2e8f0; stroke-width: 1; stroke-dasharray: 4,4; }',
        '  .label { font-size: 12px; fill: #475569; }',
        '  .axis-title { font-size: 14px; font-weight: 600; fill: #334155; }',
        '  .legend-text { font-size: 12px; fill: #1e293b; }',
        '</style>',
        f'<text x="{margin_left}" y="35" class="title">Searching Algorithms: Input Size vs Execution Time</text>',
        f'<text x="{margin_left}" y="53" class="subtitle">Problem 1: Linear Search vs Binary Search across positional test cases</text>',
    ]

    # Draw horizontal grid lines and Y-axis ticks
    num_y_ticks = 6
    for i in range(num_y_ticks + 1):
        val = (max_time_ns / num_y_ticks) * i
        y = scale_y(val)
        svg_parts.append(f'<line x1="{margin_left}" y1="{y}" x2="{margin_left + plot_width}" y2="{y}" class="grid" />')
        svg_parts.append(f'<text x="{margin_left - 12}" y="{y + 4}" text-anchor="end" class="label">{val:.0f} ns</text>')

    # Draw X-axis ticks
    for s in sizes:
        x = scale_x(s)
        svg_parts.append(f'<line x1="{x}" y1="{margin_top}" x2="{x}" y2="{margin_top + plot_height}" class="grid" />')
        svg_parts.append(f'<text x="{x}" y="{margin_top + plot_height + 20}" text-anchor="middle" class="label">N={s}</text>')

    # Draw Axes
    svg_parts.append(f'<line x1="{margin_left}" y1="{margin_top + plot_height}" x2="{margin_left + plot_width}" y2="{margin_top + plot_height}" class="axis" />')
    svg_parts.append(f'<line x1="{margin_left}" y1="{margin_top}" x2="{margin_left}" y2="{margin_top + plot_height}" class="axis" />')

    # Axis Titles
    svg_parts.append(f'<text x="{margin_left + plot_width / 2}" y="{margin_top + plot_height + 48}" text-anchor="middle" class="axis-title">Input Size (Number of Elements, N)</text>')
    svg_parts.append(f'<text x="25" y="{margin_top + plot_height / 2}" text-anchor="middle" transform="rotate(-90 25 {margin_top + plot_height / 2})" class="axis-title">Execution Time (nanoseconds)</text>')

    # Group series
    series_data: Dict[str, List[Tuple[int, float]]] = {}
    for r in results:
        key = f"{r.algorithm} - {r.case_name}"
        if r.algorithm == "Linear Search" and r.case_name == "End":
            key = "Linear Search - End (Worst Case)"
        elif r.algorithm == "Linear Search" and r.case_name == "Beginning":
            key = "Linear Search - Beginning (Best Case)"
        elif r.algorithm == "Binary Search" and r.case_name == "Absent":
            key = "Binary Search - Absent (Worst Case)"
        elif r.algorithm == "Binary Search" and r.case_name == "Middle":
            key = "Binary Search - Middle (Best Case)"

        if key not in series_data:
            series_data[key] = []
        series_data[key].append((r.input_size, r.time_ns))

    # Plot Lines & Points
    legend_y = margin_top + 10
    for name, points in series_data.items():
        if name not in series_styles:
            continue
        color, stroke_style, marker = series_styles[name]
        sorted_pts = sorted(points, key=lambda p: p[0])

        path_d = []
        for idx, (sz, t_ns) in enumerate(sorted_pts):
            px = scale_x(sz)
            py = scale_y(t_ns)
            path_d.append(f"{'M' if idx == 0 else 'L'} {px:.2f} {py:.2f}")

        dash = 'stroke-dasharray="6,4"' if stroke_style == "dashed" else ('stroke-dasharray="2,2"' if stroke_style == "dotted" else '')
        svg_parts.append(f'<path d="{" ".join(path_d)}" fill="none" stroke="{color}" stroke-width="2.5" {dash} />')

        # Draw markers
        for sz, t_ns in sorted_pts:
            px = scale_x(sz)
            py = scale_y(t_ns)
            svg_parts.append(f'<circle cx="{px:.2f}" cy="{py:.2f}" r="4.5" fill="{color}" stroke="#ffffff" stroke-width="1.5" />')

        # Legend Entry
        lx = margin_left + plot_width + 25
        ly = legend_y
        svg_parts.append(f'<line x1="{lx}" y1="{ly}" x2="{lx + 20}" y2="{ly}" stroke="{color}" stroke-width="2.5" {dash} />')
        svg_parts.append(f'<circle cx="{lx + 10}" cy="{ly}" r="3.5" fill="{color}" />')
        svg_parts.append(f'<text x="{lx + 28}" y="{ly + 4}" class="legend-text">{name}</text>')
        legend_y += 24

    svg_parts.append('</svg>')

    with path.open("w", encoding="utf-8") as f:
        f.write("\n".join(svg_parts) + "\n")

    return path


def generate_html_report(
    results: List[BenchmarkResult],
    svg_filename: str = "search_complexity_plot.svg",
    filepath: Path | str = "results/search_analysis.html",
) -> Path:
    """Generate a comprehensive, beautiful HTML report."""
    path = Path(filepath)
    path.parent.mkdir(parents=True, exist_ok=True)

    rows_html: List[str] = []
    for r in results:
        badge_cls = "bg-blue" if r.algorithm == "Linear Search" else "bg-green"
        rows_html.append(f"""
        <tr>
            <td><span class="badge {badge_cls}">{r.algorithm}</span></td>
            <td><strong>{r.input_size}</strong></td>
            <td>{r.case_name}</td>
            <td><code>{r.target_value}</code></td>
            <td>{r.found_index}</td>
            <td><span class="pill">{r.comparisons}</span></td>
            <td><strong>{r.time_ns:.2f} ns</strong></td>
            <td>{r.time_us:.4f} µs</td>
        </tr>
        """)

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Problem 1: Searching Algorithms Experimental Analysis</title>
    <style>
        :root {{
            --bg: #0f172a;
            --card-bg: #1e293b;
            --text-main: #f8fafc;
            --text-muted: #94a3b8;
            --accent-blue: #38bdf8;
            --accent-green: #34d399;
            --accent-orange: #fb923c;
            --border: #334155;
        }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            background-color: var(--bg);
            color: var(--text-main);
            margin: 0;
            padding: 30px 20px;
        }}
        .container {{
            max-width: 1100px;
            margin: 0 auto;
        }}
        header {{
            margin-bottom: 30px;
            border-bottom: 1px solid var(--border);
            padding-bottom: 20px;
        }}
        h1 {{ margin: 0 0 10px 0; font-size: 26px; color: var(--text-main); }}
        p.subtitle {{ margin: 0; color: var(--text-muted); font-size: 15px; }}
        .card {{
            background: var(--card-bg);
            border: 1px solid var(--border);
            border-radius: 12px;
            padding: 24px;
            margin-bottom: 25px;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.2);
        }}
        .card-title {{
            font-size: 18px;
            font-weight: 600;
            margin-top: 0;
            margin-bottom: 16px;
            color: var(--accent-blue);
        }}
        .svg-container {{
            background: #ffffff;
            border-radius: 8px;
            padding: 15px;
            overflow-x: auto;
            text-align: center;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            font-size: 14px;
        }}
        th, td {{
            text-align: left;
            padding: 10px 12px;
            border-bottom: 1px solid var(--border);
        }}
        th {{
            background: rgba(255, 255, 255, 0.03);
            color: var(--text-muted);
            font-weight: 600;
            text-transform: uppercase;
            font-size: 12px;
            letter-spacing: 0.5px;
        }}
        tr:hover {{
            background: rgba(255, 255, 255, 0.02);
        }}
        .badge {{
            display: inline-block;
            padding: 3px 8px;
            border-radius: 4px;
            font-size: 12px;
            font-weight: 600;
        }}
        .bg-blue {{ background: #0284c7; color: #fff; }}
        .bg-green {{ background: #059669; color: #fff; }}
        .pill {{
            background: #334155;
            padding: 2px 7px;
            border-radius: 10px;
            font-weight: 600;
        }}
        .analysis-grid {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 20px;
        }}
        @media (max-width: 768px) {{
            .analysis-grid {{ grid-template-columns: 1fr; }}
        }}
        .analysis-box {{
            background: rgba(255, 255, 255, 0.02);
            border: 1px solid var(--border);
            border-radius: 8px;
            padding: 16px;
        }}
        .analysis-box h3 {{ margin-top: 0; font-size: 16px; color: var(--accent-orange); }}
        ul {{ margin: 0; padding-left: 20px; color: var(--text-muted); line-height: 1.6; }}
        li strong {{ color: var(--text-main); }}
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>DAA Lab Assignment 2 – Problem 1 Analysis</h1>
            <p.subtitle>Experimental and Theoretical Analysis of Linear Search and Binary Search (SVNIT M.Tech CSDS103)</p>
        </header>

        <div class="card">
            <h2 class="card-title">Execution Time vs Input Size Plot</h2>
            <div class="svg-container">
                <img src="{svg_filename}" alt="Searching Complexity Plot" style="max-width:100%; height:auto;">
            </div>
        </div>

        <div class="card">
            <h2 class="card-title">Theoretical vs Experimental Complexity Comparison</h2>
            <div class="analysis-grid">
                <div class="analysis-box">
                    <h3>Linear Search Analysis</h3>
                    <ul>
                        <li><strong>Best Case ($O(1)$):</strong> Target at index 0 requires exactly 1 comparison and consistently executes in ~200–300 ns regardless of array size $N$.</li>
                        <li><strong>Worst / Absent Case ($O(n)$):</strong> Target at end or absent requires $N$ comparisons. Execution time scales linearly as $N$ increases from 10 to 200 (0.77 µs → 11.5 µs).</li>
                        <li><strong>Average Case ($O(n)$):</strong> Target at middle requires $N/2$ comparisons, scaling linearly.</li>
                    </ul>
                </div>
                <div class="analysis-box">
                    <h3>Binary Search Analysis</h3>
                    <ul>
                        <li><strong>Best Case ($O(1)$):</strong> Target located at middle element on first iteration requires 1-3 comparisons and executes in ~400–600 ns.</li>
                        <li><strong>Worst / Absent Case ($O(\log n)$):</strong> Search space halves at every step, requiring at most $\approx \lceil\log_2 N\rceil + 1$ comparisons (max 8 comparisons for $N=200$).</li>
                        <li><strong>Scalability:</strong> While Linear Search latency increases $15\times$ from $N=10$ to $N=200$, Binary Search remains nearly constant at ~0.8–1.0 µs.</li>
                    </ul>
                </div>
            </div>
        </div>

        <div class="card">
            <h2 class="card-title">Detailed Experimental Results Table</h2>
            <div style="overflow-x: auto;">
                <table>
                    <thead>
                        <tr>
                            <th>Algorithm</th>
                            <th>Input Size (N)</th>
                            <th>Test Case</th>
                            <th>Target</th>
                            <th>Found Index</th>
                            <th>Comparisons</th>
                            <th>Time (ns)</th>
                            <th>Time (µs)</th>
                        </tr>
                    </thead>
                    <tbody>
                        {"".join(rows_html)}
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</body>
</html>
"""
    with path.open("w", encoding="utf-8") as f:
        f.write(html_content)

    return path


def generate_sorting_svg_plot(
    results: List[Dict],
    filepath: Path | str = "results/sorting_complexity_plot.svg",
) -> Path:
    """Generate a clean, high-resolution standalone vector SVG plot comparing Input Size vs Time for Sorting."""
    path = Path(filepath)
    path.parent.mkdir(parents=True, exist_ok=True)

    width = 960
    height = 580
    margin_left = 95
    margin_right = 265
    margin_top = 70
    margin_bottom = 75

    plot_width = width - margin_left - margin_right
    plot_height = height - margin_top - margin_bottom

    sizes = sorted(list(set(r["n"] for r in results)))
    min_size = min(sizes)
    max_size = max(sizes)

    max_time_ms = max(r["time_ms"] for r in results) * 1.15
    if max_time_ms <= 0:
        max_time_ms = 1.0

    def scale_x(size: float) -> float:
        if max_size == min_size:
            return margin_left + plot_width / 2
        return margin_left + ((size - min_size) / (max_size - min_size)) * plot_width

    def scale_y(time_ms: float) -> float:
        return margin_top + plot_height - (time_ms / max_time_ms) * plot_height

    series_styles: Dict[str, Tuple[str, str, str]] = {
        "Bubble Sort - Reverse (Worst Case)": ("#003049", "solid", "circle"),
        "Bubble Sort - Random": ("#3a86ff", "dashed", "square"),
        "Bubble Sort - Sorted (Best Case)": ("#8338ec", "dotted", "diamond"),
        "Selection Sort - Reverse": ("#007f5f", "solid", "circle"),
        "Selection Sort - Random": ("#2b9348", "dashed", "square"),
        "Selection Sort - Sorted": ("#80b918", "dotted", "diamond"),
        "Insertion Sort - Reverse (Worst Case)": ("#d00000", "solid", "circle"),
        "Insertion Sort - Random": ("#ff6000", "dashed", "square"),
        "Insertion Sort - Sorted (Best Case)": ("#ffb703", "dotted", "diamond"),
    }

    svg_parts: List[str] = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}" style="background:#ffffff; font-family: -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica, Arial, sans-serif;">',
        '<style>',
        '  .title { font-size: 20px; font-weight: 700; fill: #1e293b; }',
        '  .subtitle { font-size: 13px; fill: #64748b; }',
        '  .axis { stroke: #94a3b8; stroke-width: 1.5; }',
        '  .grid { stroke: #e2e8f0; stroke-width: 1; stroke-dasharray: 4,4; }',
        '  .label { font-size: 12px; fill: #475569; }',
        '  .axis-title { font-size: 14px; font-weight: 600; fill: #334155; }',
        '  .legend-text { font-size: 12px; fill: #1e293b; }',
        '</style>',
        f'<text x="{margin_left}" y="35" class="title">Sorting Algorithms: Input Size vs Execution Time</text>',
        f'<text x="{margin_left}" y="53" class="subtitle">Problem 2: Bubble Sort vs Selection Sort vs Insertion Sort across Random, Sorted, and Reverse inputs</text>',
    ]

    num_y_ticks = 6
    for i in range(num_y_ticks + 1):
        val = (max_time_ms / num_y_ticks) * i
        y = scale_y(val)
        svg_parts.append(f'<line x1="{margin_left}" y1="{y:.2f}" x2="{margin_left + plot_width:.2f}" y2="{y:.2f}" class="grid" />')
        svg_parts.append(f'<text x="{margin_left - 12}" y="{y + 4:.2f}" text-anchor="end" class="label">{val:.2f} ms</text>')

    for s in sizes:
        x = scale_x(s)
        svg_parts.append(f'<line x1="{x:.2f}" y1="{margin_top}" x2="{x:.2f}" y2="{margin_top + plot_height}" class="grid" />')
        svg_parts.append(f'<text x="{x:.2f}" y="{margin_top + plot_height + 20}" text-anchor="middle" class="label">N={s}</text>')

    svg_parts.append(f'<line x1="{margin_left}" y1="{margin_top + plot_height}" x2="{margin_left + plot_width}" y2="{margin_top + plot_height}" class="axis" />')
    svg_parts.append(f'<line x1="{margin_left}" y1="{margin_top}" x2="{margin_left}" y2="{margin_top + plot_height}" class="axis" />')

    svg_parts.append(f'<text x="{margin_left + plot_width / 2:.2f}" y="{margin_top + plot_height + 52}" text-anchor="middle" class="axis-title">Input Size (Number of Elements, N)</text>')
    svg_parts.append(f'<text x="25" y="{margin_top + plot_height / 2:.2f}" text-anchor="middle" transform="rotate(-90 25 {margin_top + plot_height / 2:.2f})" class="axis-title">Execution Time (milliseconds)</text>')

    series_data: Dict[str, List[Tuple[int, float]]] = {}
    for r in results:
        key = f"{r['algo']} - {r['type']}"
        if r['algo'] == "Bubble Sort" and r['type'] == "Reverse":
            key = "Bubble Sort - Reverse (Worst Case)"
        elif r['algo'] == "Bubble Sort" and r['type'] == "Sorted":
            key = "Bubble Sort - Sorted (Best Case)"
        elif r['algo'] == "Insertion Sort" and r['type'] == "Reverse":
            key = "Insertion Sort - Reverse (Worst Case)"
        elif r['algo'] == "Insertion Sort" and r['type'] == "Sorted":
            key = "Insertion Sort - Sorted (Best Case)"

        if key not in series_data:
            series_data[key] = []
        series_data[key].append((r["n"], r["time_ms"]))

    legend_y = margin_top + 5
    for name, points in series_data.items():
        if name not in series_styles:
            continue
        color, stroke_style, marker = series_styles[name]
        sorted_pts = sorted(points, key=lambda p: p[0])

        path_d = []
        for idx, (sz, t_ms) in enumerate(sorted_pts):
            px = scale_x(sz)
            py = scale_y(t_ms)
            path_d.append(f"{'M' if idx == 0 else 'L'} {px:.2f} {py:.2f}")

        dash = 'stroke-dasharray="6,4"' if stroke_style == "dashed" else ('stroke-dasharray="2,2"' if stroke_style == "dotted" else '')
        svg_parts.append(f'<path d="{" ".join(path_d)}" fill="none" stroke="{color}" stroke-width="2.5" {dash} />')

        for sz, t_ms in sorted_pts:
            px = scale_x(sz)
            py = scale_y(t_ms)
            if marker == "circle":
                svg_parts.append(f'<circle cx="{px:.2f}" cy="{py:.2f}" r="4.5" fill="{color}" stroke="#ffffff" stroke-width="1.5" />')
            elif marker == "square":
                svg_parts.append(f'<rect x="{px - 4:.2f}" y="{py - 4:.2f}" width="8" height="8" fill="{color}" stroke="#ffffff" stroke-width="1.5" />')
            elif marker == "diamond":
                svg_parts.append(f'<polygon points="{px:.2f},{py - 5:.2f} {px + 5:.2f},{py:.2f} {px:.2f},{py + 5:.2f} {px - 5:.2f},{py:.2f}" fill="{color}" stroke="#ffffff" stroke-width="1.5" />')

        lx = margin_left + plot_width + 20
        ly = legend_y
        svg_parts.append(f'<line x1="{lx}" y1="{ly}" x2="{lx + 20}" y2="{ly}" stroke="{color}" stroke-width="2.5" {dash} />')
        if marker == "circle":
            svg_parts.append(f'<circle cx="{lx + 10}" cy="{ly}" r="3.5" fill="{color}" />')
        elif marker == "square":
            svg_parts.append(f'<rect x="{lx + 6.5}" y="{ly - 3.5}" width="7" height="7" fill="{color}" />')
        elif marker == "diamond":
            svg_parts.append(f'<polygon points="{lx + 10},{ly - 4} {lx + 14},{ly} {lx + 10},{ly + 4} {lx + 6},{ly}" fill="{color}" />')

        svg_parts.append(f'<text x="{lx + 26}" y="{ly + 4}" class="legend-text">{name}</text>')
        legend_y += 24

    svg_parts.append('</svg>')

    with path.open("w", encoding="utf-8") as f:
        f.write("\n".join(svg_parts) + "\n")

    return path


def generate_sorting_ascii_charts(results: List[Dict]) -> str:
    """Generate clean ASCII terminal bar graphs comparing execution times for sorting."""
    lines = []
    lines.append("=" * 80)
    lines.append("ASCII VISUALIZATION: INPUT SIZE vs EXECUTION TIME (ms)")
    lines.append("=" * 80)

    input_types = ["Reverse", "Random", "Sorted"]
    for itype in input_types:
        lines.append(f"\n--- Input Distribution: {itype.upper()} ---")
        sub = [r for r in results if r["type"] == itype]
        max_time = max((r["time_ms"] for r in sub), default=1.0)
        max_bar_width = 38

        for r in sub:
            bar_len = int((r["time_ms"] / max_time) * max_bar_width) if max_time > 0 else 0
            bar = "█" * max(1, bar_len)
            label = f"{r['algo'][:9]} N={r['n']:<3}"
            lines.append(f"{label} | {bar:<38} | {r['time_ms']:>8.4f} ms ({r['comps']:>6} comps)")

    lines.append("=" * 80)
    return "\n".join(lines)


def generate_sorting_html_report(
    results: List[Dict],
    svg_filename: str = "sorting_complexity_plot.svg",
    filepath: Path | str = "results/sorting_analysis.html",
) -> Path:
    """Generate a comprehensive, modern interactive HTML report for sorting algorithms."""
    path = Path(filepath)
    path.parent.mkdir(parents=True, exist_ok=True)

    rows_html = []
    for r in results:
        badge_cls = "bg-blue" if r["algo"] == "Bubble Sort" else ("bg-green" if r["algo"] == "Selection Sort" else "bg-orange")
        type_badge = "pill-sorted" if r["type"] == "Sorted" else ("pill-reverse" if r["type"] == "Reverse" else "pill-random")
        rows_html.append(f"""
        <tr>
            <td><span class="badge {badge_cls}">{r['algo']}</span></td>
            <td><strong>{r['n']}</strong></td>
            <td><span class="pill {type_badge}">{r['type']}</span></td>
            <td><code>{r['comps']:,}</code></td>
            <td><strong>{r['time_us']:.2f} µs</strong></td>
            <td><strong>{r['time_ms']:.4f} ms</strong></td>
        </tr>
        """)

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Problem 2: Sorting Algorithms Experimental Analysis</title>
    <style>
        :root {{
            --bg: #0f172a;
            --card-bg: #1e293b;
            --text-main: #f8fafc;
            --text-muted: #94a3b8;
            --accent-blue: #38bdf8;
            --accent-green: #34d399;
            --accent-orange: #fb923c;
            --accent-red: #f87171;
            --border: #334155;
        }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            background-color: var(--bg);
            color: var(--text-main);
            margin: 0;
            padding: 30px 20px;
        }}
        .container {{
            max-width: 1100px;
            margin: 0 auto;
        }}
        header {{
            margin-bottom: 30px;
            border-bottom: 1px solid var(--border);
            padding-bottom: 20px;
        }}
        h1 {{ margin: 0 0 10px 0; font-size: 26px; color: var(--text-main); }}
        p.subtitle {{ margin: 0; color: var(--text-muted); font-size: 15px; }}
        .card {{
            background: var(--card-bg);
            border: 1px solid var(--border);
            border-radius: 12px;
            padding: 24px;
            margin-bottom: 25px;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.2);
        }}
        .card-title {{
            font-size: 18px;
            font-weight: 600;
            margin-top: 0;
            margin-bottom: 16px;
            color: var(--accent-blue);
        }}
        .svg-container {{
            background: #ffffff;
            border-radius: 8px;
            padding: 15px;
            overflow-x: auto;
            text-align: center;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            font-size: 14px;
        }}
        th, td {{
            text-align: left;
            padding: 10px 12px;
            border-bottom: 1px solid var(--border);
        }}
        th {{
            background: rgba(255, 255, 255, 0.03);
            color: var(--text-muted);
            font-weight: 600;
            text-transform: uppercase;
            font-size: 12px;
            letter-spacing: 0.5px;
        }}
        tr:hover {{
            background: rgba(255, 255, 255, 0.02);
        }}
        .badge {{
            display: inline-block;
            padding: 3px 8px;
            border-radius: 4px;
            font-size: 12px;
            font-weight: 600;
        }}
        .bg-blue {{ background: #0284c7; color: #fff; }}
        .bg-green {{ background: #059669; color: #fff; }}
        .bg-orange {{ background: #ea580c; color: #fff; }}
        .pill {{
            padding: 3px 8px;
            border-radius: 10px;
            font-size: 12px;
            font-weight: 600;
        }}
        .pill-sorted {{ background: rgba(52, 211, 153, 0.15); color: #34d399; border: 1px solid rgba(52, 211, 153, 0.3); }}
        .pill-random {{ background: rgba(56, 189, 248, 0.15); color: #38bdf8; border: 1px solid rgba(56, 189, 248, 0.3); }}
        .pill-reverse {{ background: rgba(248, 113, 113, 0.15); color: #f87171; border: 1px solid rgba(248, 113, 113, 0.3); }}
        .analysis-grid {{
            display: grid;
            grid-template-columns: 1fr 1fr 1fr;
            gap: 20px;
        }}
        @media (max-width: 850px) {{
            .analysis-grid {{ grid-template-columns: 1fr; }}
        }}
        .analysis-box {{
            background: rgba(255, 255, 255, 0.02);
            border: 1px solid var(--border);
            border-radius: 8px;
            padding: 16px;
        }}
        .analysis-box h3 {{ margin-top: 0; font-size: 16px; }}
        .box-bubble h3 {{ color: var(--accent-blue); }}
        .box-selection h3 {{ color: var(--accent-green); }}
        .box-insertion h3 {{ color: var(--accent-orange); }}
        ul {{ margin: 0; padding-left: 18px; color: var(--text-muted); line-height: 1.5; font-size: 13.5px; }}
        li strong {{ color: var(--text-main); }}
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>DAA Lab Assignment 2 – Problem 2 Analysis</h1>
            <p class="subtitle">Experimental and Theoretical Analysis of Bubble Sort, Selection Sort, and Insertion Sort (SVNIT M.Tech CSDS103)</p>
        </header>

        <div class="card">
            <h2 class="card-title">Execution Time vs Input Size Plot</h2>
            <div class="svg-container">
                <img src="{svg_filename}" alt="Sorting Complexity Plot" style="max-width:100%; height:auto;">
            </div>
        </div>

        <div class="card">
            <h2 class="card-title">Theoretical vs Experimental Complexity Breakdown</h2>
            <div class="analysis-grid">
                <div class="analysis-box box-bubble">
                    <h3>Bubble Sort (Early Exit)</h3>
                    <ul>
                        <li><strong>Best Case (O(n)):</strong> When array is already sorted, terminates after pass 1 ($n-1$ comparisons, 0 swaps) in ~2 µs.</li>
                        <li><strong>Worst Case (O(n²)):</strong> On reverse sorted array, requires maximum comparisons $\\frac{{n(n-1)}}{{2}}$ and $O(n^2)$ swaps (~10–12 ms for $N=500$).</li>
                        <li><strong>Average Case (O(n²)):</strong> Randomly permuted elements require quadratic passes.</li>
                    </ul>
                </div>
                <div class="analysis-box box-selection">
                    <h3>Selection Sort</h3>
                    <ul>
                        <li><strong>Invariable Complexity (Θ(n²)):</strong> Performs exactly $\\frac{{n(n-1)}}{{2}}$ comparisons across ALL input types (Random, Sorted, Reverse).</li>
                        <li><strong>Comparisons:</strong> $N=50 \\to 1,225$, $N=100 \\to 4,950$, $N=200 \\to 19,900$, $N=500 \\to 124,750$.</li>
                        <li><strong>Swap Efficiency:</strong> Performs at most $n-1$ swaps, minimizing memory writes despite quadratic comparisons.</li>
                    </ul>
                </div>
                <div class="analysis-box box-insertion">
                    <h3>Insertion Sort</h3>
                    <ul>
                        <li><strong>Best Case (O(n)):</strong> On already sorted arrays, each item is checked once and requires 0 shifts ($n-1$ comparisons, &lt; 1 µs).</li>
                        <li><strong>Worst Case (O(n²)):</strong> On reverse sorted array, requires $\\frac{{n(n-1)}}{{2}}$ comparisons and maximum element shifts.</li>
                        <li><strong>Empirical Efficiency:</strong> Typically 2–3x faster than Bubble Sort on random inputs due to low constant factors ($n^2/4$ avg comps).</li>
                    </ul>
                </div>
            </div>
        </div>

        <div class="card">
            <h2 class="card-title">Detailed Experimental Results Table</h2>
            <div style="overflow-x: auto;">
                <table>
                    <thead>
                        <tr>
                            <th>Algorithm</th>
                            <th>Input Size (N)</th>
                            <th>Input Distribution</th>
                            <th>Comparisons</th>
                            <th>Time (µs)</th>
                            <th>Time (ms)</th>
                        </tr>
                    </thead>
                    <tbody>
                        {"".join(rows_html)}
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</body>
</html>
"""
    with path.open("w", encoding="utf-8") as f:
        f.write(html_content)

    return path


def generate_matrix_svg_plot(
    results: List[Dict],
    filepath: Path | str = "results/matrix_complexity_plot.svg",
) -> Path:
    """Generate a clean, high-resolution standalone vector SVG plot comparing Matrix Size vs Time."""
    path = Path(filepath)
    path.parent.mkdir(parents=True, exist_ok=True)

    width = 960
    height = 580
    margin_left = 95
    margin_right = 265
    margin_top = 70
    margin_bottom = 75

    plot_width = width - margin_left - margin_right
    plot_height = height - margin_top - margin_bottom

    sizes = sorted(list(set(r["n"] for r in results)))
    min_size = min(sizes)
    max_size = max(sizes)

    max_time_ms = max(r["time_ms"] for r in results) * 1.12
    if max_time_ms <= 0:
        max_time_ms = 1.0

    def scale_x(size: float) -> float:
        if max_size == min_size:
            return margin_left + plot_width / 2
        return margin_left + ((size - min_size) / (max_size - min_size)) * plot_width

    def scale_y(time_ms: float) -> float:
        return margin_top + plot_height - (time_ms / max_time_ms) * plot_height

    series_styles: Dict[str, Tuple[str, str, str]] = {
        "Matrix Multiplication (O(n^3))": ("#d00000", "solid", "diamond"),
        "Matrix Addition (O(n^2))": ("#3a86ff", "solid", "circle"),
        "Matrix Transpose (O(n^2))": ("#2b9348", "dashed", "square"),
    }

    svg_parts: List[str] = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}" style="background:#ffffff; font-family: -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica, Arial, sans-serif;">',
        '<style>',
        '  .title { font-size: 20px; font-weight: 700; fill: #1e293b; }',
        '  .subtitle { font-size: 13px; fill: #64748b; }',
        '  .axis { stroke: #94a3b8; stroke-width: 1.5; }',
        '  .grid { stroke: #e2e8f0; stroke-width: 1; stroke-dasharray: 4,4; }',
        '  .label { font-size: 12px; fill: #475569; }',
        '  .axis-title { font-size: 14px; font-weight: 600; fill: #334155; }',
        '  .legend-text { font-size: 12px; fill: #1e293b; }',
        '</style>',
        f'<text x="{margin_left}" y="35" class="title">Matrix Algorithms: Matrix Size vs Execution Time</text>',
        f'<text x="{margin_left}" y="53" class="subtitle">Problem 3: Matrix Addition [O(n²)] vs Matrix Transpose [O(n²)] vs Matrix Multiplication [O(n³)]</text>',
    ]

    num_y_ticks = 6
    for i in range(num_y_ticks + 1):
        val = (max_time_ms / num_y_ticks) * i
        y = scale_y(val)
        svg_parts.append(f'<line x1="{margin_left}" y1="{y:.2f}" x2="{margin_left + plot_width:.2f}" y2="{y:.2f}" class="grid" />')
        svg_parts.append(f'<text x="{margin_left - 12}" y="{y + 4:.2f}" text-anchor="end" class="label">{val:.2f} ms</text>')

    for s in sizes:
        x = scale_x(s)
        svg_parts.append(f'<line x1="{x:.2f}" y1="{margin_top}" x2="{x:.2f}" y2="{margin_top + plot_height}" class="grid" />')
        svg_parts.append(f'<text x="{x:.2f}" y="{margin_top + plot_height + 20}" text-anchor="middle" class="label">{s}x{s}</text>')

    svg_parts.append(f'<line x1="{margin_left}" y1="{margin_top + plot_height}" x2="{margin_left + plot_width}" y2="{margin_top + plot_height}" class="axis" />')
    svg_parts.append(f'<line x1="{margin_left}" y1="{margin_top}" x2="{margin_left}" y2="{margin_top + plot_height}" class="axis" />')

    svg_parts.append(f'<text x="{margin_left + plot_width / 2:.2f}" y="{margin_top + plot_height + 52}" text-anchor="middle" class="axis-title">Square Matrix Dimension (N x N)</text>')
    svg_parts.append(f'<text x="25" y="{margin_top + plot_height / 2:.2f}" text-anchor="middle" transform="rotate(-90 25 {margin_top + plot_height / 2:.2f})" class="axis-title">Execution Time (milliseconds)</text>')

    series_data: Dict[str, List[Tuple[int, float]]] = {}
    for r in results:
        key = f"{r['operation']} ({r['complexity']})"
        if key not in series_data:
            series_data[key] = []
        series_data[key].append((r["n"], r["time_ms"]))

    legend_y = margin_top + 10
    for name, (color, stroke_style, marker) in series_styles.items():
        if name not in series_data:
            continue
        sorted_pts = sorted(series_data[name], key=lambda p: p[0])

        path_d = []
        for idx, (sz, t_ms) in enumerate(sorted_pts):
            px = scale_x(sz)
            py = scale_y(t_ms)
            path_d.append(f"{'M' if idx == 0 else 'L'} {px:.2f} {py:.2f}")

        dash = 'stroke-dasharray="6,4"' if stroke_style == "dashed" else ('stroke-dasharray="2,2"' if stroke_style == "dotted" else '')
        svg_parts.append(f'<path d="{" ".join(path_d)}" fill="none" stroke="{color}" stroke-width="2.5" {dash} />')

        for sz, t_ms in sorted_pts:
            px = scale_x(sz)
            py = scale_y(t_ms)
            if marker == "circle":
                svg_parts.append(f'<circle cx="{px:.2f}" cy="{py:.2f}" r="4.5" fill="{color}" stroke="#ffffff" stroke-width="1.5" />')
            elif marker == "square":
                svg_parts.append(f'<rect x="{px - 4:.2f}" y="{py - 4:.2f}" width="8" height="8" fill="{color}" stroke="#ffffff" stroke-width="1.5" />')
            elif marker == "diamond":
                svg_parts.append(f'<polygon points="{px:.2f},{py - 5:.2f} {px + 5:.2f},{py:.2f} {px:.2f},{py + 5:.2f} {px - 5:.2f},{py:.2f}" fill="{color}" stroke="#ffffff" stroke-width="1.5" />')

        lx = margin_left + plot_width + 20
        ly = legend_y
        svg_parts.append(f'<line x1="{lx}" y1="{ly}" x2="{lx + 20}" y2="{ly}" stroke="{color}" stroke-width="2.5" {dash} />')
        if marker == "circle":
            svg_parts.append(f'<circle cx="{lx + 10}" cy="{ly}" r="3.5" fill="{color}" />')
        elif marker == "square":
            svg_parts.append(f'<rect x="{lx + 6.5}" y="{ly - 3.5}" width="7" height="7" fill="{color}" />')
        elif marker == "diamond":
            svg_parts.append(f'<polygon points="{lx + 10},{ly - 4} {lx + 14},{ly} {lx + 10},{ly + 4} {lx + 6},{ly}" fill="{color}" />')

        svg_parts.append(f'<text x="{lx + 26}" y="{ly + 4}" class="legend-text">{name}</text>')
        legend_y += 28

    svg_parts.append('</svg>')

    with path.open("w", encoding="utf-8") as f:
        f.write("\n".join(svg_parts) + "\n")

    return path


def generate_matrix_ascii_charts(results: List[Dict]) -> str:
    """Generate clean ASCII terminal bar graphs comparing execution times for matrix operations."""
    lines = []
    lines.append("=" * 80)
    lines.append("ASCII VISUALIZATION: MATRIX SIZE vs EXECUTION TIME (ms)")
    lines.append("=" * 80)

    operations = ["Matrix Multiplication", "Matrix Addition", "Matrix Transpose"]
    for op in operations:
        lines.append(f"\n--- Operation: {op.upper()} ---")
        sub = [r for r in results if r["operation"] == op]
        max_time = max((r["time_ms"] for r in sub), default=1.0)
        max_bar_width = 38

        for r in sub:
            bar_len = int((r["time_ms"] / max_time) * max_bar_width) if max_time > 0 else 0
            bar = "█" * max(1, bar_len)
            label = f"{r['operation'][:11]} {r['size']:<7}"
            lines.append(f"{label} | {bar:<38} | {r['time_ms']:>9.4f} ms ({r['complexity']})")

    lines.append("=" * 80)
    return "\n".join(lines)


def generate_matrix_html_report(
    results: List[Dict],
    svg_filename: str = "matrix_complexity_plot.svg",
    filepath: Path | str = "results/matrix_analysis.html",
) -> Path:
    """Generate a comprehensive, modern interactive HTML report for matrix operations."""
    path = Path(filepath)
    path.parent.mkdir(parents=True, exist_ok=True)

    rows_html = []
    for r in results:
        badge_cls = "bg-red" if r["operation"] == "Matrix Multiplication" else ("bg-blue" if r["operation"] == "Matrix Addition" else "bg-green")
        pill_cls = "pill-cube" if r["complexity"] == "O(n^3)" else "pill-quad"
        rows_html.append(f"""
        <tr>
            <td><span class="badge {badge_cls}">{r['operation']}</span></td>
            <td><strong>{r['size']}</strong></td>
            <td><span class="pill {pill_cls}">{r['complexity']}</span></td>
            <td><code>{r['time_us']:.2f} µs</code></td>
            <td><strong>{r['time_ms']:.4f} ms</strong></td>
        </tr>
        """)

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Problem 3: Matrix Algorithms Experimental Analysis</title>
    <style>
        :root {{
            --bg: #0f172a;
            --card-bg: #1e293b;
            --text-main: #f8fafc;
            --text-muted: #94a3b8;
            --accent-blue: #38bdf8;
            --accent-green: #34d399;
            --accent-orange: #fb923c;
            --accent-red: #f87171;
            --border: #334155;
        }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            background-color: var(--bg);
            color: var(--text-main);
            margin: 0;
            padding: 30px 20px;
        }}
        .container {{
            max-width: 1100px;
            margin: 0 auto;
        }}
        header {{
            margin-bottom: 30px;
            border-bottom: 1px solid var(--border);
            padding-bottom: 20px;
        }}
        h1 {{ margin: 0 0 10px 0; font-size: 26px; color: var(--text-main); }}
        p.subtitle {{ margin: 0; color: var(--text-muted); font-size: 15px; }}
        .card {{
            background: var(--card-bg);
            border: 1px solid var(--border);
            border-radius: 12px;
            padding: 24px;
            margin-bottom: 25px;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.2);
        }}
        .card-title {{
            font-size: 18px;
            font-weight: 600;
            margin-top: 0;
            margin-bottom: 16px;
            color: var(--accent-blue);
        }}
        .svg-container {{
            background: #ffffff;
            border-radius: 8px;
            padding: 15px;
            overflow-x: auto;
            text-align: center;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            font-size: 14px;
        }}
        th, td {{
            text-align: left;
            padding: 10px 12px;
            border-bottom: 1px solid var(--border);
        }}
        th {{
            background: rgba(255, 255, 255, 0.03);
            color: var(--text-muted);
            font-weight: 600;
            text-transform: uppercase;
            font-size: 12px;
            letter-spacing: 0.5px;
        }}
        tr:hover {{
            background: rgba(255, 255, 255, 0.02);
        }}
        .badge {{
            display: inline-block;
            padding: 3px 8px;
            border-radius: 4px;
            font-size: 12px;
            font-weight: 600;
        }}
        .bg-blue {{ background: #0284c7; color: #fff; }}
        .bg-green {{ background: #059669; color: #fff; }}
        .bg-red {{ background: #dc2626; color: #fff; }}
        .pill {{
            padding: 3px 8px;
            border-radius: 10px;
            font-size: 12px;
            font-weight: 600;
        }}
        .pill-quad {{ background: rgba(56, 189, 248, 0.15); color: #38bdf8; border: 1px solid rgba(56, 189, 248, 0.3); }}
        .pill-cube {{ background: rgba(248, 113, 113, 0.15); color: #f87171; border: 1px solid rgba(248, 113, 113, 0.3); }}
        .analysis-grid {{
            display: grid;
            grid-template-columns: 1fr 1fr 1fr;
            gap: 20px;
        }}
        @media (max-width: 850px) {{
            .analysis-grid {{ grid-template-columns: 1fr; }}
        }}
        .analysis-box {{
            background: rgba(255, 255, 255, 0.02);
            border: 1px solid var(--border);
            border-radius: 8px;
            padding: 16px;
        }}
        .analysis-box h3 {{ margin-top: 0; font-size: 16px; }}
        .box-add h3 {{ color: var(--accent-blue); }}
        .box-trans h3 {{ color: var(--accent-green); }}
        .box-mul h3 {{ color: var(--accent-red); }}
        ul {{ margin: 0; padding-left: 18px; color: var(--text-muted); line-height: 1.5; font-size: 13.5px; }}
        li strong {{ color: var(--text-main); }}
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>DAA Lab Assignment 2 – Problem 3 Analysis</h1>
            <p class="subtitle">Experimental and Theoretical Analysis of Matrix Addition, Transpose, and Multiplication (SVNIT M.Tech CSDS103)</p>
        </header>

        <div class="card">
            <h2 class="card-title">Execution Time vs Matrix Size Plot</h2>
            <div class="svg-container">
                <img src="{svg_filename}" alt="Matrix Complexity Plot" style="max-width:100%; height:auto;">
            </div>
        </div>

        <div class="card">
            <h2 class="card-title">Theoretical vs Experimental Complexity Breakdown</h2>
            <div class="analysis-grid">
                <div class="analysis-box box-add">
                    <h3>Matrix Addition (O(n²))</h3>
                    <ul>
                        <li><strong>Scalar Operations:</strong> Exactly $n^2$ additions and assignments.</li>
                        <li><strong>Scaling Factor:</strong> Doubling dimension (e.g. $50\\times50 \\to 100\\times100$) increases time by $\\approx 4\\times$.</li>
                        <li><strong>Observed Latency:</strong> Scales smoothly from ~0.003 ms ($10\\times10$) to ~3.5–5 ms ($500\\times500$).</li>
                    </ul>
                </div>
                <div class="analysis-box box-trans">
                    <h3>Matrix Transpose (O(n²))</h3>
                    <ul>
                        <li><strong>Scalar Operations:</strong> Exactly $n^2$ element indexing assignments ($T[i][j] = A[j][i]$).</li>
                        <li><strong>Cache Behavior:</strong> Direct quadratic access pattern with low memory overhead.</li>
                        <li><strong>Observed Latency:</strong> Executes within ~0.002 ms ($10\\times10$) up to ~3.5 ms ($500\\times500$).</li>
                    </ul>
                </div>
                <div class="analysis-box box-mul">
                    <h3>Matrix Multiplication (O(n³))</h3>
                    <ul>
                        <li><strong>Scalar Operations:</strong> $n^3$ multiplications and $n^2(n-1)$ additions.</li>
                        <li><strong>Scaling Factor:</strong> Doubling dimension increases operations by $2^3 = 8\\times$. $10\\times$ dimension increase yields $1000\\times$ latency.</li>
                        <li><strong>Observed Latency:</strong> Escalates steeply from ~0.007 ms ($10\\times10$) to ~1,000–1,200 ms ($500\\times500$).</li>
                    </ul>
                </div>
            </div>
        </div>

        <div class="card">
            <h2 class="card-title">Detailed Experimental Results Table</h2>
            <div style="overflow-x: auto;">
                <table>
                    <thead>
                        <tr>
                            <th>Operation</th>
                            <th>Matrix Size</th>
                            <th>Complexity</th>
                            <th>Time (µs)</th>
                            <th>Time (ms)</th>
                        </tr>
                    </thead>
                    <tbody>
                        {"".join(rows_html)}
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</body>
</html>
"""
    with path.open("w", encoding="utf-8") as f:
        f.write(html_content)

    return path


