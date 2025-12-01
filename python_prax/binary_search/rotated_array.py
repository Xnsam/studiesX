

def rotated_search(nums: list, target: int) -> int:
    """
    init l, r = 0, len(nums) - 1

    calculate the midpoint
    if target == nums[m]:
        return m
    
    check if nums[l] <= mid:
        if target > nums[mid] or target < nums[l]:
        l = mid + 1
        else
        r = mid - 1
    else:
        if target < nums[mid] or target > nums[r]:
        r = mid + 1
        else
        l = mid - 1
    
    return the default value -1
    """
    l, r = 0, len(nums) - 1
    while l <= r:
        m = (r + l) // 2

        if target == nums[m]:
            return m
        
        if nums[l] <= nums[m]:
            if target > nums[m] or target < nums[l]:
                l = m + 1
            else:
                r = m - 1
        else:
            if target < nums[m] or target > nums[r]:
                r = m - 1
            else:
                l = m + 1
    return -1


tests = [
    ([3,4,5,6,1,2], 1, 4),
    ([3,5,6,0,1,2], 4, -1)
]


for idx, t in enumerate(tests):
    res = rotated_search(t[0], t[1])
    print(idx, " ", "Test passed" if res == t[2] else "Test Failed")