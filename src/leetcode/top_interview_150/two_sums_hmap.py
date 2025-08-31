class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        numbers = {}

        i = 0
        while i < len(nums):
            to_find = target - nums[i]
            if to_find in numbers:
                return [i, numbers[to_find]]
            numbers[nums[i]] = i
            i += 1
