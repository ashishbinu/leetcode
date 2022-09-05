class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp[i] represents lis ending at ith position in i array
        n = len(nums)
        dp = [0] * n
        dp[0] = 1
        for i in range(1,n):
            dp[i] = 1 + max([dp[j] for j in range(i) if nums[i] > nums[j]],default=0) 
            
        return max(dp)