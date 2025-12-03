

def subarray_productk(nums: list, k: int) -> int:
    l = 0
    res = 0
    product = 1

    for r in range(len(nums)):
        product *= nums[r]
        while l <= r and product >= k:
            product //= nums[l]
            l += 1
        res += (r - l + 1)
    
    return res



tests = [
    ([10,5,2,6], 100, 8),
    ([1, 2, 3], 0, 0),
    ([1, 1, 1], 1, 0)
]


for idx, t in enumerate(tests):
    res =   subarray_productk(t[0], t[1])
    print(idx, " ", "Test passed" if res == t[2] else "Test Failed")