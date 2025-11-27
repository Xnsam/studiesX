


def two_sum(nums: list[int], target: int) -> list:
    target_diff = {}

    if not nums:
        return []

    for idx, num in enumerate(nums):
        if num in target_diff:
            return [target_diff[num], idx]
        else:
            diff = target - num
            target_diff[diff] = idx
    
    return []



tests = [
    ([3, 4, 5, 6], 7, [0, 1]),
    ([3, 4, 5, 6], 9, [1, 2]),
    ([-1, 0, -2, -3, 5], -4, [0, 3])
]

for idx, t in enumerate(tests):
    res = two_sum(t[0], t[1])
    print(res)
    print(idx, " ", res == t[2])