# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        
        """
        # time - O(n), space - O(1)
        
        # find mid point of list
        s = f = ListNode(-1,head) # dummy head
        while f and f.next: s,f = s.next,f.next.next
       
        # reverse second half of the list
        def reverse(head):
            prev,cur,nxt = None,head,head
            while cur:
                nxt = nxt.next
                cur.next = prev
                prev,cur = cur,nxt
            return prev
        
        end = reverse(s.next)
        s.next = None # remove the link between the two lists
        
        # merge the two lists
        while end:
            head.next,end.next,end,head = end,head.next,end.next,head.next
        
        # # time - O(n), space - O(n)
        # cur = head
        # arr = []
        # while cur:
        #     arr.append(cur)
        #     cur = cur.next
        # 
        # n = len(arr)
        # i = 0
        # j = n - 1
        # while i < j:
        #     arr[i].next = arr[j] 
        #     i += 1
        #     arr[j].next = arr[i]
        #     j -= 1
        # arr[i].next = None
        
        # can be done using recursion but TLE
        # # time - O(n^2), space - O(n)
        # if head is None or head.next is None or head.next.next is None: return head
        # cur = head 
        # prev = None
        # while cur.next: prev,cur = cur,cur.next
        # nxt = head.next
        # prev.next,cur.next,head.next = None,nxt,cur
        # self.reorderList(nxt)
        