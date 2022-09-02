class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # iterative
        if n < 1: return False
        while n%3==0 and n>1: n//=3
        return n == 1
            
        # # recursive
        # if n == 1: return True
        # if n%3 != 0 or n < 1: return False
        # return self.isPowerOfThree(n//3)
        