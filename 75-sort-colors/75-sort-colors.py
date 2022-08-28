class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = l = 0
        r = n - 1
        
        while i < r:
            while nums[r] == 2:
                r-=1 
                if r < 0 and l > r: return
            while nums[l] == 0:
                l+=1 
                if l >= n or l > r: return 
            while i < r and nums[i] == 1 or i < l: i+=1 
            if nums[i] == 2:
                nums[i],nums[r] = nums[r],nums[i]
            elif nums[i] == 0:
                nums[i],nums[l] = nums[l],nums[i]