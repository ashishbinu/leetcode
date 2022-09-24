class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp[i] represents max money robbed from houses 0..=i such that no two robbed houses are adjacent
        n = len(nums)
        if n < 1: return 0
        if n == 1: return nums[0]
        
        dp = [0] * n
        for i in range(n-1):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        a = dp[n-2]    
        dp = [0] * n
        for i in range(1,n):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])
            
        return max(a,dp[n-1])
        