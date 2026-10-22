import time
import random
import matplotlib.pyplot as plt

# Set random seed for reproducibility
random.seed(42)

# --- Problem 1 Implementations ---
def count_inversions_dc(arr):
    if len(arr) <= 1:
        return arr, 0
    mid = len(arr) // 2
    left, inv_left = count_inversions_dc(arr[:mid])
    right, inv_right = count_inversions_dc(arr[mid:])
    
    merged = []
    i = j = inv_split = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            inv_split += len(left) - i
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged, inv_left + inv_right + inv_split

def count_inversions_bf(arr):
    inv = 0
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                inv += 1
    return inv

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + mid + quick_sort(right)

def insertion_sort(arr):
    a = arr.copy()
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a

print("=== Problem 1 Verification ===")
sample = [8, 4, 2, 1]
sorted_sample, inv_dc = count_inversions_dc(sample)
inv_bf = count_inversions_bf(sample)
print(f"Original Array: {sample}")
print(f"Divide & Conquer: Sorted = {sorted_sample}, Inversions = {inv_dc}")
print(f"Brute Force:      Inversions = {inv_bf}")

# Problem 1 Benchmarking
p1_sizes = [100, 200, 400, 800, 1600, 3200]
t_dc, t_bf, t_quick, t_insert = [], [], [], []

for n in p1_sizes:
    arr = [random.randint(1, 100000) for _ in range(n)]
    
    t0 = time.perf_counter()
    count_inversions_dc(arr)
    t_dc.append(time.perf_counter() - t0)
    
    t0 = time.perf_counter()
    count_inversions_bf(arr)
    t_bf.append(time.perf_counter() - t0)
    
    t0 = time.perf_counter()
    quick_sort(arr)
    t_quick.append(time.perf_counter() - t0)
    
    t0 = time.perf_counter()
    insertion_sort(arr)
    t_insert.append(time.perf_counter() - t0)

print("\n=== Problem 1 Benchmark Timings (seconds) ===")
print("n\tD&C (s)\t\tBF (s)\t\tQuick (s)\tInsert (s)")
for i, n in enumerate(p1_sizes):
    print(f"{n}\t{t_dc[i]:.6f}\t{t_bf[i]:.6f}\t{t_quick[i]:.6f}\t{t_insert[i]:.6f}")

# Plotting Problem 1
plt.figure(figsize=(8, 4.5), dpi=300)
plt.plot(p1_sizes, t_dc, marker='o', linewidth=1.5, label='D&C Inversion Count (O(n log n))')
plt.plot(p1_sizes, t_bf, marker='s', linewidth=1.5, label='Brute Force Inversion Count (O(n²))')
plt.plot(p1_sizes, t_quick, marker='^', linewidth=1.5, label='Quick Sort (O(n log n))')
plt.plot(p1_sizes, t_insert, marker='d', linewidth=1.5, label='Insertion Sort (O(n²))')

plt.title('Problem 1: Input Size vs Execution Time', fontsize=12, fontweight='bold')
plt.xlabel('Input Size (n)', fontsize=11)
plt.ylabel('Execution Time (seconds)', fontsize=11)
plt.legend(fontsize=9.5)
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig('p1_inversion_benchmark.png')
plt.close()
print("Saved p1_inversion_benchmark.png")


# --- Problem 2 Implementations ---
def power_iterative(a, n):
    res = 1
    for _ in range(n):
        res *= a
    return res

def power_recursive_naive(a, n):
    if n == 0:
        return 1
    if n % 2 == 0:
        return power_recursive_naive(a, n // 2) * power_recursive_naive(a, n // 2)
    else:
        return a * power_recursive_naive(a, n - 1)

def power_dc(a, n):
    if n == 0:
        return 1
    half = power_dc(a, n // 2)
    if n % 2 == 0:
        return half * half
    else:
        return a * half * half

def power_dc_iterative(a, n):
    res = 1
    base = a
    while n > 0:
        if n % 2 == 1:
            res *= base
        base *= base
        n //= 2
    return res

print("\n=== Problem 2 Verification ===")
a, n = 2, 10
p_iter = power_iterative(a, n)
p_naive = power_recursive_naive(a, n)
p_dc = power_dc(a, n)
p_dc_iter = power_dc_iterative(a, n)

print(f"Computing {a}^{n}:")
print(f"Repeated Multiplication : {p_iter}")
print(f"Naive Recursive         : {p_naive}")
print(f"Divide and Conquer      : {p_dc}")
print(f"Iterative D&C           : {p_dc_iter}")

# Problem 2 Benchmarking
p2_n_values = [50, 100, 150, 200, 250, 300, 400, 500]
t_iter, t_naive, t_fast = [], [], []
a = 2

for exp in p2_n_values:
    # Run repeated multiplication
    t0 = time.perf_counter()
    for _ in range(100):
        power_iterative(a, exp)
    t_iter.append((time.perf_counter() - t0) / 100.0)
    
    # Run naive recursive
    t0 = time.perf_counter()
    for _ in range(100):
        power_recursive_naive(a, exp)
    t_naive.append((time.perf_counter() - t0) / 100.0)
    
    # Run divide and conquer
    t0 = time.perf_counter()
    for _ in range(100):
        power_dc(a, exp)
    t_fast.append((time.perf_counter() - t0) / 100.0)

print("\n=== Problem 2 Benchmark Timings (seconds) ===")
print("Exponent (n)\tRepeated Mult (s)\tNaive Rec (s)\t\tD&C (s)")
for i, exp in enumerate(p2_n_values):
    print(f"{exp}\t\t{t_iter[i]:.8f}\t\t{t_naive[i]:.8f}\t\t{t_fast[i]:.8f}")

# Plotting Problem 2
plt.figure(figsize=(8, 4.5), dpi=300)
plt.plot(p2_n_values, t_iter, marker='o', linewidth=1.5, label='Repeated Multiplication (O(n))')
plt.plot(p2_n_values, t_naive, marker='s', linewidth=1.5, label='Naive Recursive (O(n))')
plt.plot(p2_n_values, t_fast, marker='^', linewidth=1.5, label='Divide & Conquer (O(log n))')

plt.title('Problem 2: Exponent (n) vs Execution Time', fontsize=12, fontweight='bold')
plt.xlabel('Exponent (n)', fontsize=11)
plt.ylabel('Execution Time (seconds)', fontsize=11)
plt.legend(fontsize=9.5)
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig('p2_exponentiation_benchmark.png')
plt.close()
print("Saved p2_exponentiation_benchmark.png")
