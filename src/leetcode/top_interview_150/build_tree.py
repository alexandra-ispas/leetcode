# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """

        # inorder: s -> r -> d
        # preorder: r -> s ->

        if len(preorder) == 0 or len(inorder) == 0:
            return None

        r = preorder.pop(0)
        inx = inorder.index(r)

        root = TreeNode(val=r)
        root.left = self.buildTree(preorder, inorder[:inx])
        root.right = self.buildTree(preorder, inorder[inx + 1 :])

        return root
