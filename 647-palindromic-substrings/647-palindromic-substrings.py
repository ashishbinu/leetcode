class Solution:
    def countSubstrings(self, s: str) -> int:
        # dp[(i,j)] represents if string i..=j is palindrome or not
        n = len(s)
        dp = set() # it only stores (i,j) such that it is a palindrome
        
        for l in range(1,n+1): # l is length
            for i in range(n-l+1): # i and j are start and end of substring
                j = i+l-1
                if s[i] == s[j]:
                    if l <= 3: dp.add((i,j))
                    elif (i+1,j-1) in dp: dp.add((i,j))
                    
        return len(dp)