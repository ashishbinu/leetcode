class Solution:
    def findMin(self, nums: List[int]) -> int:
        def condition(idx):
            l = idx - 1
            r = idx + 1
            a = nums[l] if l >= 0 else math.inf
            b = nums[r] if r < n else math.inf
            return nums[idx] < a and nums[idx] < b
        
        n = len(nums)
        
        l,r = 0,n-1
        
        while l <= r:
            m = l + (r-l)//2
            if condition(m): return nums[m]
            if nums[m] >= nums[l] and nums[m] > nums[r]:
                l = m + 1
            else:
                r = m - 1