from collections import defaultdict

def is_valid_sudoku(board: list) -> bool:
    rows = defaultdict(set)
    cols = defaultdict(set)
    squares = defaultdict(set)

    for r in range(9):
        for c in range(9):

            cell_value = board[r][c]

            if cell_value == ".":
                continue

            if cell_value in rows[r] or cell_value in cols[c] or cell_value in squares[(r//3, c//3)]:
                return False
            
            rows[r].add(cell_value)
            cols[c].add(cell_value)
            squares[(r//3, c//3)].add(cell_value)
    
    return True



board1 = [["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]

board2 = [["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","1",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]

tests = [
    (board1, True),
    (board2, False)
]

for idx, t in enumerate(tests):
    res = is_valid_sudoku(t[0])
    print(idx, " ", res == t[1])