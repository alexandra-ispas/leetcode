class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        mapping = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        if len(s) == 1:
            return mapping.get(s, "Wrong input")

        result = 0

        for i in range(len(s) - 1):
            curr = mapping[s[i]]
            next = mapping[s[i + 1]]

            if curr < next:
                result -= curr
            else:
                result += curr
        return result + mapping[s[len(s) - 1]]
