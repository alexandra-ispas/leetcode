class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """

        length = sys.maxsize
        i = 0
        j = 0
        sum = 0

        while j < len(nums):
            sum += nums[j]
            while sum >= target:
                length = min(length, j - i + 1)
                sum -= nums[i]
                i += 1
            j += 1

        if length == sys.maxsize:
            return 0
        return length
