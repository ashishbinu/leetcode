class Solution:
    def climbStairs(self, n: int,memo={}) -> int:
        # It's basically fibonacci with fib(0) = 1 and fib(1) = 1
        
        a,b = 1,1
        for i in range(1,n):
            a,b = b,a+b
        return b
    
        # def cs(n,a,b):
        #     if n == 0: return a
        #     if n == 1: return b
        #     
        #     return cs(n-1,b,a+b)
        # 
        # return cs(n,1,1)
        