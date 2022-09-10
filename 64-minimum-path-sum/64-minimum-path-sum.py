class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n,m = len(grid),len(grid[0])
        prev = [0 for _ in range(m)]
        for i in range(n):
            curr = [0] * m
            for j in range(m):
                curr[j] = grid[i][j]
                if i > 0 and j > 0: curr[j] += min(prev[j],curr[j-1])
                elif i > 0: curr[j] += prev[j]
                elif j > 0: curr[j] += curr[j-1]
            prev = curr
                
        return curr[-1]
        