class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """

        i = 0
        new_start = newInterval[0]
        new_end = newInterval[1]
        result = []
        while i < len(intervals) and intervals[i][0] < new_start:
            result.append(intervals[i])
            i += 1

        if len(result) == 0 or result[-1][1] < new_start:
            result.append(newInterval)
        else:
            prev = result[-1]
            prev[1] = max(prev[1], new_end)

        while i < len(intervals):
            prev = result[-1]
            if prev[1] < intervals[i][0]:
                result.append(intervals[i])
            else:
                result[-1][1] = max(prev[1], intervals[i][1])
            i += 1
        return result
