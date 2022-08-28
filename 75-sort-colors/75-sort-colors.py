class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = l = 0
        r = n - 1
        
        while i < r:
            while nums[l] == 0:
                l+=1 
                if l >= n or l > r: return 
            while nums[r] == 2:
                r-=1 
                if r < 0 or l > r: return
            if i < l: i = l    
            while nums[i] == 1:
                i+=1 
                if i > r: return
                
            if nums[i] == 2: nums[i],nums[r] = nums[r],nums[i]
            elif nums[i] == 0: nums[i],nums[l] = nums[l],nums[i]