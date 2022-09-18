class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # using bisect
        a = bisect_left(nums,target)
        b = bisect_right(nums,target) - 1
        a = a if -1 < a < len(nums) and nums[a] == target else -1
        b = b if -1 < b < len(nums) and nums[b] == target else -1
        return [a,b]
    
        # # binary search
        # n = len(nums)
        # l,r = -1,n
        # while l + 1 < r:
        #     m = l + (r - l)//2
        #     if target <= nums[m]:
        #         r = m
        #     else:
        #         l = m
        # a = r if -1 < r < n and nums[r] == target else -1
        # 
        # l,r = a,n # l is changed to a instead of -1 as it reduced the search space
        # while l + 1 < r:
        #     m = l + (r - l)//2
        #     if nums[m] <= target:
        #         l = m
        #     else:
        #         r = m
        # b = l if -1 < l < n and nums[l] == target else -1
        # 
        # return [a,b]