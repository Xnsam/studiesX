

def rotated_search(nums: int) -> int:
    res = nums[0]
    l, r = 0, len(nums) - 1

    while l <= r:
        if nums[l] < nums[r]:
            res = min(res, nums[l])
            break

        m = (r + l) // 2
        res = min(res, nums[m])
        if nums[m] >= nums[l]:
            l = m + 1
        else:
            r = m - 1
    return res

tests = [
    ([3,4,5,6,1,2], 1),
    ([3,5,6,0,1,2], 0)
]


for idx, t in enumerate(tests):
    res = rotated_search(t[0])
    print(idx, " ", "Test passed" if res == t[1] else "Test Failed")