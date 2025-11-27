from typing import Union

def rev_polish(tokens: list) -> Union[float, int]:
    stack = []

    for token in tokens:
        match token:
            case "+":
                a, b = stack.pop(), stack.pop()
                stack.append(a + b)
            case "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            case "*":
                a, b = stack.pop(), stack.pop()
                stack.append(a * b)
            case "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(float(b)/a))
            case _:
                stack.append(int(token))

    return int(stack[0])

tests = [
    (
        ["1","2","+","3","*","4","-"],
        5
    )
]


for idx, t in enumerate(tests):
    res = rev_polish(t[0])
    print(idx, " ", "Test passed" if res == t[1] else "Test Failed")