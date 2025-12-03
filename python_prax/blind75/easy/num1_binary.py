
def count1(num: int) -> int:
    bin_value = str(bin(num))

    count = 0
    for val in bin_value:
        if val == "1":
            count += 1
    return count

def count1(n: int) -> int:
    res = 0
    while n:
        n = n & n - 1
        res += 1
    return res


tests = [
    (3, 2),
    (128, 1),
    (2147483645, 30)
]


for idx, t in enumerate(tests):
    res = count1(t[0])
    print(idx, " ", "Test passed" if res == t[1] else "Test Failed")