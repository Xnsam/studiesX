
def prod_itself(nums: list) -> list:
    n = len(nums)
    suff = [0] * n
    pref = [0] * n
    res = [0] * n

    pref[0] = suff[n-1] = 1

    for i in range(1, n):
        pref[i] = nums[i - 1] * pref[i - 1]
    for i in range(n - 2, -1, -1):
        suff[i] = nums[i + 1] * suff[i+1]
    for i in range(n):
        res[i] = pref[i] * suff[i]
    
    return res

tests = [
    ([1,2,3,4], [24,12,8,6]),
    ([-1,1,0,-3,3], [0,0,9,0,0]),
    ([1,2,4,6], [48,24,12,8]),
    ([-1,0,1,2,3], [0,-6,0,0,0])
]


for idx, t in enumerate(tests):
    res = prod_itself(t[0])
    print(idx, " ", "Test passed" if res == t[1] else "Test Failed")