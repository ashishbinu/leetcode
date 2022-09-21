class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cntr = defaultdict(int)
        for x in nums: cntr[x] += 1
        res = list(cntr.items())
        res.sort(key=lambda x: x[1],reverse=True)
        return [res[i][0] for i in range(k)]