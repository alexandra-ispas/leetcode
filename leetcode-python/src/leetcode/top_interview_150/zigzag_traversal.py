# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []

        queue = [root]
        result = []
        left_right = True

        while len(queue) > 0:
            size = len(queue)

            level = [0] * size
            for i in range(size):
                node = queue.pop(0)
                if left_right:
                    level[i] = node.val
                else:
                    level[size - 1 - i] = node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(level)
            left_right = not left_right

        return result
