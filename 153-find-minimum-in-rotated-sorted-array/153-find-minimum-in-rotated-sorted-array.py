class Solution:
    def findMin(self, nums: List[int]) -> int:
        # if array is sorted
        if nums[0] <= nums[-1]: return nums[0]
        n = len(nums)
        l,r = -1,n
        while l+1<r:
            m = (l+r)//2
            if nums[0] > nums[m]: r = m
            else: l = m
        return nums[r]
            