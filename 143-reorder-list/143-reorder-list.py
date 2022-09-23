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
        i = 0
        j = n - 1
        while i < j:
            arr[i].next = arr[j] 
            i += 1
            arr[j].next = arr[i]
            j -= 1
        arr[i].next = None
            