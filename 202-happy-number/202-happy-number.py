class Solution:
    def isHappy(self, n: int) -> bool:
        def sum_of_digit_squares(n):
            s = 0
            while n:
                n,d = divmod(n,10)
                s += d * d
            return s
                
        memo = set()
        while n != 1:
            memo.add(n)
            n = sum_of_digit_squares(n)
            if n in memo: return False
        return True
            