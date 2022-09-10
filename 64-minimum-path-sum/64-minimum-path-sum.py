class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n,m = len(grid),len(grid[0])
        dp = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                dp[i][j] = grid[i][j]
                if i > 0 and j > 0: dp[i][j] += min(dp[i-1][j],dp[i][j-1])
                elif i > 0: dp[i][j] += dp[i-1][j]
                elif j > 0: dp[i][j] += dp[i][j-1]
                
        return dp[n-1][m-1]
        