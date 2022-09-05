class Solution:
    def hammingWeight(self, n: int) -> int:
        
        # runs only the number of 1 times
        res = 0
        while n:
            # n - 1 reduces a single 1 from the n and creates other ones on the right side which will be removed by and op with n
            n &= n-1
            res += 1
        
        return res
        
        # res = 0
        # while n:
        #     res += n & 1
        #     n = n>>1
        # return res
    
        # convert to binary string [bin() - O(logn)]
        # return sum([int(x) for x in bin(n)[2:]])
    
    