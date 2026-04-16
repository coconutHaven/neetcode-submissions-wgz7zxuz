# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1

        res = ListNode(min(list1.val, list2.val))

        if list1.val <= list2.val:
            list1 = list1.next
        else:
            list2 = list2.next

        res.next = self.mergeTwoLists(list1, list2)

        return res