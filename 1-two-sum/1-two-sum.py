class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        numdict = {}
        
        for i,v in enumerate(nums):
            if target - v in numdict:
                return [i,numdict[target-v]]
            numdict[v] = i