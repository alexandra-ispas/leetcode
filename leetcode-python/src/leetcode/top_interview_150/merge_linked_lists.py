# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        new_list = ListNode(0)
        new_head = new_list

        while list1 != None or list2 != None:
            val1 = list1.val if list1 != None else sys.maxsize
            val2 = list2.val if list2 != None else sys.maxsize

            if val1 <= val2:
                new_list.next = ListNode(val1)
                new_list = new_list.next

                list1 = list1.next if list1 is not None else None
            if val2 < val1:
                new_list.next = ListNode(val2)
                new_list = new_list.next

                list2 = list2.next if list2 is not None else None

        return new_head.next
