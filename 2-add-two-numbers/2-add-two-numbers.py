# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # # time - O(m + n), space - O(1)
        a,b = l1,l2
        start = None
        end = None
        carry = 0
        
        while a or b:
            tmp = carry
            if a: tmp += a.val
            if b: tmp += b.val
            carry = tmp // 10
            tmp %= 10
            
            if a: a.val = tmp
            if b: b.val = tmp
            
            if a: a,start,end = a.next,l1,a
            if b: b,start,end = b.next,l2,b
            
        if carry: end.next = ListNode(val=carry)
        
        return start
        
        
        # # time - O(m + n), space - O(m + n)
        # a,b = l1,l2
        # c = l3 = ListNode() # dummy head
        # carry = 0
        # 
        # while a or b:
        #     tmp = carry
        #     if a: tmp += a.val
        #     if b: tmp += b.val
        #     carry = tmp // 10
        #     tmp %= 10
        #     
        #     c.next = ListNode(val=tmp)
        #     c = c.next
        #     
        #     a = a.next if a else None
        #     b = b.next if b else None
        #     
        # if carry: c.next = ListNode(val=carry)
        # 
        # return l3.next