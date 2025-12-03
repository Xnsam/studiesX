
def is_valid_anagram(s:str, t:str) -> bool:
    s_map = {}
    t_map = {}

    if len(s) != len(t):
        return False
    
    for idx in range(len(s)):
        cos = s[idx]
        cot = t[idx]

        s_map[cos] = s_map.get(cos, 0) + 1
        t_map[cot] = t_map.get(cot, 0) + 1

    return s_map == t_map




tests = [
    (["anagram", "nagaram"], True),
    (["car", "rat"], False)
]


for idx, t in enumerate(tests):
    res = is_valid_anagram(t[0][0], t[0][1])
    print(idx, " ", "Test passed" if res == t[1] else "Test Failed")