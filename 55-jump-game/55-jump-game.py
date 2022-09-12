class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # dp approach
        n = len(nums)
        dp = [False] * n
        dp[0] = True
        for i in range(1,n):
            for j in reversed(range(i)):
                dp[i] = dp[j] and j + nums[j] >= i
                if dp[i]: break
                    
        return dp[-1]
    
        # # greedy approach
        # n = len(nums)
        # res = n - 1
        # for i in range(n-1,-1,-1):
        #     if nums[i] - (res - i) >= 0:
        #         res = i
        # return not res