class Solution(object):
    def countIslands(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """

        l = len(grid)
        c = len(grid[0])

        visited = [[False for _ in range(c)] for _ in range(l)]

        def dfs(i, j):
            if i < 0 or j < 0 or i >= l or j >= c:
                return 0
            if grid[i][j] == 0:
                return 0
            if visited[i][j]:
                return 0

            visited[i][j] = True

            return (
                grid[i][j]
                + dfs(i - 1, j)
                + dfs(i + 1, j)
                + dfs(i, j - 1)
                + dfs(i, j + 1)
            )

        count = 0
        for i in range(l):
            for j in range(c):
                if grid[i][j] != 0 and not visited[i][j]:
                    value = dfs(i, j)
                    if value % k == 0:
                        count += 1

        return count
