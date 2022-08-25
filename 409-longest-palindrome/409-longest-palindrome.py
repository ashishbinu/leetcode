class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = {}
        for v in s:
            if v not in counter: counter[v] = 0
            counter[v] += 1
        
        res = 0
        flag = False
        for k,v in counter.items():
            if v%2 == 0:
                res += v
                counter[k] -= v
            else:
                res += v - 1
                counter[k] -= v - 1
                flag = True
        if flag: res += 1
            
        return res