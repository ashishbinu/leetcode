class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # dp with space optimisation
        n = len(nums)
        a,b,c = 1,1,1 # a = dp[i-1], b = min_dp[i-1], c = dp[i]
        res = -math.inf
        for i,v in enumerate(nums):
            c = max(a*v,b*v,v)
            b = min(a*v,b*v,v)
            a = c
            if c > res: res = c
        return res
    
        # # dp approach
        # # dp[i] stores the max product subarray which includes i in the array till i 
        # # min_dp[i] stores the min product subarray which includes i in the array till i 
        # n = len(nums)
        # dp = [1]*n
        # min_dp = [1]*n
        # dp[0] = nums[0]
        # min_dp[0] = nums[0]
        # for i in range(1,n):
        #     dp[i] = max(nums[i],min_dp[i-1]*nums[i],dp[i-1]*nums[i])
        #     # min_dp is there to store the min product in the case to find max in [-2,3,-4] 
        #     min_dp[i] = min(nums[i],min_dp[i-1]*nums[i],dp[i-1]*nums[i])
        #     
        # return max(dp)