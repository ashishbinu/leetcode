class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        def cond(i,ch): return ch < letters[i]
        
        n = len(letters)
        l,r = -1,n
        while l + 1 < r:
            m = (l+r)//2
            if cond(m,target): r = m
            else: l = m
        
        return letters[r%n]