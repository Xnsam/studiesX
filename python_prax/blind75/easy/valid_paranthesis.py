def valid_paranthesis(s: int) -> int: 
    stack = []
    close_open = {
        "}": "{",
        "]": "[",
        ")": "(" 
    }

    if s[0] in close_open:
        return False

    for c in s:
        if c in close_open:
            if stack and close_open[c] in stack:
                stack.pop()
        else:
            stack.append(c)
    
    return False if stack else True

tests = [
    ("()", True),
    ("()[]{}", True),
    ("(]", False),
    ("([])", True),
    ("([)]", False),
    ("((())", False)
]


for idx, t in enumerate(tests):
    res = valid_paranthesis(t[0])
    print(idx, " ", "Test passed" if res == t[1] else "Test Failed")