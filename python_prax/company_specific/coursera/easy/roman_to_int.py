

def roman_to_int(s: str) -> int:
    roman = {
            "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000
    }

    res = 0

    for i in range(len(s)):
        if i + 1 < len(s) and roman[s[i]] < roman[s[i+1]]:
            res -= roman[s[i]]
        else:
            res += roman[s[i]]

    return res

tests = [
    ("III", 3),
    ("XLIX", 49)
]


for idx, t in enumerate(tests):
    res = roman_to_int(t[0])
    print(idx, " ", "Test passed" if res == t[1] else "Test Failed")