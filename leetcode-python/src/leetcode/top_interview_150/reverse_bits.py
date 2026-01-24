class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        for i in range(32):
            bit_i = (n >> i) & 1
            res = res | (bit_i << (31 - i))
        return res
