
def valid_paranthesis(s: str) -> bool:
    closed_open_map = {
        "}": "{",
        ")": "(",
        "]": "["
    }
    stack = []

    if not s:
        return False
    
    for i, c in enumerate(s):
        if i == 0 and c in closed_open_map:
            return False
        print(stack)
        print("-" * 10)
        if c in closed_open_map:
            if stack and stack[-1] == closed_open_map[c]:
                stack.pop()
            else:
                return False
        else:
            stack.append(c)
    
    return True if not stack else False


tests = [
    ("[]", True), 
    ("[]{}()", True),
    ("[{()}]", True), 
    ("[{}]([])", True),
    ("{}[(]", False),
    ("{({[)]", False),
    ("{{{{{{}}}}", False)
]


for idx, t in enumerate(tests):
    res = valid_paranthesis(t[0])
    print(idx, " ", "Test passed" if res == t[1] else "Test Failed")