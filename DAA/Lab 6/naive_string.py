from re import PatternError


def naive_search(text, pattern):
    n = len(text)
    m = len(pattern)

    for i in range(n-m):
        j = 0
        while j < m and text[i+j] == pattern[j]:
            j += 1

        if j == m:
            print("pattern found at index" , i)


text = "AABAACAADAABAABA"
pattern = "AABA"

naive_search(text, pattern)
