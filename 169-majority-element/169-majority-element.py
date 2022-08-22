class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Boyer Moore algorithm - https://www.youtube.com/watch?v=7pnhv842keE
        res = count = 0
        
        for i in nums:
            if i != res:
                if not count:
                    res = i
                    count = 1
                    continue
                count -= 1
            else:
                count += 1
                
        return res
        
        # counter = Counter(nums)
        # return counter.most_common(1)[0][0]
        