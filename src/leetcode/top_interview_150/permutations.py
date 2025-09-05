class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        visited = set()

        def backtrack(curr):
            if len(curr) == len(nums):
                result.append(curr)
                return

            for i in range(len(nums)):
                if i not in visited:
                    visited.add(i)
                    backtrack(curr + [nums[i]])
                    visited.remove(i)

        backtrack([])
        return result
