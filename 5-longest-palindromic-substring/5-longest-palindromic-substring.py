class Solution:
    def longestPalindrome(self, s: str) -> str:
        # time - O(n^2), space - O(1)
        # iterator is mid of palindrome and expanding on both sides
        
        def expand_from_mid(l,r,s): # it expands from l and r till its palindrome
            while l >= 0 and r < n:
                if s[l] != s[r]: break
                l -= 1
                r += 1
            return l+1,r-1
        
        n = len(s)
        L = R = 0
        for i in range(n-1):
            for j in [0,1]: # it handles both cases where mid is single element or double
                l,r = expand_from_mid(i,i + j,s)
                if r - l > R - L: L,R = l,r
            
        return s[L:R+1] 
    
        # DP with dp[l][r] (represents if l..=r substring is palindrome or not) works
        
        # # DP don't know if my logic will work or not
        # n = len(s)
        # # dp[i] represents max length substring palindrome such that i^th character is the last character
        # dp = [1] * n
        # idx = 0
        # for i in range(1,n):
        #     # find the transition function
        #     if i - dp[i-1] - 1 > 0:
        #         dp[i] = dp[i-1] + 2 * (s[i - dp[i-1] - 1] == s[i])
        #     else:
        #         dp[i] = 2 * (s[i] == s[i-1])
        #     idx = i if dp[i] > dp[idx] else idx # end idx for max length palindrom substring
        #     
        # return s[idx-dp[idx]+1:idx+1]