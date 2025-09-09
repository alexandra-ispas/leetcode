"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None

        it = root
        while it.left:
            level_it = it

            while level_it:
                level_it.left.next = level_it.right
                if level_it.next:
                    level_it.right.next = level_it.next.left
                level_it = level_it.next

            it = it.left

        return root
