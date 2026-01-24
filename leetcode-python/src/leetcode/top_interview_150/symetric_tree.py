# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if root is None:
            return False
        return self.helper(root.left, root.right)

    def helper(self, left, right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False

        return (
            left.val == right.val
            and self.helper(left.left, right.right)
            and self.helper(left.right, right.left)
        )
