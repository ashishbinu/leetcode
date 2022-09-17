class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l,r = -1,n
        while l + 1 < r:
            m = l+ (r-l)//2
            if target < nums[m]:
                r = m
            else:
                l = m
        if nums[l] != target: l+=1
        return l
                