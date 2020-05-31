from typing import List

def isValidSudoku(board: List[List[str]]) -> bool:
    rows = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: []}
    columns = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: []}

    for block_num in range(9):
        block = []
        for i in range(3):
            for j in range(3):
                row = (block_num // 3)*3 + i
                column = (block_num % 3) * 3 + j
                num = board[row][column]

                if num != '.':
                    if num in rows[row] or num in columns[column] or num in block:
                        return False
                    else:
                        rows[row].append(num)
                        columns[column].append(num)
                        block.append(num)

    return True

if __name__ == "__main__":
    print(isValidSudoku([
                          ["5","3",".",".","7",".",".",".","."],
                          ["6",".",".","1","9","5",".",".","."],
                          [".","9","8",".",".",".",".","6","."],
                          ["8",".",".",".","6",".",".",".","3"],
                          ["4",".",".","8",".","3",".",".","1"],
                          ["7",".",".",".","2",".",".",".","6"],
                          [".","6",".",".",".",".","2","8","."],
                          [".",".",".","4","1","9",".",".","5"],
                          [".",".",".",".","8",".",".","7","9"]
                        ]
    ))

    print(isValidSudoku([
                            ["8", "3", ".", ".", "7", ".", ".", ".", "."],
                            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                            [".", "9", "8", ".", ".", ".", ".", "6", "."],
                            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                            [".", "6", ".", ".", ".", ".", "2", "8", "."],
                            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                            [".", ".", ".", ".", "8", ".", ".", "7", "9"]
                        ]
    ))

    print(isValidSudoku([
                            [".", ".", ".", ".", "5", ".", ".", "1", "."],
                            [".", "4", ".", "3", ".", ".", ".", ".", "."],
                            [".", ".", ".", ".", ".", "3", ".", ".", "1"],
                            ["8", ".", ".", ".", ".", ".", ".", "2", "."],
                            [".", ".", "2", ".", "7", ".", ".", ".", "."],
                            [".", "1", "5", ".", ".", ".", ".", ".", "."],
                            [".", ".", ".", ".", ".", "2", ".", ".", "."],
                            [".", "2", ".", "9", ".", ".", ".", ".", "."],
                            [".", ".", "4", ".", ".", ".", ".", ".", "."]
                        ]
    ))