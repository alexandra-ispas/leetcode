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
        if root == None:
            return

        node = root
        dummy = Node(0)
        level = dummy

        while node:

            while node:
                if node.left:
                    level.next = node.left
                    level = level.next
                if node.right:
                    level.next = node.right
                    level = level.next

                node = node.next

            node = dummy.next
            level = dummy
            dummy.next = None

        return root
