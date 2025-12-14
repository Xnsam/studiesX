

def min_rotated_array(nums: list) -> int:
    l, r = 0, len(nums) - 1

    while l < r:
        m = l + ((r - l) // 2)

        if nums[m] > nums[r]:
            l = m + 1
        else:
            r = m
    
    return nums[l]

tests = [
    ([3,4,5,1,2], 1),
    ([4,5,6,7,0,1,2], 0),
    ([11,13,15,17], 11)
]


for idx, t in enumerate(tests):
    res = min_rotated_array(t[0])
    print(idx, " ", "Test passed" if res == t[1] else "Test Failed")