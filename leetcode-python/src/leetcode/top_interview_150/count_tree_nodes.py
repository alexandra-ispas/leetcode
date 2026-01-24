# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if root == None:
            return 0
        # else:
        #     return 1 + self.countNodes(root.left) + self.countNodes(root.right)

        l_height = self.getLHeight(root)
        r_height = self.getRHeight(root)

        if l_height == r_height:
            return 2**l_height - 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

    def getRHeight(self, node):
        height = 0
        while node:
            height += 1
            node = node.right
        return height

    def getLHeight(self, node):
        height = 0
        while node:
            height += 1
            node = node.left
        return height
