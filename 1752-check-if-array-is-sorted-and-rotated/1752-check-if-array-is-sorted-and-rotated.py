class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        flag = 0
        for i in range(n-1):
            if not (nums[i] <= nums[i+1]): flag += 1
        print(flag)
        return flag==0 or (flag==1 and nums[0] >= nums[-1])
            
