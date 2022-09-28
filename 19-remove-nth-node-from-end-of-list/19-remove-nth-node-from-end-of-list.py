# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 1 pass
        # time - O(n), space - O(1)
        dummy = s = f = ListNode(-1,head) # dummy head
        
        for _ in range(n): f = f.next
            
        while f.next: s,f = s.next,f.next
            
        s.next = s.next.next
        return dummy.next
        
        
        # # 2 pass
        # # time - O(n), space - O(1)
        # N = 0
        # cur = head
        # while cur:
        #     N += 1
        #     cur=cur.next
        #     
        # dummy = cur = ListNode(-1,head) # dummy head
        # for _ in range(N-n): cur=cur.next
        #     
        # cur.next = cur.next.next
        # return dummy.next