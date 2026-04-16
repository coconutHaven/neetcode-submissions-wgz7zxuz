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

        curr1 = list1
        curr2 = list2

        res = ListNode(min(curr2.val, curr1.val))
        currRes = res

        if curr1.val <= curr2.val:
                curr1 = curr1.next
        else:
                curr2 = curr2.next

        currRes.next = self.mergeTwoLists(curr1, curr2)

        return res