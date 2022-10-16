class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        ecnt = defaultdict(int)
        for u,v in edges:
            if u != v:
                ecnt[u] += 1
                ecnt[v] += 1
        return max(ecnt, key=lambda x: ecnt[x])
        