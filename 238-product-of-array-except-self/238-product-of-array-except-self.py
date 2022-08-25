class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prod_arr = [0] * n
        rev_prod_arr = [0] * n
        prod_arr[0] = nums[0]
        rev_prod_arr[-1] = nums[-1]
        
        for k in range(1,n):
            prod_arr[k] = nums[k] * prod_arr[k-1]
        for k in reversed(range(n-1)):
            rev_prod_arr[k] = nums[k] * rev_prod_arr[k+1]
            
        res = [0] * n
        res[0] = rev_prod_arr[1]
        for k in range(1,n-1):
            res[k]  = prod_arr[k-1] * rev_prod_arr[k+1]
            
        res[-1] = prod_arr[-2]
        return res
            