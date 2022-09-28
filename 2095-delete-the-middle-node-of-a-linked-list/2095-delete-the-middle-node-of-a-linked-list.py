# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None: return head
        dummy = s = ListNode(-1,head) # dummy head
        f = head
        while f and f.next: s,f = s.next,f.next.next
        s.next = s.next.next # s stops at one node before upper middle element
        return dummy.next
        