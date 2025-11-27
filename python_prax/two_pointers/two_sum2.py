
def two_sum2(nums: int, target: int) -> list:
    l, r = 0, len(nums) - 1

    while l < r:
        if nums[l] + nums[r] > target:
            r -= 1
        elif nums[l] + nums[r] < target:
            l += 1
        elif nums[l] + nums[r] == target:
            return [l+1, r+1]
    
    return []


tests = [
    ([1, 2, 3, 4], 3, [1, 2]), 
    ([1, 2, 3, 4], 6, [2, 4])
]

for idx, t in enumerate(tests):
    res = two_sum2(t[0], t[1])
    print(idx, " ", "Test passed" if res == t[2] else "Test Failed")