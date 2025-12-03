
def count_pali(s: str, l: int, r: int) -> int:
    res = 0
    while l >= 0 and res < len(s) and s[l] == s[r]:
        res += 1
        l -= 1
        r += 1
    return res

def count_subarrays(s: str) -> int:
    res = 0

    for i in range(len(s)):
        res += count_pali(s, i, i)
        res += count_pali(s, i, i + 1)
    return res


tests = [
    ("abc", 3),
    ("aaa", 6),  
]


for idx, t in enumerate(tests):
    res =  count_subarrays(t[0])
    print(idx, " ", "Test passed" if res == t[1] else "Test Failed")