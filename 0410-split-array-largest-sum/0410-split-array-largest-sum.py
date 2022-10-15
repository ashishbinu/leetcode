class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        # resource : https://www.youtube.com/watch?v=HoMJSSSU_fY
        def check(given_subarr_sum):
            k,subarr_sum = 1,0
            for val in nums:
                subarr_sum += val
                if subarr_sum > given_subarr_sum:
                    k+=1
                    subarr_sum=val
            return m >= k
                
        
        l, r = max(nums)-1, sum(nums)+1
        while r-l > 1:
            mid = l+(r-l)//2
            if check(mid): r=mid
            else: l=mid
        return r