## Context

See `proposal.md`. In standard English dictionary ordering for names, alphabetical ordering considers letters irrespective of case as primary comparison (`'a'`/`'A'` $<$ `'b'`/`'B'` ... $<$ `'n'`/`'N'` ... $<$ `'r'`/`'R'`). When names differ only in casing (e.g. `"amit"` vs `"Amit"`), a deterministic secondary tie-breaking rule is applied so that words remain neatly organized.

## Goals / Non-Goals

**Goals:**
- Implement natural dictionary comparison (`compare_strings`) comparing characters case-insensitively first.
- Apply deterministic tie-breaking for case-identical strings (e.g. lowercase precedes uppercase, `"amit"` $<$ `"Amit"`).
- Maintain custom Merge Sort without built-in sorting functions.
- Maintain $O(n)$ duplicate detection on the sorted list.
- Update analysis documentation and test cases accordingly.

**Non-Goals:**
- Using built-in sort functions.

## Decisions

### 1. Two-Tier String Comparison
- **Primary Tier**: Convert characters to lowercase (`ord(c.lower())`) and compare.
  - Character `'a'`/`'A'` (value 97) is strictly smaller than `'b'`/`'B'` (value 98).
- **Prefix Tier**: If strings match across common length, shorter string precedes longer string.
- **Secondary Tier (Tie-Breaking)**: If strings match case-insensitively and have equal length:
  - Compare character cases: lowercase character precedes uppercase character (e.g., `'amit'` $<$ `'Amit'`).
  - If characters are identical, strings are equal (return 0).

### 2. Pseudocode

```text
ALGORITHM CustomCompare(s1, s2):
    len1 ← Length(s1), len2 ← Length(s2)
    minLen ← Min(len1, len2)

    // Primary Tier: Case-insensitive comparison
    FOR i ← 0 TO minLen - 1 DO:
        c1 ← ToLower(s1[i])
        c2 ← ToLower(s2[i])
        IF ASCII(c1) < ASCII(c2) THEN RETURN -1
        IF ASCII(c1) > ASCII(c2) THEN RETURN 1

    // Length check
    IF len1 < len2 THEN RETURN -1
    IF len1 > len2 THEN RETURN 1

    // Secondary Tier: Case tie-breaking (lowercase precedes uppercase)
    FOR i ← 0 TO minLen - 1 DO:
        IF s1[i] != s2[i] THEN
            IF IsLower(s1[i]) AND IsUpper(s2[i]) THEN RETURN -1
            IF IsUpper(s1[i]) AND IsLower(s2[i]) THEN RETURN 1

    RETURN 0
```

## Risks / Trade-offs

- **[Case Sensitivity Definition]** → Mitigation: Explicitly document the two-tier comparison in `problem1_analysis.md` answering point (b) of Problem 1.
