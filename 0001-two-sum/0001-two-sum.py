class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexof = {}
        for k,v in enumerate(nums):
            b = target - v
            if b in indexof: return [k,indexof[b]]
            indexof[v] = k