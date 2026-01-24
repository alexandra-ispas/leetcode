class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        NEW, VISITING, VISITED = 0, 1, 2
        status = [NEW for i in range(numCourses)]

        adj = [[] for i in range(numCourses)]
        for node, prq in prerequisites:
            adj[node].append(prq)

        result = []

        def dfs(node):
            if status[node] == VISITING:
                return False
            if status[node] == VISITED:
                return True

            status[node] = VISITING

            for nei in adj[node]:
                if not dfs(nei):
                    return False

            status[node] = VISITED
            result.append(node)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        return result
