class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        def cond(i): return arr[i] > arr[i+1]
        n = len(arr)
        l,r = 0,n-2
        while l+1 < r:
            m = (l+r)//2
            if cond(m): r=m
            else: l=m
        return r
        