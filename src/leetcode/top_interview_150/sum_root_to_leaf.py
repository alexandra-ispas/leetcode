# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.results = []

    def sumNumbers(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if root is None:
            return 0

        return self.helper(root, 0)

    def helper(self, root, value):
        if root is None:
            return 0

        value = value * 10 + root.val

        if root.left is None and root.right is None:
            return value

        return self.helper(root.left, value) + self.helper(root.right, value)
