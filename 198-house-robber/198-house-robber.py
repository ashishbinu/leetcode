class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp[i] represents the max amt of money to steal from 0..i houses such that no two houses are adjacent
        # dp[0] = nums[0]
        # dp[1] = nums[1]
        a,b = 0,0
        n = len(nums)
        
        for i in range(n):
            v1 = a+nums[i]
            v2 = b
            a = b
            b = max(v1,v2)
        
        return b
        