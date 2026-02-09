
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        row, col = click
        if board[row][col] == 'M':
            board[row][col] = 'X'
        else:
            self.reveal(row, col, board)
        return board

    def reveal(self, i: int, j: int, board: List[List[str]]):
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != 'E':
            return
        neigh = self.numbermines(i, j, board, 0)
        if neigh > 0:
            board[i][j] = str(neigh)
        else:
            board[i][j] = 'B'
            self.reveal(i + 1, j, board)
            self.reveal(i, j + 1, board)
            self.reveal(i - 1, j, board)
            self.reveal(i, j - 1, board)
            self.reveal(i + 1, j + 1, board)
            self.reveal(i - 1, j - 1, board)
            self.reveal(i + 1, j - 1, board)
            self.reveal(i - 1, j + 1, board)

    def numbermines(self, row: int, col: int, board: List[List[str]], c: int) -> int:
        if row - 1 >= 0 and board[row - 1][col] == 'M': c += 1
        if row + 1 < len(board) and board[row + 1][col] == 'M': c += 1
        if col - 1 >= 0 and board[row][col - 1] == 'M': c += 1
        if col + 1 < len(board[0]) and board[row][col + 1] == 'M': c += 1
        if row - 1 >= 0 and col - 1 >= 0 and board[row - 1][col - 1] == 'M': c += 1
        if row - 1 >= 0 and col + 1 < len(board[0]) and board[row - 1][col + 1] == 'M': c += 1
        if row + 1 < len(board) and col - 1 >= 0 and board[row + 1][col - 1] == 'M': c += 1
        if row + 1 < len(board) and col + 1 < len(board[0]) and board[row + 1][col + 1] == 'M': c += 1
        return c