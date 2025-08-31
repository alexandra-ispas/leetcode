# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        carry_over = 0

        h1 = ListNode(0)
        tail = h1

        while l1 != None or l2 != None or carry_over != 0:
            d1 = l1.val if l1 is not None else 0
            d2 = l2.val if l2 is not None else 0

            sum = d1 + d2 + carry_over

            carry_over = sum / 10
            h1.next = ListNode(sum % 10)

            h1 = h1.next

            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

        return tail.next
