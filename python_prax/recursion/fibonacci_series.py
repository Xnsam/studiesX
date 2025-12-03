

def fibonacci_series(n: int) -> int:
    if n == 0:
        return 0
    
    elif n == 1:
        return 1
    
    else:
        return fibonacci_series(n - 1) + fibonacci_series(n - 2)

tests = [
    (0, 0), 
    (1, 1),
    (2, 1),
    (3, 2),
    (4, 3),
    (5, 5),
    (6, 8),
    (7, 13),
    (8, 21),
    (9, 34)
]


for idx, t in enumerate(tests):
    res = fibonacci_series(t[0])
    print(idx, " ", "Test passed" if res == t[1] else "Test Failed")




# for idx, t in enumerate(tests):
#     res = tribonnaci_series(t[0])
#     print(idx, " ", "Test passed" if res == t[1] else "Test Failed")



