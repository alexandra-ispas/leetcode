# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        self.max_sum = float("-inf")  # Global best sum

        def dfs(node):
            if not node:
                return 0
            # Left aur right subtree se best gain (agar negative ho, ignore = 0)
            left_gain = max(dfs(node.left), 0)
            right_gain = max(dfs(node.right), 0)

            # Full path passing through current node
            current_sum = node.val + left_gain + right_gain

            # Update global max
            self.max_sum = max(self.max_sum, current_sum)

            # Return best gain to parent (only one side)
            return node.val + max(left_gain, right_gain)

        dfs(root)
        return self.max_sum
