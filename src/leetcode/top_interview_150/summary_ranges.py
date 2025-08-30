class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """

        result = []

        i = 0
        while i < len(nums):

            start = nums[i]
            range_l = nums[i]

            while start + 1 in nums:
                start += 1

            range_r = start
            if range_l == range_r:
                result.append(str(range_l))
            else:
                result.append(str(range_l) + "->" + str(range_r))
            i += (start - range_l) + 1

        return result
