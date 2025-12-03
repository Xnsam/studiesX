


def min_moves(nums: list) -> int:
    nums.sort() # assumption 
    # [1, 2, 3]

    cum = 0
    while nums:
        cum = cum + (nums[-1] + cum) - (nums[0] + cum)
        # cum = 0 + (3 + 0) - (1 + 0) = 0 + 3 - 1 = 2
        # cum = 2 + (2 + 2) - (1 + 2) = 2 + 4 - 3 = 3
        # cum = 3 + (1 + 3) - (1 + 3) = 3 + 4 - 4 = 3

        nums.pop()
        # 3, [1, 2]
        # 2, [1]
    return cum


tests = [
    ([1, 2, 3], 3),
    ([1, 1, 1], 0)
]


for idx, t in enumerate(tests):
    res = min_moves(t[0])
    print(idx, " ", "Test passed" if res == t[1] else "Test Failed")