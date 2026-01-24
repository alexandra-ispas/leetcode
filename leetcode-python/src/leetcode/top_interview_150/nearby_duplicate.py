class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        mappings = {}

        for i, n in enumerate(nums):
            if n in mappings and i - mappings[n] <= k:
                return True
            mappings[n] = i

        return False
