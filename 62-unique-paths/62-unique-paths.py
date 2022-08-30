class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # prev list not needed, curr list is enough
        # time - O(m*n) , space - O(n)
        curr = [1] * n
        for i in range(1,m):
            for j in range(1,n):
                curr[j] += curr[j-1]
        return curr[n-1]
        
        # # iterative dp with space optimisation
        # prev = [1] * n
        # curr = [1] * n
        # for i in range(1,m):
        #     for j in range(n):
        #         curr[j] = prev[j]
        #         if j-1 >= 0: curr[j] += curr[j-1]
        #     prev = curr
        # return curr[n-1]
        
        # # iterative dp space-O(m*n)
        # dp = [[0 for _ in range(n)] for _ in range(m)]
        # dp = [[0 for _ in range(n)] for _ in range(m)]
        # dp[0][0] = 1
        # for i in range(m):
        #     for j in range(n):
        #         if i - 1 >= 0: dp[i][j] += dp[i-1][j] 
        #         if j - 1 >= 0: dp[i][j] += dp[i][j-1]
        # 
        # return dp[m-1][n-1]