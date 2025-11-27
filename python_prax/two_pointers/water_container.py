


def contains_max_water(nums: int) -> int:
    res = 0
    l, r = 0, len(nums) - 1

    while l < r:
        area = (r - l) * min(nums[l], nums[r])
        res = max(area, res)

        if nums[l] < nums[r]:
            l += 1
        else:
            r -= 1
    return res


tests = [
    ([1,7,2,5,4,7,3,6], 36),
    ([2,2,2], 4)
]


for idx, t in enumerate(tests):
    res = contains_max_water(t[0])
    print(idx, " ", "Test passed" if res == t[1] else "Test Failed")