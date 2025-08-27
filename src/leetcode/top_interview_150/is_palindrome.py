import re


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        new_s = re.sub(r"[^a-zA-Z0-9]", "", s).lower()

        return new_s == new_s[::-1]
