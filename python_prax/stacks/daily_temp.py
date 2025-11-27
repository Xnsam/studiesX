
def daily_temp(temps: list) -> list:
    days = [0] * len(temps)
    stack = []

    for i, t in enumerate(temps):
        while stack and t > stack[-1][0]:
            prev_t, prev_i = stack.pop()
            days[prev_i] = i - prev_i # current day - prev day
        stack.append((t, i))
    return days

tests = [
    ([30,38,30,36,35,40,28], [1,4,1,2,1,0,0])
]


for idx, t in enumerate(tests):
    res = daily_temp(t[0])
    print(idx, " ", "Test passed" if res == t[1] else "Test Failed")