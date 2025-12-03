def two_sum(nums: list, target: int) -> list:
    
    diff_map = {}
    for idx, num in enumerate(nums):
        diff = target - num

        if diff in diff_map:
            return [diff_map[diff], idx]
        else:
            diff_map[num] = idx
    print(diff_map)
    return []


tests = [
    ([2,7,11,15], 9, [0, 1]),
    ([3,2,4], 6, [1, 2]),
    ([3, 3], 6, [0, 1]),
    ([-1, 0, 2, -5, 2], -6, [0, 3])
]


for idx, t in enumerate(tests):
    res = two_sum(t[0], t[1])
    print(idx, " ", "Test passed" if res == t[2] else "Test Failed")