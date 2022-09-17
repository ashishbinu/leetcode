class Solution:
    def mySqrt(self, x: int) -> int:
        def condition(v): return v*v <= x
        
        l,r = 0,x+1
        while l + 1 < r:
            m = l + (r-l)//2
            if condition(m): l = m
            else: r = m
        return l
                
        