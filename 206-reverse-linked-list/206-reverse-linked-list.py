# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # recursive
        #
        # if head is None or head.next is None: return head
        # newHead = self.reverseList(head.next)
        # head.next.next = head
        # head.next = None
        # return newHead
        
        # iterative
        prev = None
        while head:
            tmp = head.next
            head.next = prev
            prev = head
            head = tmp
            
        return prev
        
