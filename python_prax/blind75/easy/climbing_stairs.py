import math

def climbing_stairs(n: int) -> int:
    sqrt5 = math.sqrt(5)
    phi = ( 1 + sqrt5) / 2 # golden ratio
    psi = (1 - sqrt5) / 2 # conjugate of golden ratio

    n += 1
    return round((phi ** n - psi ** n) / sqrt5 ) # direct way of getting a fibonacci series

tests = [
    (2, 2),
    (3, 3),
]


for idx, t in enumerate(tests):
    res = climbing_stairs(t[0])
    print(idx, " ", "Test passed" if res == t[1] else "Test Failed")