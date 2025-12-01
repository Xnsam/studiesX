
def search_matrix(matrix: list, target: int) -> int:
    ROWS, COLS = len(matrix), len(matrix[0])

    l, r = 0, ROWS * COLS - 1
    while l <= r:
        m = l + (r - l) // 2
        row, col = m // COLS, m % COLS

        if target > matrix[row][col]:
            l = m + 1
        elif target < matrix[row][col]:
            r = m - 1
        else:
            return True
    return False


tests = [
    ([[1,2,4,8],[10,11,12,13],[14,20,30,40]], 10, True),
    ([[1,2,4,8],[10,11,12,13],[14,20,30,40]], 15, False)
]


for idx, t in enumerate(tests):
    res = search_matrix(t[0], t[1])
    print(idx, " ", "Test passed" if res == t[2] else "Test Failed")