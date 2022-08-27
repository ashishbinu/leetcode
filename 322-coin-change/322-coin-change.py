class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}
        
        def coinchange(x):
            if x == 0: return 0
            if x < 0 : return -1
            if x in dp: return dp[x]
            
            min_val = None
            for i in coins:
                v = coinchange(x-i)
                if not v < 0:
                    if min_val is None: min_val = v
                    min_val = min(min_val,v)
            if min_val is not None:
                dp[x] = 1 + min_val
            else:
                dp[x] = -1
            return dp[x]
        
        return coinchange(amount)
        