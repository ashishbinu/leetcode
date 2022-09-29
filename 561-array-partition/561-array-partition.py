class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(v for k,v in enumerate(sorted(nums)) if k%2==0)
        