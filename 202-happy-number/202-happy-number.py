class Solution:
    def isHappy(self, n: int) -> bool:
        def next(n): # sum of square of digit function
            s = 0
            while n:
                n,d = divmod(n,10)
                s += d * d
            return s
        
        # time - O(n), space - O(1)
        
        s = f = n
        while 1:
            s = next(s)        # s = s.next
            f = next(next(f))  # f = f.next.next
            if s == f: break
            
        return f == 1
                
        # # time - O(n), space - O(n)
        # memo = set()
        # while n != 1:
        #     memo.add(n)
        #     n = next(n)
        #     if n in memo: return False
        # return True
            