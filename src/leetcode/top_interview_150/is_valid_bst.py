# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        return self.helper(root, float("-inf"), float("inf"))

    def helper(self, root, mini, maxi):
        if not root:
            return True

        return (
            (root.val > mini and root.val < maxi)
            and self.helper(root.left, mini, root.val)
            and self.helper(root.right, root.val, maxi)
        )
