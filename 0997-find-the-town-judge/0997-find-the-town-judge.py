class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # judge is the only node in graph with OUTegree 0 and INegree n - 1
        
        # time - O(E+V), space - O(V)
        in_out = [0] * (n+1) # indegree - outdegree
        
        for a,b in trust:
            in_out[a] -= 1
            in_out[b] += 1
            
        for i in range(1,n+1):
            if in_out[i]==n-1: return i
        return -1
        
        # # time - O(E+V), space - O(2V)
        # IN = [0] * (n+1)
        # OUT= [0] * (n+1)
        # 
        # for a,b in trust:
        #     OUT[a] += 1
        #     IN[b] += 1
        #     
        # for i in range(1,n+1):
        #     # this proves only node with this property exists
        #     if IN[i]==n-1 and OUT[i]==0: return i
        # return -1