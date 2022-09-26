# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # Two pointers when reaching the end of linked list goes to head of the other list
        # After each full iteration of linked list both pointers wud be at same length from the end
        # time - O(m+n), space - O(1)
        a,b = headA,headB
        if a is None or b is None: return None
        while a != b: # when both a = b = None implies no intersection
            a = a.next if a else headB
            b = b.next if b else headA
        return a
    
        # # time - O(m+n), space - O(m)
        # nodes = set()
        # cur = headA
        # while cur:
        #     nodes.add(cur)
        #     cur = cur.next
        #     
        # cur = headB
        # while cur:
        #     if cur in nodes: return cur
        #     cur = cur.next
        # return None