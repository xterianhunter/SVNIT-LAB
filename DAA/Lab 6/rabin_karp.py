def rabin_karp_search(text, pattern):
    n = len(text)
    m = len(pattern)

    d = 256
    q = 101

    pattern_hash = 0
    text_hash = 0
    h = 1

    for i in range(m-1):
        h = (h * d) % q
        print("h: ", h)
    print("H: ", h)

    for i in range(m):
        pattern_hash = (d * pattern_hash + ord(pattern[i])) % q
        text_hash = (d * text_hash + ord(text[i])) % q

        print("pattern_hash: ", pattern_hash)
        print("text_hash: ", text_hash)

text = "AABAACAADAABAABA"
pattern = "AABA"

rabin_karp_search(text, pattern)
