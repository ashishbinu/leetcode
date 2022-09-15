class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3: return 0
        pr = [True] * (n//2)
        pr[0] = False
        
        for i in range(3,n,2):
            if pr[i//2]:
                for j in range(i*i,n,i):
                    if j%2: pr[j//2] = False
            
        return sum(pr) + 1