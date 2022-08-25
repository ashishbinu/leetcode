class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # Works on kadane's algorithm
        
        max_profit = 0
        s = 0
        for k,v in enumerate(prices):
            if k == 0: continue # skip for first index
            pd = prices[k] - prices[k-1]
            s += pd
            if s < 0: s = 0
            max_profit = max(s,max_profit)
            
        return max_profit    
            
            
            
        
        