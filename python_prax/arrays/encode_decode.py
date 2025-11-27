# def encode(strs: list[str]) -> str:
#     res = ""
#     for s in strs:
#         res += str(len(s)) + "#" + s
#     return res

# def decode(s: str) -> list:
#     res, i = [], 0

#     while i < len(s):
#         j = i
#         while s[j] != "#":
#             j += 1
        
#         length = int(s[i:j])
#         res.append(s[j + 1 : j + 1 + length])
#         i = j + 1 + length
    
#     return res





def encode(strs: list) -> str:
    res = ""
    for s in strs:
        res += str(len(s)) + "#" + s
    return res

def decode(s: str) -> list:
    res = []
    i = 0

    while i < len(s):
        j = i
        while s[j] != "#":
            j += 1
        
        length = int(s[i:j])
        str_data = s[j + 1: j + 1 + length]
        res.append(str_data)
        i = j + 1 + length
    
    return res


input_s = ["neet","code","love","you"]

print(encode(input_s))
print(decode(encode(input_s)))