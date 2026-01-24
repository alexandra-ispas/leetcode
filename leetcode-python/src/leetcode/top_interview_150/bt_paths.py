# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[str]
        """
        if root is None:
            return []

        result = []

        def dfs(node, current):
            if current == "":
                new_current = str(node.val)
            else:
                new_current = "{}->{}".format(current, node.val)

            if node.left is None and node.right is None:
                result.append(new_current)
                return
            if node.left is not None:
                dfs(node.left, new_current)
            if node.right is not None:
                dfs(node.right, new_current)

        dfs(root, "")
        return result
