class Solution:
    def countBits(self, n: int) -> List[int]:
        c = []
        
        for i in range(n+1):
            res = 0
            while i:
                i &= i - 1
                res += 1
            c.append(res)
            
        return c