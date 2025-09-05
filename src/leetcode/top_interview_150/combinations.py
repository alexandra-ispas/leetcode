class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        result = []

        def backtrack(i, current):
            if len(current) == k:
                result.append(current)
                return

            for num in range(i, n + 1):
                backtrack(num + 1, current + [num])

        backtrack(1, [])
        return result
