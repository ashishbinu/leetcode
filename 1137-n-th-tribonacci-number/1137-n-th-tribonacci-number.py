class Solution:
    def tribonacci(self, n: int) -> int:
        a,b,c = 1,0,0
        for i in range(1,n+1):
            a,b,c = b,c,a+b+c
        return c
        