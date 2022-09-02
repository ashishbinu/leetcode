class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n < 1: return False
        while n%4==0 and n>1: n//=4
        return n == 1