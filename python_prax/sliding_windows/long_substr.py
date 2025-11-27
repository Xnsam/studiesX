
def long_substr(s: str) -> int:
    l = 0
    max_s = 0
    substr = s[l]

    for r in range(1, len(s)):
        while s[r] in substr and l < r:
            l += 1
            substr = s[l:r]

        substr += s[r]
        max_s = max(max_s, len(substr))

    return max_s

tests = [
    ("zxyzxyz", 3),
    ("xxxx", 1)
]

for idx, t in enumerate(tests):
    res = long_substr(t[0])
    print(idx, " ", res == t[1])
