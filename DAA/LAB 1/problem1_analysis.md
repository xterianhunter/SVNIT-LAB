# Problem 1: Employee Directory – Detailed Analysis & Report

**Course**: Design and Analysis of Algorithm (CSDS103)  
**Department**: Computer Science and Engineering Department, SVNIT, Surat  
**Program**: M.Tech. I – Semester I  

---

## 1. Problem Statement

An organisation maintains the names of $n$ employees in an unsorted list. The objective is to:
1. Arrange the names in lexicographical order without using built-in sorting functions.
2. Display all names that occur more than once.
3. If no duplicate names exist, report `"No duplicate names exist."`
4. Program must take input from the user where names are separated by commas.

---

## 2. Algorithm & Pseudocode

### 2.1 String Comparison Algorithm (`CustomCompare`)

To ensure natural dictionary ordering across different capitalizations (e.g. grouping `"amit"` and `"Amit"` together before `"Neha"` and `"rahul"` / `"Rahul"`), we implement a **two-tier comparison**:
1. **Primary Tier (Case-Insensitive Alphabetical)**: Compare characters after converting to lowercase (`ord(char.lower())`).
2. **Prefix Tier**: Shorter strings precede longer strings with identical prefixes.
3. **Secondary Tier (Case Tie-Breaking)**: When strings are case-insensitively identical, lowercase characters precede uppercase characters deterministically.

```text
ALGORITHM CustomCompare(s1, s2):
    len1 ← Length(s1)
    len2 ← Length(s2)
    minLen ← Min(len1, len2)

    // Primary Tier: Case-insensitive alphabetical comparison
    FOR i ← 0 TO minLen - 1 DO:
        c1 ← ToLower(s1[i])
        c2 ← ToLower(s2[i])
        IF ASCII(c1) < ASCII(c2) THEN
            RETURN -1
        ELSE IF ASCII(c1) > ASCII(c2) THEN
            RETURN 1
    
    // Prefix Tier: Shorter prefix precedes longer string
    IF len1 < len2 THEN
        RETURN -1
    ELSE IF len1 > len2 THEN
        RETURN 1
    
    // Secondary Tier: Deterministic case tie-breaking (lowercase precedes uppercase)
    FOR i ← 0 TO minLen - 1 DO:
        IF s1[i] != s2[i] THEN
            IF IsLower(s1[i]) AND IsUpper(s2[i]) THEN
                RETURN -1
            ELSE IF IsUpper(s1[i]) AND IsLower(s2[i]) THEN
                RETURN 1
            ELSE IF ASCII(s1[i]) < ASCII(s2[i]) THEN
                RETURN -1
            ELSE
                RETURN 1

    RETURN 0
```

### 2.2 Custom Merge Sort Algorithm (`MergeSort` & `Merge`)

We use **Merge Sort** (Divide and Conquer), which provides guaranteed $O(n \log n)$ time complexity in all cases.

```text
ALGORITHM MergeSort(arr):
    n ← Length(arr)
    IF n <= 1 THEN
        RETURN arr
    
    mid ← n // 2
    leftHalf ← MergeSort(arr[0 ... mid - 1])
    rightHalf ← MergeSort(arr[mid ... n - 1])
    
    RETURN Merge(leftHalf, rightHalf)


ALGORITHM Merge(left, right):
    result ← empty list
    i ← 0, j ← 0
    lenLeft ← Length(left), lenRight ← Length(right)

    WHILE i < lenLeft AND j < lenRight DO:
        cmp ← CustomCompare(left[i], right[j])
        IF cmp <= 0 THEN
            Append left[i] to result
            i ← i + 1
        ELSE
            Append right[j] to result
            j ← j + 1
    
    WHILE i < lenLeft DO:
        Append left[i] to result
        i ← i + 1
    
    WHILE j < lenRight DO:
        Append right[j] to result
        j ← j + 1
        
    RETURN result
```

### 2.3 Duplicate Detection Algorithm (`FindDuplicates`)

