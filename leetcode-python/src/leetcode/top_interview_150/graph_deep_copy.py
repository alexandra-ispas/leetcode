"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution(object):
    def __init__(self):
        self.mapping = {}

    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return None

        if node in self.mapping:
            return self.mapping[node]

        new_node = Node(val=node.val)
        self.mapping[node] = new_node

        for neigh in node.neighbors:
            new_node.neighbors.append(self.cloneGraph(neigh))

        return new_node
