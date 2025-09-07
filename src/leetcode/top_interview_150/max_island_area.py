class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        l = len(grid)
        c = len(grid[0])

        def dfs(i, j):
            if i < 0 or j < 0:
                return 0
            if i >= l or j >= c:
                return 0

            if grid[i][j] != 1:
                return 0

            grid[i][j] = -1

            return 1 + dfs(i - 1, j) + dfs(i + 1, j) + dfs(i, j - 1) + dfs(i, j + 1)

        mini = float("-inf")
        for i in range(l):
            for j in range(c):
                if grid[i][j] == 1:
                    size = dfs(i, j)
                    mini = max(mini, size)

        return mini if mini != float("-inf") else 0
