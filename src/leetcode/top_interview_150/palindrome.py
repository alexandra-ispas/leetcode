class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        reverse = 0
        x1 = x
        while x1 > 0:
            reverse *= 10
            reverse += x1 % 10
            x1 /= 10

        if x < 0:
            reverse *= -1
        return x == reverse
