class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [1] * len(nums)

        suff = 1
        for i in range(len(nums)):
            result[i] *= suff

            suff *= nums[i]

        pref = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= pref
            pref *= nums[i]

        return result


