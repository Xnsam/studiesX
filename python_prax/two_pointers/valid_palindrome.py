

def is_valid_palindrome(xstr: str) -> bool:
    l, r = 0, len(xstr) - 1
    xstr = xstr.lower()

    while l < r:
        if not xstr[l].isalpha():
            l += 1
        if not xstr[r].isalpha():
            r -= 1
        
        if xstr[l] != xstr[r]:
            return False
        
        l, r = l + 1, r - 1
    return True


tests = [
    ("tab a cat", False),
    ("Was it a car or a cat I saw?", True)
]

for idx, t in enumerate(tests):
    res = is_valid_palindrome(t[0])
    print(idx, " ", "Test passed" if res == t[1] else "Test Failed")