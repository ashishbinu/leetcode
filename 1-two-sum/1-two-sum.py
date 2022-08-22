class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        numdict = {}
        for i,v in enumerate(nums):
            sval = target - v 
            if sval in numdict: return [i,numdict[sval]]
            numdict[v] = i