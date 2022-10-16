class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        # Given graph is a valid star so common vertex between any two edge is center
        a,b = edges[0]
        c,d = edges[-1]
        return a if a==c or a==d else b