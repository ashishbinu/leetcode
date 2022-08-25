class Solution:
    def longestPalindrome(self, s: str) -> int:
        # 1 pass - time - O(n) , space - O(n)
        
        hashset = set()
        res = 0
        for v in s:
            if v not in hashset:
                hashset.add(v)
            else:
                hashset.remove(v)
                res += 2
                
        if len(hashset) != 0: res += 1
        return res
        
        # # 2 pass solution
        # # time - O(n) , space - O(n)
        # counter = {}
        # for v in s:
        #     if v not in counter: counter[v] = 0
        #     counter[v] += 1
        # 
        # res = 0
        # flag = False
        # for k,v in counter.items():
        #     if v%2 == 0:
        #         res += v
        #     else:
        #         res += v - 1
        #         flag = True
        # if flag: res += 1
        #     
        # return res