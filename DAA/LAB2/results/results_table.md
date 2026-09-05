# Problem 1: Experimental Analysis of Searching Algorithms

## Benchmark Results Table

| Algorithm | Input Size ($N$) | Test Case | Target Value | Found Index | Comparisons | Execution Time (ns) | Execution Time (µs) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Linear Search | 10 | Beginning | 26 | 0 | 1 | 275.19 | 0.2752 |
| Linear Search | 10 | Middle | 251 | 5 | 6 | 590.02 | 0.5900 |
| Linear Search | 10 | End | 760 | 9 | 10 | 577.56 | 0.5776 |
| Linear Search | 10 | Absent | 1760 | -1 | 10 | 554.75 | 0.5548 |
| Binary Search | 10 | Beginning | 26 | 0 | 3 | 422.83 | 0.4228 |
| Binary Search | 10 | Middle | 251 | 5 | 3 | 379.75 | 0.3798 |
| Binary Search | 10 | End | 760 | 9 | 4 | 578.26 | 0.5783 |
| Binary Search | 10 | Absent | 1760 | -1 | 4 | 584.33 | 0.5843 |
| Linear Search | 50 | Beginning | 7 | 0 | 1 | 203.67 | 0.2037 |
| Linear Search | 50 | Middle | 430 | 25 | 26 | 1363.10 | 1.3631 |
| Linear Search | 50 | End | 981 | 49 | 50 | 1973.99 | 1.9740 |
| Linear Search | 50 | Absent | 1981 | -1 | 50 | 1857.78 | 1.8578 |
| Binary Search | 50 | Beginning | 7 | 0 | 5 | 571.22 | 0.5712 |
| Binary Search | 50 | Middle | 430 | 25 | 5 | 602.09 | 0.6021 |
| Binary Search | 50 | End | 981 | 49 | 6 | 683.29 | 0.6833 |
| Binary Search | 50 | Absent | 1981 | -1 | 6 | 707.59 | 0.7076 |
| Linear Search | 100 | Beginning | 7 | 0 | 1 | 202.75 | 0.2028 |
| Linear Search | 100 | Middle | 465 | 50 | 51 | 1772.19 | 1.7722 |
| Linear Search | 100 | End | 990 | 99 | 100 | 3570.30 | 3.5703 |
| Linear Search | 100 | Absent | 1990 | -1 | 100 | 3402.05 | 3.4020 |
| Binary Search | 100 | Beginning | 7 | 0 | 6 | 659.14 | 0.6591 |
| Binary Search | 100 | Middle | 465 | 50 | 6 | 663.85 | 0.6638 |
| Binary Search | 100 | End | 990 | 99 | 7 | 772.49 | 0.7725 |
| Binary Search | 100 | Absent | 1990 | -1 | 7 | 798.43 | 0.7984 |
| Linear Search | 200 | Beginning | 7 | 0 | 1 | 209.17 | 0.2092 |
| Linear Search | 200 | Middle | 1035 | 100 | 101 | 3348.57 | 3.3486 |
| Linear Search | 200 | End | 1993 | 199 | 200 | 7890.75 | 7.8908 |
| Linear Search | 200 | Absent | 2993 | -1 | 200 | 7520.56 | 7.5206 |
| Binary Search | 200 | Beginning | 7 | 0 | 7 | 786.23 | 0.7862 |
| Binary Search | 200 | Middle | 1035 | 100 | 7 | 814.11 | 0.8141 |
| Binary Search | 200 | End | 1993 | 199 | 8 | 1114.03 | 1.1140 |
| Binary Search | 200 | Absent | 2993 | -1 | 8 | 965.25 | 0.9653 |

### Summary Observations
- **Linear Search**: Execution time and comparison count grow linearly ($O(n)$) with input size for end/absent cases, while beginning case is instantaneous ($O(1)$).
- **Binary Search**: Execution time and comparison count grow logarithmically ($O(\log n)$), taking at most $\approx \lceil\log_2 N\rceil$ comparisons across all sizes.