On the sorted array, duplicate names appear in contiguous clusters. We identify duplicates in a single linear scan ($O(n)$ time).

```text
ALGORITHM FindDuplicates(sortedArr):
    duplicates ← empty list
    n ← Length(sortedArr)
    i ← 0

    WHILE i < n DO:
        count ← 1
        WHILE i + 1 < n AND CustomCompare(sortedArr[i], sortedArr[i + 1]) == 0 DO:
            count ← count + 1
            i ← i + 1
        
        IF count > 1 THEN
            Append (sortedArr[i], count) to duplicates
        
        i ← i + 1

    RETURN duplicates
```

---

## 3. Case Sensitivity & Character Comparison Definition

The character comparison is formally defined as a **Two-Tier Natural Lexicographical Order**:

1. **Primary Alphabetical Order (Case-Insensitive)**:
   - Letters are mapped by their alphabetical position:
     `'a'` / `'A'` (rank 1) $<$ `'b'` / `'B'` (rank 2) $<$ ... $<$ `'z'` / `'Z'` (rank 26).
   - This ensures that names starting with `'A'` or `'a'` are grouped before names starting with `'N'` or `'n'`, which in turn are grouped before `'R'` or `'r'`.
2. **Prefix Comparison**:
   - If two strings match across all characters up to the shorter string's length, the shorter string is strictly smaller.
   - Example: `"Amit"` $<$ `"Amita"`.
3. **Secondary Case Tie-Breaking**:
   - If two words are alphabetically identical across all positions (e.g., `"amit"` vs `"Amit"`), lowercase letters are deterministically placed before uppercase letters.
   - Example: `"amit"` $<$ `"Amit"`, `"rahul"` $<$ `"Rahul"`.
4. **Exact Duplicate Equality**:
   - Two tokens are exact duplicates if and only if every character and its casing match completely (`CustomCompare` returns 0).
   - Example: `"Neha"` and `"Neha"` $\rightarrow$ duplicate count = 2.

---

## 4. Complexity Analysis

Let:
- $n = \text{number of employee names}$
- $L = \text{maximum length of an employee name string}$

### 4.1 Time Complexity

Each comparison between two strings takes at most $O(L)$ time.

1. **Best-Case Time Complexity**:
   - Merge Sort divides the problem into subproblems of size $n/2$ at each level, producing a recurrence relation:
     $$T(n) = 2T(n/2) + O(n \cdot L)$$
   - Solving via Master Theorem ($a = 2, b = 2, f(n) = O(n)$) yields:
     $$T_{\text{best}}(n) = O(n \cdot L \log n)$$

2. **Average-Case Time Complexity**:
   - For arbitrary permutations of input names, recursion tree depth is $\lceil \log_2 n \rceil$ with $O(n \cdot L)$ work per level:
     $$T_{\text{avg}}(n) = O(n \cdot L \log n)$$

3. **Worst-Case Time Complexity**:
   - Unlike Quick Sort (which can degrade to $O(n^2)$), Merge Sort guarantees balanced subproblems at all levels regardless of initial ordering or duplicate distribution:
     $$T_{\text{worst}}(n) = O(n \cdot L \log n)$$

4. **Duplicate Detection Time**:
   - Single linear scan over sorted array: performs $n - 1$ string comparisons of cost $O(L)$:
     $$T_{\text{dup}}(n) = O(n \cdot L)$$

5. **Overall Time Complexity**:
   $$\mathbf{O(n \cdot L \log n)}$$

### 4.2 Auxiliary Space Complexity

- **Merge Operation**: At each step of merging, auxiliary arrays are allocated of size proportional to the subproblem size, totaling $O(n \cdot L)$ space at any level of recursion.
- **Call Stack Depth**: The recursion tree depth is $O(\log n)$.
- **Duplicate List Storage**: Storing $k$ distinct duplicates requires $O(k \cdot L)$ space where $k \le n/2$.
- **Total Auxiliary Space**:
  $$\mathbf{O(n \cdot L)}$$

---

