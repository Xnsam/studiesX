
def num_car_fleet(positions: list, speeds: list, target: int) -> int:
    pairs = [[p, s] for p, s in zip(positions, speeds)]
    stack = []
    sorted_pairs = sorted(pairs, reverse=True)
    for p, s in sorted_pairs:
        stack.append((target - p) / s)
        if len(stack) >= 2 and stack[-1] <= stack[-2]:
            stack.pop()
        print(stack)
        print("-" * 10)
    return len(stack)

tests = [
    ([1, 4], [3, 2], 10, 1),
    ([4, 1, 0, 7], [2, 2, 1, 1], 10, 3)
]


for idx, t in enumerate(tests):
    res = num_car_fleet(t[0], t[1], t[2])
    print(idx, " ", "Test passed" if res == t[3] else "Test Failed")
