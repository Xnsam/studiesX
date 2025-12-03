
def count_bits1(n: int) -> list:
    
    def count1(n: int) -> int:
        res = 0
        while n:
            n &= n - 1
            res += 1
        return res
    
    res = []
    for i in range(0, n + 1):
        res.append(count1(i))
    
    return res

def count_bits(n: int) -> list:
    dp = [0] * (n + 1)
    for i in range(n + 1):
        dp[i] = dp[i >> 1] + (i & 1)
    return dp


tests = [
    (2, [0, 1, 1]), 
    (5, [0, 1, 1, 2, 1, 2])
]


for idx, t in enumerate(tests):
    res = count_bits1(t[0])
    print(idx, " ", "Test passed" if res == t[1] else "Test Failed")