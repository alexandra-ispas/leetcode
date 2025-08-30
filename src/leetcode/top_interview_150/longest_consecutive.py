class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = 0
        nums = set(nums)

        for n in nums:
            if n - 1 not in nums:
                start = n
                cnt = 1
                while start + 1 in nums:
                    cnt += 1
                    start += 1
                length = max(length, cnt)
        return length
