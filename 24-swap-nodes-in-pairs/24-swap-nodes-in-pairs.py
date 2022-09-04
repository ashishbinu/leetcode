# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # iterative
        if head is None or head.next is None: return head
        
        prev = ListNode(next=head)
        curr = head
        new_head = curr.next
        
        while curr:
            nxt  = curr.next
            if nxt is None: break

            curr.next = nxt.next
            nxt.next = curr
            prev.next = nxt

            prev = curr
            curr = curr.next
        
        return new_head
        
        # # recursive
        # if head is None or head.next is None: return head
        # prev = head
        # curr = head.next 
        # nxt = self.swapPairs(head.next.next)
        # prev.next = nxt
        # curr.next = prev
        # return curr