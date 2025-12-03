def contains_duplicate(nums: int) -> bool:
    
    is_visited = tuple()

    for n in nums:
        if n in is_visited:
            return  True
        else:
            is_visited += (n,)
    
    return False




tests = [
    ([1,2,3,1], True),
    ([1,2,3,4], False)
]


for idx, t in enumerate(tests):
    res = contains_duplicate(t[0])
    print(idx, " ", "Test passed" if res == t[1] else "Test Failed")