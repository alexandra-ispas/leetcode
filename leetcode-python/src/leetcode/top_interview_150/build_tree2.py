# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: Optional[TreeNode]
        """
        # inorder:      s -> r -> d
        # postorder:    s -> d -> r

        return self.helper(inorder, postorder)

    def helper(self, inorder, postorder):
        if len(inorder) == 0 or len(postorder) == 0:
            return None

        root_val = postorder.pop()
        root_idx = inorder.index(root_val)

        root = TreeNode(root_val)
        root.right = self.helper(inorder[root_idx + 1 :], postorder)
        root.left = self.helper(inorder[:root_idx], postorder)

        return root
