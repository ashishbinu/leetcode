class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        
        N = len(s)
        n = len(g)
       
        i = 0
        for j in range(N):
            if i >= n: break
            if s[j] >= g[i]:
                i+=1
                
        return i
        
        