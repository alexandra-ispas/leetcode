class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        iterations = 0
        while True:
            i = 0
            result = 0
            while n > 0:
                result += (n % 10) ** 2
                n = n / 10
            if result == 1:
                return True
            n = result
            iterations += 1
            if iterations == 10:
                return False
        return False
