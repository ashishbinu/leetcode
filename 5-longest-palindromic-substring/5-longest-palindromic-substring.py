class Solution:
    def longestPalindrome(self, s: str) -> str:
        # time - O(n^2)
        n = len(s)
        best_l = 0
        best_r = 0
        best_len = 1
        for i in range(n):
            l,r = i,i
            while l >= 0 and r < n:
                if s[l] != s[r]: break
                l -= 1
                r += 1
            l += 1
            r -= 1
            length = r - l + 1
            if length > best_len:
                best_len = length
                best_l,best_r = l,r
            
        for i in range(n-1):
            l,r = i,i+1
            while l >= 0 and r < n:
                if s[l] != s[r]: break
                l -= 1
                r += 1
            l += 1
            r -= 1
            length = r - l + 1
            if length > best_len:
                best_len = length
                best_l,best_r = l,r
            
        return s[best_l:best_r+1] 
    
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