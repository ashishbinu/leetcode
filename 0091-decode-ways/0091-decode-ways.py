class Solution:
    def numDecodings(self, s: str) -> int:
        # dp[i] represents no. of ways to form a valid string for input string till ith index
        # initially dp[i-1] is dp[0]
        a,b = 1,int(s[0]!="0") # dp[i-2], dp[i-1]

        for i in range(1,len(s)): 
            td, od = int(s[i-1]), int(s[i]) # ten's digit, one's digit
            dd = td * 10 + od # double digits

            a,b = b,b * (od > 0) + a * (10 <= dd <= 26)

        # b is dp[n-1]
        return b