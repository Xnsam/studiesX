
def lcq(nums: int) -> int:
    
    set_nums = set(nums) # puts it in order, another form of sorting
    longest = 0

    for num in set_nums:
        if num - 1 not in set_nums:
            length = 0
            while num + length in set_nums:
                length += 1
            longest = max(length, longest)
    return longest



tests = [
    ([2,20,4,10,3,4,5], 4),
    ([0,3,2,5,4,6,1,1], 7)
]

for idx, t in enumerate(tests):
    res = lcq(t[0])
    print(idx, " ", res == t[1])