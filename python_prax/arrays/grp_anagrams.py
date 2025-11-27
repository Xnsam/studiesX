

def grp_anagrams(strs: list[str]) -> list[list]:
    res = {}
    for s in strs:
        s = s.lower()
        char_set = ["0"] * 26
        for c in s:
            char_set[ord(c) - 97] = "1"
        
        char_set = "".join(char_set)
        if char_set in res:
            res[char_set].append(s)
        else:
            res[char_set] = [s]

    return list(res.values())


tests = [
    (["act","pots","tops","cat","stop","hat"], [["hat"],["act", "cat"],["stop", "pots", "tops"]]),
    (["x"], [["x"]]),
    ([""], [[""]])
]

for idx, t in enumerate(tests):
    res = grp_anagrams(t[0])
    print(res)
    print(idx, " ", res == t[1])