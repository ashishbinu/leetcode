class Solution:
    def rob(self, nums: List[int]) -> int:
        def max(a,b): return a if a > b else b
        
        # dp[i] represents max money robbed from houses 0..=i such that no two robbed houses are adjacent
        # time - O(n), space - O(n)
        n = len(nums)
        if n == 1: return nums[0]
        
        a = b = c = d = 0 # a,c = dp[i-2], b,d = dp[i-1]
        for i in range(n-1):
            a,b = b,max(a + nums[i], b)
            c,d = d,max(c + nums[i+1], d)
            
        # b = dp[n-2] - represents max money robbed from house 0..=n-2
        # d = dp[n-1] - represents max money robbed from house 1..=n-1
            
        return max(b,d)
        