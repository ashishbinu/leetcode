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
        cur = head
        arr = []
        while cur:
            arr.append(cur)
            cur = cur.next
        
        n = len(arr)
        for i in range(1 + n//2):
            j = n - i - 1
            if i >= j:
                arr[i].next = None
                break
            arr[i].next = arr[j] 
            arr[j].next = arr[i+1]
            