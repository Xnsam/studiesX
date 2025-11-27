
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.min_stack.append(
            min(val, self.min_stack[-1] if self.min_stack else val)
        )

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> None:
        return self.stack[-1]

    def getMin(self) -> None:
        return self.min_stack[-1]

def run_test(actions: list) -> list:

    min_stack_obj = None
    result = []
    for idx, action in enumerate(actions):
        match action:
            case "MinStack":
                min_stack_obj = MinStack()
                res = None
            case "push":
                res = min_stack_obj.push(actions[idx+1])
            case "pop":
                res = min_stack_obj.pop()
            case 'top':
                res = min_stack_obj.top()
            case 'getMin':
                res = min_stack_obj.getMin()
            
            case _:
                res = None
        
        result.append(res)
    return result


tests = [
    (
        ["MinStack", "push", 1, "push", 2, "push", 0, "getMin", "pop", "top", "getMin"], 
        [None, None, None, None, None, None, None, 0, None, 2, 1]
    )
]


for idx, t in enumerate(tests):
    res = run_test(t[0])
    print(idx, " ", "Test passed" if res == t[1] else "Test Failed")