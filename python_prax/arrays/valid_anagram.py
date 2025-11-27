
def is_valid_anagram(s: str, t: str):
    char_set_t = [0] * 26
    char_set_s = [0] * 26

    if len(s) != len(t):
        return False
    
    for i in range(len(s)):
        char_set_s[ord(s[i]) - 97] = 1
        char_set_t[ord(t[i]) - 97] = 1
    
    return char_set_s == char_set_t



tests = [
    ("racecar", "carrace", True),
    ("jar", "jam", False),
    ("mom", "mom", True)
]

for idx, t in enumerate(tests):
    res = is_valid_anagram(t[0], t[1])
    print(idx, " ", res == t[2])