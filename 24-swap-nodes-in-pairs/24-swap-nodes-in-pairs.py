# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # recursive
        if head is None or head.next is None: return head
        prev = head
        curr = head.next 
        nxt = self.swapPairs(head.next.next)
        prev.next = nxt
        curr.next = prev
        return curr
        
        