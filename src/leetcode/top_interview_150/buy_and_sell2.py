class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        i = 1
        max_final = 0

        while i < len(prices):
            if prices[i-1] < prices[i]:
                max_final += prices[i] - prices[i-1]
            i += 1
        return max_final
