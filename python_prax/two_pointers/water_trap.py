

def max_water_trap(nums: int) -> int:
    if not nums:
        return 0
    
    l, r = 0, len(nums) - 1
    left_max, right_max = nums[l], nums[r]
    res = 0
    while l < r:
        print(l, r)
        print(left_max, right_max)
        print('-'*10)
        if left_max < right_max:
            l += 1
            left_max = max(left_max, nums[l])
            res += left_max - nums[l]
            print("left_max < right_max")
            print(left_max, right_max, res, nums[l])
            print('=' * 10)
        else:
            r -= 1
            right_max = max(right_max, nums[r])
            res += right_max - nums[r]
            print("left_max > right_max")
            print(left_max, right_max, res, nums[r])
            print('=' * 10)
    return res


tests = [
    ([0,2,0,3,1,0,1,3,2,1], 9)
]


for idx, t in enumerate(tests):
    res = max_water_trap(t[0])
    print(idx, " ", "Test passed" if res == t[1] else "Test Failed")