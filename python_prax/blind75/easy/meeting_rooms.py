


def is_conflict(meetings: str) -> str:
    meetings.sort(key=lambda x: x[0])

    for i in range(1, len(meetings)):
        m = meetings[i-1]
        n = meetings[i]

        if m[1] > n[0]:
            return False

    return True


tests = [
    ([(0,30),(5,10),(15,20)], False),
    ([(5,8),(9,15)], True)
]


for idx, t in enumerate(tests):
    res = is_conflict(t[0])
    print(idx, " ", "Test passed" if res == t[1] else "Test Failed")