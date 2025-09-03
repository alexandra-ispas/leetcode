class Solution(object):
    def solve(self, board):
        if not board:
            return

        l = len(board)
        c = len(board[0])

        for i in range(l):
            self.visit(board, i, 0, l, c)
            self.visit(board, i, c - 1, l, c)

        for j in range(c):
            self.visit(board, 0, j, l, c)
            self.visit(board, l - 1, j, l, c)

        for i in range(l):
            for j in range(c):
                if board[i][j] == ".":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"

    def visit(self, board, i, j, l, c):
        if i < 0 or j < 0:
            return
        if i >= l or j >= c:
            return

        if board[i][j] != "O":
            return

        board[i][j] = "."

        self.visit(board, i - 1, j, l, c)
        self.visit(board, i + 1, j, l, c)
        self.visit(board, i, j - 1, l, c)
        self.visit(board, i, j + 1, l, c)
