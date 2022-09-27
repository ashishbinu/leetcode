# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a,b = l1,l2
        c = l3 = ListNode() # dummy head
        carry = 0
        
        while a or b:
            tmp = carry
            if a: tmp += a.val
            if b: tmp += b.val
            carry = tmp // 10
            tmp %= 10
            
            c.next = ListNode(val=tmp)
            c = c.next
            
            a = a.next if a else None
            b = b.next if b else None
            
        if carry: c.next = ListNode(val=carry)

        return l3.next