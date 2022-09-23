class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        count = 1
        m_cnt = int(n > 0)
        print(nums)
        for i in range(1,n):
            if nums[i-1] + 1 == nums[i]:
                count += 1
            elif nums[i-1] == nums[i]:
                continue
            else:
                count = 1
            m_cnt = max(m_cnt,count)
        return m_cnt