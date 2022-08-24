# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        i = j = head
        while j:
            if j.next is None: break
            i = i.next
            j = j.next.next
            
        return i
            
        