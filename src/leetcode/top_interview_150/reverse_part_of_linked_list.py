# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """
        if head == None or left == right:
            return head

        dummy = ListNode(0)
        dummy.next = head

        prev = next = None
        counter = 1
        prev = dummy
        while counter < left:
            prev = prev.next
            counter += 1

        curr = prev.next

        while counter < right:
            next = curr.next
            curr.next = next.next
            next.next = prev.next
            prev.next = next

            counter += 1

        return dummy.next
