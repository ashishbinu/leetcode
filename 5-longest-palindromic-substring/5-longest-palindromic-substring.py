class Solution:
    def longestPalindrome(self, s: str) -> str:
        # All solutions
        # https://zkf85.github.io/2019/03/26/leetcode-005-longest-palindrome
        
        # time - O(n^2), space - O(1)
        # iterator is mid of palindrome and expanding on both sides
        n = len(s)
        L = R = 0
        for i in range(n-1):
            for j in [0,1]: # it handles both cases where mid is single element or double
                
                # it expands from l and r till its palindrome
                l,r = i,i+j
                while l >= 0 and r < n and s[l] == s[r]:
                    l -= 1
                    r += 1
                l,r = l+1,r-1
                
                if r - l > R - L: L,R = l,r
            
        return s[L:R+1] 
    
        # DP solution 1 : with dp[l][r] (represents if l..=r substring is palindrome or not) works
        # DP solution 2:  Reverse the string s to s' . Now find longest common substring between s and s'. so dp[i][j] represents length of max substring in s[0..=i] and s'[0..=j]
        
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