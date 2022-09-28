class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l,r = -1,n
        
        while l + 1 < r:
            m = (l+r)//2
            if nums[m] <= target:
                l = m
            else:
                r = m
        return l if -1 < l < n and nums[l] == target else -1
