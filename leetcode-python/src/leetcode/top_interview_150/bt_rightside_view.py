# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        # if root is None:
        #     return []

        # result = []
        # queue = [root]

        # while len(queue) > 0:
        #     size = len(queue)
        #     to_add = None

        #     for _ in range(size):
        #         node = queue.pop(0)
        #         if node:
        #             to_add = node
        #             queue.append(node.left)
        #             queue.append(node.right)

        #     if to_add:
        #         result.append(to_add.val)

        # return result

        result = []

        def dfs(node, depth):
            if not node:
                return

            if depth == len(result):
                result.append(node.val)

            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)

        dfs(root, 0)
        return result
