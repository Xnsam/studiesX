
def prod_self(nums: list[int]) -> list[int]:
    import math

    res = [0] * len(nums)
    for idx, v in enumerate(nums):
        nums[idx] = 1
        res[idx] = math.prod(nums)
        nums[idx] = v
    
    return res


tests = [
    ([1,2,4,6], [48,24,12,8]),
    ([-1,0,1,2,3], [0,-6,0,0,0])
]

for idx, t in enumerate(tests):
    res = prod_self(t[0])
    print(idx, " ", res == t[1])