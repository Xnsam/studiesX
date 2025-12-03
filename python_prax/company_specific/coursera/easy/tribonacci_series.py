
dp = {}

def tribonnaci_series(n: int) -> int:
    if n <= 2:
        return 1 if n!= 0 else 0
    
    elif n in dp:
        return dp[n]
    
    else:
        dp[n] = tribonnaci_series(n - 1) + tribonnaci_series(n - 2) + tribonnaci_series(n - 3)
    
    return dp[n]


tests = [
    (3, 2),
    (21, 121415)
]


for idx, t in enumerate(tests):
    res = tribonnaci_series(t[0])
    print(idx, " ", "Test passed" if res == t[1] else "Test Failed")




