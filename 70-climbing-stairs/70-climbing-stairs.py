class Solution:
    def climbStairs(self, n: int,memo={}) -> int:
        
        # It's basically fibonacci
        
        def cs(n,a,b):
            if n == 0: return a
            if n == 1: return b
            
            return cs(n-1,b,a+b)
        
        return cs(n,1,1)
        