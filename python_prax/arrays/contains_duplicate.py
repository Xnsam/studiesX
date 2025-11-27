

def contains_duplicate(nums: list[int]) -> bool:
    return len(set(nums)) != len(nums)

def contains_duplicates(nums: list[int]) -> bool:
    is_visited = tuple()

    for n in nums:
        if n in is_visited:
            return True
    return False

tests = [
    ([1, 2, 3, 3, 4], True),
    ([0, 1, -1, 2, -4, 3], False),
    ([5, 5, 5, 5, 5], True)
]

for idx, t in enumerate(tests):
    res = contains_duplicate(t[0])
    print(idx, " ", res == t[1])