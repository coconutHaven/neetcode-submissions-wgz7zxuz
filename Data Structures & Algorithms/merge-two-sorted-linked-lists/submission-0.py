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


        while curr1 != None and curr2 != None:
            currRes.next = ListNode(min(curr2.val, curr1.val))
            currRes = currRes.next
            if curr1.val <= curr2.val:
                curr1 = curr1.next
            else:
                curr2 = curr2.next

        # add the rest of either
        while curr1:
            currRes.next = ListNode(curr1.val)
            currRes = currRes.next
            curr1 = curr1.next
        while curr2:
            currRes.next = ListNode(curr2.val)
            currRes = currRes.next
            curr2 = curr2.next 

        return res