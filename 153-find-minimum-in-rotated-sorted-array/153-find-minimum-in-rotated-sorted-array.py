class Solution:
    def findMin(self, nums: List[int]) -> int:
        def condition(m):
            return nums[0] <= nums[-1] or nums[0] > nums[m]
        n = len(nums)
        l,r = -1,n
        while l+1<r:
            m = l+(r-l)//2
            if condition(m): r = m
            else: l = m
        return nums[r]
            