## 5. Duplicate Detection Without Sorting (Comparison & Discussion)

Can duplicate detection be performed without sorting the array? **Yes**. Below is a comparison of different approaches:

| Approach | Time Complexity (Average) | Time Complexity (Worst) | Auxiliary Space | Preserves Lexicographical Order? | Requires Sorting? |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **1. Custom Sort + Linear Scan (Chosen)** | $O(n \cdot L \log n)$ | $O(n \cdot L \log n)$ | $O(n \cdot L)$ | **Yes** | **Yes** |
| **2. Brute Force (Nested Loops)** | $O(n^2 \cdot L)$ | $O(n^2 \cdot L)$ | $O(1)$ (in-place flags) | **No** | **No** |
| **3. Hash Table / Frequency Map** | $O(n \cdot L)$ | $O(n^2 \cdot L)$ | $O(n \cdot L)$ | **No** | **No** |
| **4. Trie (Prefix Tree)** | $O(n \cdot L)$ | $O(n \cdot L)$ | $O(\Sigma \cdot n \cdot L)$ | **Yes** (via in-order traversal) | **No** (implicit) |

### Detailed Evaluation:
1. **Brute Force ($O(n^2 \cdot L)$ time, $O(1)$ space)**:
   - For every element $i$, iterate over all elements $j > i$ to check for equality.
   - Requires no extra space, but becomes prohibitively slow as $n$ grows.
2. **Hash Table ($O(n \cdot L)$ time, $O(n \cdot L)$ space)**:
   - Faster than sorting for pure duplicate detection because each insertion/lookup takes $O(L)$ on average.
   - However, a hash table **does not arrange the names in lexicographical order**, meaning a separate sorting step would still be mandatory to fulfill the problem requirements.
3. **Trie Structure ($O(n \cdot L)$ time, $O(\Sigma \cdot n \cdot L)$ space)**:
   - Stores character nodes; each leaf maintains frequency count.
   - An in-order traversal yields lexicographically sorted output with counts in $O(n \cdot L)$ time, but incurs significant pointer overhead and memory consumption.
4. **Conclusion**:
   - Combining **custom Merge Sort with a linear duplicate scan** optimally solves **both** requirements (lexicographical sorting and duplicate detection) simultaneously within $O(n \cdot L \log n)$ time and $O(n \cdot L)$ auxiliary space.

---

## 6. Representative Test Cases & Boundary Cases

### Test Case 1: Natural Dictionary Ordering with Mixed Cases
- **Input**: `amit, Amit, Rahul, Neha, rahul, Neha`
- **Sorted Output**: `amit, Amit, Neha, Neha, rahul, Rahul`
- **Duplicate Report**:
  - `'Neha'` appears 2 times

### Test Case 2: Multiple Duplicates (Lab Sheet Example)
- **Input**: `Amit, Neha, Amit, Rahul, Neha, Karan, Rahul`
- **Sorted Output**: `Amit, Amit, Karan, Neha, Neha, Rahul, Rahul`
- **Duplicate Report**:
  - `'Amit'` appears 2 times
  - `'Neha'` appears 2 times
  - `'Rahul'` appears 2 times

### Test Case 3: No Duplicates (All Unique)
- **Input**: `Amit, Karan, Neha, Rahul, Priya`
- **Sorted Output**: `Amit, Karan, Neha, Priya, Rahul`
- **Duplicate Report**: `No duplicate names exist.`

### Test Case 4: All Elements Identical
- **Input**: `Amit, Amit, Amit, Amit`
- **Sorted Output**: `Amit, Amit, Amit, Amit`
- **Duplicate Report**: `'Amit'` appears 4 times

### Test Case 5: Single Name (Boundary Case)
- **Input**: `Karan`
- **Sorted Output**: `Karan`
- **Duplicate Report**: `No duplicate names exist.`

### Test Case 6: Empty Input (Boundary Case)
- **Input**: `""` or `"  ,  ,  "`
- **Result**: Gracefully reports empty list; no crashes.
