
def three_sum(nums: list) -> int:
    res = []
    nums.sort()

    for i, a in enumerate(nums):
        if i > 0 and a == nums[i-1]:
            continue

        j, k = i + 1, len(nums) - 1
        while j < k:
            _sum = a + nums[j] + nums[k]
            if _sum > 0:
                k -= 1
            elif _sum < 0:
                j += 1
            else:
                res.append([a, nums[j], nums[k]])
                j += 1

                while nums[j] == nums[j - 1] and j < k:
                    j += 1
        return res



tests = [
    ([-1,0,1,2,-1,-4], [[-1,-1,2],[-1,0,1]]),
    ([0, 1, 1], []),
    ([0, 0, 0], [0, 0, 0])
]


for idx, t in enumerate(tests):
    res =  three_sum(t[0], t[1])
    print(idx, " ", "Test passed" if res == t[2] else "Test Failed")