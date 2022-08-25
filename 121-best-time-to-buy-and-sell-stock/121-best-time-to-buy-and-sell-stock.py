class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Two pointer approach
        l,r = 0,1
        max_profit = 0
        while r < len(prices):
            profit = prices[r] - prices[l]
            if profit < 0:
                l = r
            max_profit = max(profit,max_profit)
            r += 1
        return max_profit
    
        # # Works on kadane's algorithm
        # max_profit = 0
        # s = 0
        # for k,v in enumerate(prices):
        #     if k == 0: continue # skip for first index
        #     pd = prices[k] - prices[k-1]
        #     s += pd
        #     if s < 0: s = 0
        #     max_profit = max(s,max_profit)
        #     
        # return max_profit    
            
            
            
        
        