import math

def prax(n: int) -> int:
    sqrt5 = math.sqrt(5)
    phi = (1 + sqrt5) / 2
    psi = (1 - sqrt5) / 2

    n += 1
    return round((phi ** n - psi ** n) / sqrt5)


tests = [
    (2, 2),
    (3, 3)
]


for idx, t in enumerate(tests):
    res = prax(t[0])
    print(idx, " ", "Test passed" if res == t[1] else "Test Failed")