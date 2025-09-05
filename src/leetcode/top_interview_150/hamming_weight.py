class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """

        # counter = 0
        # while n > 0:
        #     if n % 2 == 1:
        #         counter += 1

        #     n /= 2

        # return counter

        counter = 0
        while n:
            counter += n & 1
            n = n >> 1

        return counter
