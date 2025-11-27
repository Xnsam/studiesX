


def top_k_freq(nums: list, k: int) -> list:
    
    freq_map = {}

    for num in nums: # O(n)
        if num in freq_map:
            freq_map[num] += 1
        else:
            freq_map[num] = 1
    
    sorted_map = sorted(freq_map.items(), key=lambda items: items[1], reverse=True) # O(N log N), O(N)
    sorted_map = dict(sorted_map)
    top_k = list(sorted_map.keys())[:k]
    return top_k


def top_k_freq_bucket(nums: list, k: int) -> list:
    count = {}
    freq = [[] for i in range(len(nums) + 1)]

    for num in nums:
        count[num] = 1 + count.get(num, 0)
    for num, cnt in count.items():
        freq[cnt].append(num)

    res = []
    for i in range(len(freq) - 1, 0, -1):
        for num in freq[i]:
            res.append(num)
            if len(res) == k:
                return res
            

def top_k_test(nums: list[int], k: int) -> list:
    count = {}
    freq = [[] for i in range(len(nums) + 1)]

    for num in nums:
        count[num] = 1 + count.get(num, 0)
    
    for num, cnt in count.items():
        freq[cnt].append(num)
    
    res = []
    for i in range(len(freq) - 1, 0, -1):
        for num in freq[i]:
            res.append(num)
            if len(res) == k:
                return res


tests = [
    ([1,2,2,3,3,3], 2, [3, 2]),
    ([7, 7], 1, [7]),
    ([8, -1, 0, -2, 1, 8], 1, [8])
]

for idx, t in enumerate(tests):
    res = top_k_test(t[0], t[1])
    print(res)
    print(idx, " ", res == t[2])