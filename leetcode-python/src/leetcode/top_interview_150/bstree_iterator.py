# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: Optional[TreeNode]
        """
        # s -> r -> d
        self.values = [0]

        def dfs(node):
            if node is None:
                return []
            dfs(node.left)
            self.values += [node.val]
            dfs(node.right)

        dfs(root)
        self.i = 0

    def next(self):
        """
        :rtype: int
        """
        self.i += 1
        return self.values[self.i]

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.i < len(self.values) - 1


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
