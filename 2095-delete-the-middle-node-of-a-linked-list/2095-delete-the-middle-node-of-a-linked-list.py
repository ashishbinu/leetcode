# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None: return head
        s,f = head,head
        dummy = prev = ListNode(-1,head) # dummy head
        while f and f.next:
            prev = s
            s,f = s.next,f.next.next
        prev.next = s.next
        return dummy.next
        