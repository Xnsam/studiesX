

def three_sum(nums: int) -> list:
    res = []
    nums.sort()

    for i, a in enumerate(nums):
        # not consider the same integer as first int of 3sum
        if i > 0 and a == nums[i-1]:
            continue
        
        # two sum approach
        j, k = i + 1, len(nums) - 1
        while j < k:
            three_sum = a + nums[j] + nums[k]
            if three_sum > 0:
                k -= 1
            elif three_sum < 0:
                j += 1 
            else:
                res.append([a, nums[j], nums[k]])                
                # update the pointer
                j += 1 
                # two avoid duplicates in the subset
                while nums[j] == nums[j - 1] and j < k:
                    j += 1
    return res

tests = [
    ([-1,0,1,2,-1,-4], [[-1,-1,2],[-1,0,1]]),
]

for idx, t in enumerate(tests):
    res = three_sum(t[0])
    print(res)
    print(idx, " ", "Test passed" if res == t[1] else "Test Failed")