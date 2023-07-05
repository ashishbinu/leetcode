class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        mem = set()
        
        nums.sort()
        for i in range(n-2):
            l,r = i+1,n-1
            while l < r:
                a,b,c = nums[l], nums[r], nums[i]
                if a + b == -c:
                    if (a,b,c) not in mem:
                        ans.append([a,b,c])
                    mem.add((a,b,c))
                    l +=1 
                    r -=1
                elif a + b > -c: r -= 1
                else: l += 1
        
        return ans
        