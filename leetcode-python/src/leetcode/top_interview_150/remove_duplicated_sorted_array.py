class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 2
        k = 2

        while i < len(nums):
            if nums[i] != nums[k - 2]:
                nums[k] = nums[i]
                k = k + 1
            i = i + 1
        return k
