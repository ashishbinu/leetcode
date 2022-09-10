class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # dp[i][j] represents max lcs in string text1 with length i and text2 with length j
        # if text1[i-1] == text2[j-1]:
        #     dp[i][j] = dp[i-1][j-1] + 1  
        # else:
        #     dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        # dp[0][k] or dp[k][0] is 0
        # result is dp[n][m]
        
        n,m = len(text1),len(text2)
        prev = [0] * (m+1)
        
        for i in range(1,n+1):
            curr = [0] * (m+1)
            for j in range(1,m+1):
                if text1[i-1] == text2[j-1]:
                    curr[j] = prev[j-1] + 1  
                else:
                    curr[j] = max(prev[j],curr[j-1])
            prev = curr
       
        return curr[m]