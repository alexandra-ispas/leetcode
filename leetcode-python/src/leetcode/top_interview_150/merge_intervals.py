class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """

        intervals = sorted(intervals, key=lambda x: x[0])

        result = []

        i = 1
        current = intervals[0]
        while i < len(intervals):
            next = intervals[i]

            if current[1] < next[0]:
                # nothing common, will not merge
                result.append(current)
                current = next
            else:
                current = [current[0], max(next[1], current[1])]
            i += 1
        result.append(current)
        return result
