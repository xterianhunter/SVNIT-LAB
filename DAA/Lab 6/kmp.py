def kmp_search(text, pattern):
    n = len(text)
    m = len(pattern)

    lps = [0]* m
    j= 0

    for i in range(1,m):
        while j > 0 and pattern[i] != pattern[j]:
            j = lps[j-1]

        if pattern[i] == pattern[j]:
            j += 1
        lps[i] = j

    i = 0
    j = 0

    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1

        if j == m:
            print("Pattern found at index", i-j)
            j= lps[j-1]


        elif i<n and text[i] != pattern[j]:
            if j > 0:
                j = lps[j - 1]
            else:
                i += 1

text = "AABAACAADAABAABA"
pattern = "AABA"

kmp_search(text, pattern)


