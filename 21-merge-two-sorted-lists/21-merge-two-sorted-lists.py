# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        list3 = tmp = ListNode()
        
        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                tmp.next = ListNode(list1.val)
                list1 = list1.next
            else:
                tmp.next = ListNode(list2.val)
                list2 = list2.next
            
            tmp = tmp.next
        
        while list1 is not None:
            tmp.next = ListNode(list1.val)
            list1 = list1.next
            tmp = tmp.next
            
        while list2 is not None:
            tmp.next = ListNode(list2.val)
            list2 = list2.next
            tmp = tmp.next
            
        return list3.next