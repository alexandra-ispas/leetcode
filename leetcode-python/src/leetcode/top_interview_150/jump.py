class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        i = 0
        far = 0

        while i < len(nums):
            if i > far:
                return False
            far = max(far, i + nums[i])

            i += 1
        return True
