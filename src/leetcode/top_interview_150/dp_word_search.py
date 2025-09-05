class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        def dfs(i, j, idx):
            if idx == len(word):
                return True
            if i < 0 or j < 0:
                return False
            if i >= len(board) or j >= len(board[0]):
                return False
            if board[i][j] != word[idx]:
                return False

            temp = board[i][j]

            board[i][j] = "."
            # down = dfs(i + 1, j, idx+1)
            # up = dfs(i - 1, j, idx+1)
            # right = dfs(i, j + 1, idx+1)
            # left = dfs(i, j - 1, idx+1)

            val = (
                dfs(i + 1, j, idx + 1)
                or dfs(i - 1, j, idx + 1)
                or dfs(i, j + 1, idx + 1)
                or dfs(i, j - 1, idx + 1)
            )

            board[i][j] = temp
            return val

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True

        return False
