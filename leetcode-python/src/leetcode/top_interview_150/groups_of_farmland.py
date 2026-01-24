class Solution(object):
    def findFarmland(self, land):
        """
        :type land: List[List[int]]
        :rtype: List[List[int]]
        """
        l = len(land)
        c = len(land[0])

        def dfs(i, j):
            if i < 0 or j < 0 or i >= l or j >= c:
                return [0, 0]

            if land[i][j] != 1:
                return [0, 0]

            land[i][j] = -1
            hl1, hc1 = dfs(i + 1, j)
            hl2, hc2 = dfs(i, j + 1)

            hl = max(hl1, hl2, i)
            hc = max(hc1, hc2, j)
            return [hl, hc]

        result = []
        for i in range(l):
            for j in range(c):
                if land[i][j] == 1:
                    end = dfs(i, j)
                    result.append([i, j] + end)

        return result
