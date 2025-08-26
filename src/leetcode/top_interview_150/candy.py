class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """

        minim = min(ratings)
        candy = len(ratings)

        i = 1
        while i < len(ratings):
            if ratings[i] == ratings[i-1]:
                i += 1
                continue

            # peak
            peak = 0
            while i < len(ratings) and ratings[i] > ratings[i - 1]:
                peak += 1
                candy += peak
                i += 1

            # valley
            valley = 0
            while i < len(ratings) and ratings[i] < ratings[i - 1]:
                valley += 1
                candy += valley
                i += 1

            candy -= min(peak, valley)

        return candy

