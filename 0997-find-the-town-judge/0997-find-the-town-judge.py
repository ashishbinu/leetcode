class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # judge is the only node in graph with outdegree 0 and indegree n - 1
        ind = [0] * (n+1)
        outd= [0] * (n+1)
        
        for a,b in trust:
            outd[a] += 1
            ind[b] += 1
            
        cnt = res = 0
        for i in range(1,n+1):
            if ind[i]==n-1 and outd[i]==0:
                cnt += 1
                res = i
        return res if cnt == 1 else -1 