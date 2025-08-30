class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        mappings = {}

        i = 0
        while i < len(nums):
            n = nums[i]
            if n in mappings.keys():
                value = mappings[n]
                if abs(i - value) <= k:
                    return True
            mappings[n] = i
            i += 1
            print(mappings)
        return False
