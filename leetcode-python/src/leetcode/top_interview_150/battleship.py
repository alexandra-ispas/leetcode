class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        l = len(board)
        c = len(board[0])
        counter = 0

        def is_starter(i, j):
            if i == 0 and j == 0:
                return True
            if i == 0:
                return board[i][j - 1] == "."
            if j == 0:
                return board[i - 1][j] == "."
            return board[i - 1][j] == "." and board[i][j - 1] == "."

        for i in range(l):
            for j in range(c):
                if board[i][j] == "X" and is_starter(i, j):
                    counter += 1
        return counter
