class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1]*n
        min_dp = [1]*n
        dp[0] = nums[0]
        min_dp[0] = nums[0]
        for i in range(1,n):
            dp[i] = max(nums[i],min_dp[i-1]*nums[i],dp[i-1]*nums[i])
            min_dp[i] = min(nums[i],min_dp[i-1]*nums[i],dp[i-1]*nums[i])
        return max(dp)