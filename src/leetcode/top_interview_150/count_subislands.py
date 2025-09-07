class Solution(object):
    def countSubIslands(self, grid1, grid2):
        """
        :type grid1: List[List[int]]
        :type grid2: List[List[int]]
        :rtype: int
        """
        l = len(grid2)
        c = len(grid2[0])

        def dfs(i, j):
            if i < 0 or j < 0 or i >= l or j >= c:
                return
            if grid2[i][j] != 1:
                return

            grid2[i][j] = 0

            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)

        for i in range(l):
            for j in range(c):
                if grid1[i][j] == 0 and grid2[i][j] == 1:
                    dfs(i, j)

        count = 0
        for i in range(l):
            for j in range(c):
                if grid2[i][j] == 1:
                    dfs(i, j)
                    count += 1
        return count
