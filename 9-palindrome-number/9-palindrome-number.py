class Solution:
    def isPalindrome(self, x: int) -> bool:
        d = 0
        tmp = x
        while tmp > 0:
            tmp,r = divmod(tmp,10)
            d *= 10
            d += r
        return x == d
    
        # return str(x) == str(x)[::-1]