class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * n
        dp[0] = True
        for i in range(1,n):
            for j in reversed(range(i)):
                dp[i] = dp[j] and nums[j] >= i - j
                if dp[i]: break

        return dp[n-1]