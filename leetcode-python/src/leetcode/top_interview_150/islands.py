class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        l = len(grid)
        c = len(grid[0])

        visited = [[False for i in range(c)] for j in range(l)]

        def dfs(i, j):
            if i < 0 or j < 0:
                return
            if i >= l or j >= c:
                return
            if grid[i][j] == "0":
                return
            if visited[i][j]:
                return

            visited[i][j] = True
            dfs(i - 1, j)
            dfs(i, j - 1)
            dfs(i + 1, j)
            dfs(i, j + 1)

        count = 0
        for i in range(l):
            for j in range(c):
                if not visited[i][j] and grid[i][j] == "1":
                    dfs(i, j)
                    count += 1
        return count
