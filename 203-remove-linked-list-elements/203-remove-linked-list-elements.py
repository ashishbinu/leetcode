# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        res = ListNode(next = head) # dummy node
        
        curr = head
        prev = res
        
        while curr is not None:
            if curr.val == val:
                prev.next = curr.next
                curr = prev
            prev = curr
            curr = curr.next
            
        return res.next
        