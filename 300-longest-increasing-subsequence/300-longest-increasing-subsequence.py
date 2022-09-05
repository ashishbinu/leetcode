class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp[i] represents lis ending at ith position in i array
        n = len(nums)
        dp = [0] * n
        dp[0] = 1
        for i in range(1,n):
            dp[i] = 1 
            m = 0
            for k in range(1,i+1):
                if nums[i] > nums[i-k] and m < dp[i-k]:
                    m = dp[i-k]
            dp[i] += m
        return max(dp)