class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        
        dp = {}
        dp[0] = 0
        dp[1] = 0
        
        for i in range(2,n+1):
            v1 = dp[i-1] + cost[i-1]
            v2 = dp[i-2] + cost[i-2]
            dp[i] = v1 if v1 < v2 else v2
        
        return dp[n]