class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        strings = filter(bool, s.split(" "))
        strings.reverse()
        return " ".join(strings)
