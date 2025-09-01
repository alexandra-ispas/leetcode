# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        return self.helper(root, float("-inf"), float("inf"))

    def helper(self, root, low, high):
        if root is None:
            return high - low

        left = self.helper(root.left, low, root.val)
        right = self.helper(root.right, root.val, high)

        return min(left, right)
