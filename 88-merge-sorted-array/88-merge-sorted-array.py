class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # sort it from the back of list1
        
        i = m - 1
        j = n - 1
        while i >= 0 or j >= 0:
            # the loop will break when i and j are at -1 i.e. behind zero.
            if j==-1 or i >= 0 and nums1[i] > nums2[j]: # and has higher precedence
                nums1[i+j+1] = nums1[i] # i + j + 1 = k iterator for merged array
                i -= 1
            else:
                nums1[i+j+1] = nums2[j]
                j -= 1
                
            