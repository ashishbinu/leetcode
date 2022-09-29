class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        min_s = 0
        s = 0
        I = 0
        for j in range(n):
            if j < k:
                s += abs(arr[j] - x)
                min_s = s
            else:
                s += abs(arr[j]-x) - abs(arr[j-k]-x)
                if s < min_s:
                    min_s = s
                    I = j-k+1
        return arr[I:I+k]