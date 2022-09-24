class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp[i] represents max money robbed from houses 0..=i such that no two robbed houses are adjacent
        n = len(nums)
        if n < 1: return 0
        if n == 1: return nums[0]
        
        a,b = 0,0 # dp[i-2], dp[i-1]
        for i in range(n-1):
            a,b = b,max(a + nums[i], b)
            
        res = b  # dp[n-2] - represents max money robbed from house 0..=n-2
        a,b = 0,0
        for i in range(1,n):
            a,b = b,max(a + nums[i], b)
            
        # b = dp[n-2] - represents max money robbed from house 1..=n-1
            
        return max(res,b)
        