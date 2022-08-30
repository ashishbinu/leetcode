class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        prev = [0] * n
        curr = [0] * n
        curr[0] = 1
        
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    curr[j] = 0
                    continue
                if i-1 >= 0: curr[j] = prev[j]
                if j-1 >= 0: curr[j] += curr[j-1]
            prev = curr
            
        return curr[n-1]