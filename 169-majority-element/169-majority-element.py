class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = {}
        res,count = 0,0
        for v in nums:
            if v not in counter: counter[v] = 0
            counter[v] += 1
            if counter[v] > count:
                count = counter[v]
                res = v
        return res    
    
        # # Boyer Moore algorithm - https://www.youtube.com/watch?v=7pnhv842keE
        # # time - O(n), space - O(1)
        # res = count = 0
        # for i in nums:
        #     if not count:
        #         res,count = i,1
        #         continue
        #     if i != res:
        #         count -= 1
        #     else:
        #         count += 1
        #         
        # return res
        
        # counter = Counter(nums)
        # return counter.most_common(1)[0][0]
        