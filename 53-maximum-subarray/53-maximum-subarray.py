class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        # Kadane's algorithm
        s = 0
        m = nums[0]
        for v in nums:
            s += v
            m = s if s > m else m
            if s < 0: s = 0
        return m        
            
        