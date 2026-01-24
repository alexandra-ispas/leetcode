# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None

        if root.val in [p.val, q.val]:
            return root

        result1 = self.lowestCommonAncestor(root.left, p, q)
        result2 = self.lowestCommonAncestor(root.right, p, q)

        if result1 is not None and result2 is not None:
            return root
        return result1 or result2
