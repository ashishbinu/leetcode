class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n,N = len(p),len(s)
        res = []
        if n > N: return res
        
        pcnt = {}
        for v in p:
            if v not in pcnt: pcnt[v] = 0
            pcnt[v] += 1
        
        scnt = {} # n length string
        for i in range(n):
            if s[i] not in pcnt: continue
            if s[i] not in scnt: scnt[s[i]] = 0
            scnt[s[i]] += 1
        
        prev_anag = False
        if scnt == pcnt:
            res.append(0)
            prev_anag = True
        for j in range(n,N):
            i = j - n + 1
            if s[i-1] in pcnt: scnt[s[i-1]] -= 1
            if s[j] in pcnt:
                if s[j] not in scnt: scnt[s[j]] = 0
                scnt[s[j]] += 1
            if (prev_anag and s[i-1] == s[j]) or pcnt == scnt:
                res.append(i)
            else:
                prev_anag = False
        return res
            