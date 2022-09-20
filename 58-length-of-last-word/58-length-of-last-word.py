class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res = 0
        for v in reversed(s):
            if res and v==" ": break
            res += v!=" "
            
        return res