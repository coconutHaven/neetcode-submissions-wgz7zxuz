# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        curr = head
        lastNode = None
        while curr:
            newHead = ListNode(curr.val, lastNode)
            lastNode = newHead
            curr = curr.next
        
        return lastNode


        