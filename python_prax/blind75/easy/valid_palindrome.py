
def is_valid_palindrome(t: str):
    if t == "":
        return False
    
    if t == " ":
        return True
    
    l = 0
    r = len(t) - 1

    t = t.lower()
    while l < r:
        if not t[l].isalnum():
            l += 1
        if not t[r].isalnum():
            r -= 1
        if t[l] != t[r]:
            return False
        l, r = l + 1, r - 1
    return True



tests = [
    ("A man, a plan, a canal: Panama", False),
    ("race a car", False),
    (" ", True)
]


for idx, t in enumerate(tests):
    res = is_valid_palindrome(t[0])
    print(idx, " ", "Test passed" if res == t[1] else "Test Failed")