# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        found = {}
        curr = head
        while True:
            if curr is None or curr.next is None:
                return False
            if curr not in found:
                found[curr] = 1
            else:
                found[curr] += 1
                if found[curr] >= 2:
                    return True
            curr = curr.next


            