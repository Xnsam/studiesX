
def binary_search(nums: int, target: int) -> int:
    l = 0
    r = len(nums) - 1
    
    while l <= r:
        m = l + ((r - l) // 2)

        if target > nums[m]:
            l = m + 1
        elif target < nums[m]:
            r = m - 1
        else:
            return m
    
    return -1


tests = [
    ([-1,0,2,4,6,8], 6, 4),
    ([-1,0,2,4,6,8,9, 10, 11], 9, 6)
]


for idx, t in enumerate(tests):
    res = binary_search(t[0], t[1])
    print(idx, " ", "Test passed" if res == t[2] else "Test Failed")