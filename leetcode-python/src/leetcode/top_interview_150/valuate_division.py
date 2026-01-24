class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """

        def bfs(a, b, value):
            visited = set()
            queue = [[a, value]]

            while queue:
                node, val = queue.pop(0)
                if node == b:
                    return val
                if node in visited:
                    continue

                visited.add(node)

                for neigh in adj[node]:
                    if neigh not in visited:
                        queue.append([neigh, val * adj[node][neigh]])
            return -1

        adj = {}
        for eq, value in zip(equations, values):
            a, b = eq

            if not adj.get(a, None):
                adj[a] = {b: value}
            else:
                adj[a][b] = value

            if not adj.get(b, None):
                adj[b] = {a: 1 / value}
            else:
                adj[b][a] = 1 / value

        results = []
        for c, d in queries:
            if c not in adj or d not in adj:
                results.append(-1)
            else:
                results.append(bfs(c, d, 1))

        return results
