

def max_subarray(nums: list) -> int:
    max_sum = float('-inf')
    current_sum = 0

    for num in nums:
        current_sum += num

        if current_sum > max_sum:
            max_sum = current_sum
        
        if current_sum < 0:
            current_sum = 0
    return max_sum

tests = [
    ([2, -3, 4, -2, 2, 1, -1, 4], 8),
    ([-2,1,-3,4,-1,2,1,-5,4], 6),
    ([5,4,-1,7,8], 23),
    ([-1], -1)
]


for idx, t in enumerate(tests):
    res = max_subarray(t[0])
    print(idx, " ", "Test passed" if res == t[1] else "Test Failed")