class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        cnt = 0
        N = len(flowerbed)
        for k in range(N):
            if flowerbed[k] == 0 and (k==0 or flowerbed[k-1] == 0) and (k==N-1 or flowerbed[k+1] == 0):
                flowerbed[k] = 1
                cnt += 1
        return cnt >= n
        