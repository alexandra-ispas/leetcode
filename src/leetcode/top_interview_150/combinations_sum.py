class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []

        def backtrack(start, target, current):
            if target == 0:
                result.append(current)
                return

            if target < 0:
                return

            for i in range(start, len(candidates)):
                backtrack(i, target - candidates[i], current + [candidates[i]])

        backtrack(0, target, [])
        return result
