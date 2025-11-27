from collections import deque


def max_window(nums: list, k: int) -> list:
    max_vals = []
    i = 0

    while i + k <= len(nums):
        window = nums[i: i+k]
        max_vals.append(max(window))
        i += 1

    return max_vals


def max_window(nums: list, k: int) -> list:
    max_vals = []
    q = deque() # []
    l = r = 0
    breakpoint()
    while r < len(nums): 
        while q and nums[q[-1]] < nums[r]: # []; [0] & 1 < 2; [1] & 2 < 1
            q.pop() # [];
        q.append(r) # q = [0]; [1]; [1, 2]

        if l > q[0]: # 0 > 0; 0 > 1; 0 > 1
            q.popleft()
        
        if (r + 1) >= k: # 0 + 1 >= 3; 2 >= 3; 3 >= 3 
            max_vals.append(nums[q[0]]) # [2]
            l += 1
        r += 1 # r = 1; r = 2; r = 3;

    return max_vals


def max_window(nums: list, k: int) -> list:
    max_vals = []
    l = r = 0
    q = deque()

    while r < len(nums):

        while q and nums[q[-1]] < nums[r]:
            q.pop()
        q.append(r)

        if l > q[0]:
            q.popleft()
        
        if (r + 1) >= k:
            max_vals.append(nums[q[0]])
            l += 1
        r += 1

    return max_vals
        

tests = [
    ([1, 2, 1, 0, 4, 2, 6], 3, [2, 2, 4, 4, 6]),
    ([1, 2, 1, 0, 4, 2, 6], 2, [2, 2, 1, 4, 4, 6])
]

for idx, t in enumerate(tests):
    res = max_window(t[0], t[1])
    print(res)
    print(idx, " ", res == t[2])