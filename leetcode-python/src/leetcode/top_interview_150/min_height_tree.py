class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        # min height is when the root is always chosen in the middle
        # for a list of len = 2, both items are considered the middls

        if n == 1:
            return [0]

        # create the adjacency list
        adj = {}
        for start, end in edges:
            adj[start] = adj.get(start, []) + [end]
            adj[end] = adj.get(end, []) + [start]

        num_children = {}
        leaves = []
        for node in adj.keys():
            num_children[node] = len(adj[node])
            if num_children[node] == 1:
                leaves.append(node)

        while len(leaves) > 0:
            if n <= 2:
                return leaves

            for _ in range(len(leaves)):
                n -= 1
                leaf = leaves.pop(0)
                for node in adj[leaf]:
                    num_children[node] -= 1
                    if num_children[node] == 1:
                        leaves.append(node)
        return []
