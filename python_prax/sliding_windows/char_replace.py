
def char_replace(xstr: str, k: int) -> int:
    count = {}
    res = 0
    l = 0
    maxf = 0

    for r in range(len(xstr)):
        count[xstr[r]] = 1 + count.get(xstr[r], 0)
        maxf = max(maxf, count[xstr[r]])

        # to check if the window is valid or not
        # the window should be valid if the number of replacements in the window 
        # is less than equal to the allowed replacement
        while (r - l + 1) - maxf > k:
            count[xstr[l]] -= 1
            l += 1
        
        res = max(res, r - l + 1)
    return res


tests = [
    ("XYYX", 2, 4),
    ("AAABABB", 1, 5)
]

for idx, t in enumerate(tests):
    res = char_replace(t[0], t[1])
    print(idx, " ", res == t[2])