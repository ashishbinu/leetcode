class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # dp[i] represents min cost to reach ith position
        n = len(cost)
        
        a, b = 0, 0 # a = dp[0], b = dp[1]
        
        for i in range(2,n+1):
            v2 = b + cost[i-1]
            v1 = a + cost[i-2]
            a = b
            b = v1 if v1 < v2 else v2
        
        return b