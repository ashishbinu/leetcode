class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        indexof = defaultdict(list)
        
        for i in range(n):
            indexof[nums[i]] += [i]
        
        nums.sort()
        
        l,r = 0, n-1
        while l < r:
            a,b = nums[l], nums[r]
            is_same = a == b
            if is_same and a + b == target:
                return indexof[a]
            if a + b == target:
                return [indexof[a][0],indexof[b][0]]
            if a + b > target:
                r -= 1
            else:
                l += 1
                
                
                
        
        