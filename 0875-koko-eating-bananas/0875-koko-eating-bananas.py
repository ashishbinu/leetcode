class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l, r = 0, max(piles)
        
        def f(k):
            hrs = 0
            
            for v in piles:
                hrs += math.ceil(v/k)
            return hrs <= h
        
        while r-l > 1:
            m = (l + r)//2
            if f(m): r = m
            else: l =m
        
        return r
        