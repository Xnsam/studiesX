
def max_prod_subarray(nums: list) -> int:
    max_prod = nums[0]
    min_prod = nums[0]
    global_max = nums[0]

    for i in range(1, len(nums)):
        current = nums[i]

        calc = (current, current * max_prod, current * min_prod)
        temp_max, min_prod = max(calc) , min(calc)

        max_prod = temp_max
        global_max = max(global_max, max_prod)
    return global_max



tests = [
    ([2,3,-2,4], 6),
    ([-2,0,-1], 0),
    ([-1], -1)
]


for idx, t in enumerate(tests):
    res = max_prod_subarray(t[0])
    print(idx, " ", "Test passed" if res == t[1] else "Test Failed")