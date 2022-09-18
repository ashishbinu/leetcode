class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        l,r = -1,n
        while l + 1 < r:
            m = l + (r - l)//2
            if target <= nums[m]:
                r = m
            else:
                l = m
        a = r if -1 < r < n and nums[r] == target else -1
        
        l,r = a,n
        while l + 1 < r:
            m = l + (r - l)//2
            if nums[m] <= target:
                l = m
            else:
                r = m
        b = l if -1 < l < n and nums[l] == target else -1
        
        return [a,b]