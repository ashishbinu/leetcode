# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # # Creating new list space - O(n)
        # list3 = ptr = ListNode()
        # 
        # while list1 and list2:
        #     if list1.val < list2.val:
        #         ptr.next = ListNode(list1.val)
        #         list1 = list1.next
        #     else:
        #         ptr.next = ListNode(list2.val)
        #         list2 = list2.next
        #     
        #     ptr = ptr.next
        # 
        # # instead of creating new list for rest of the values just point the remaining list onto the merged list
        # if list1: ptr.next = list1
        # if list2: ptr.next = list2
        #     
        # return list3.next
        
        res = ListNode()
        back = res
        back.next = list1
        
        
        while list1 and list2:
            
            if list2.val < list1.val:
                back.next = list2
                tmp = list2.next
                list2.next = list1
                back = list2
                list2 = tmp
            else:
                back = list1
                list1 = list1.next
                
        if list2: back.next = list2        
            
        return res.next