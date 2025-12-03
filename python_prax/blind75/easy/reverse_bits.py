

def reverse_bits(num: int) -> int:
    res = 0

    for i in range(32):
        bit = (num >> i) & 1
        res = res + (bit << (31 - i))
    
    return res

tests = [
    (43261596, 964176192),
    (2147483644, 1073741822)
]


for idx, t in enumerate(tests):
    res = reverse_bits(t[0])
    print(idx, " ", "Test passed" if res == t[1] else "Test Failed")