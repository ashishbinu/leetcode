class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # sort it from the back of list1
        
        a = nums1
        b = nums2
        i = m - 1
        j = n - 1
        while i >= 0 or j >= 0:
            if j==-1 or (i >= 0 and a[i] > b[j]):
                a[i+j+1] = a[i]
                i -= 1
            else:
                a[i+j+1] = b[j]
                j -= 1
                
            