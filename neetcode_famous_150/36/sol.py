class solution:
    def validSudoku(self, board: list[list[str]]) -> bool:
        for row in range(9):
            seen = set()
            for i in range(9):
                if board[row][i] == '.':
                    continue
                if board[row][i] in seen:
                    return False
                seen.add(board[row][i])
        for col in range(9):
            seen = set()
            for j in range(9):
                if board[j][col] == '.':
                    continue
                if board[j][col] in seen:
                    return False
                seen.add(board[j][col])
        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = 3 * (square // 3) + i
                    col = 3 * (square % 3) + j
                    if board[row][col] == '.':
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])
        return True

