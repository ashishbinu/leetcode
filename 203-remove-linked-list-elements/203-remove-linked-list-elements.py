# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        res = ListNode()
        res.next = curr = head
        prev = res
        
        while curr is not None:
            if curr.val == val:
                curr = prev.next = curr.next
                continue
            prev = curr
            curr = curr.next
            
        return res.next
        