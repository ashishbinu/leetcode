class Solution:
    def isHappy(self, n: int) -> bool:
        def sum_of_digit_squares(n):
            s = 0
            while n:
                n,d = divmod(n,10)
                s += d * d
            return s
        
        # time - O(n), space - O(1)
        s = f = n
        while f != 1:
            s = sum_of_digit_squares(s)  # s = s.next
            f = sum_of_digit_squares(f)
            f = sum_of_digit_squares(f)  # f = f.next.next
            if s == f and s != 1: return False      # cycle detected
        return True
                
        # # time - O(n), space - O(n)
        # memo = set()
        # while n != 1:
        #     memo.add(n)
        #     n = sum_of_digit_squares(n)
        #     if n in memo: return False
        # return True
            