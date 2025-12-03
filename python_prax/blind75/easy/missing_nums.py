


def find_missing(nums: list) -> int:
    num_set = set(nums)
    for i in range(0, len(nums) + 1):
        if i not in num_set:
            return i 


tests = [
    ([3,0,1], 2),
    ([0, 1], 2),
    ([9,6,4,2,3,5,7,0,1], 8)
]


for idx, t in enumerate(tests):
    res = find_missing(t[0])
    print(idx, " ", "Test passed" if res == t[1] else "Test Failed")