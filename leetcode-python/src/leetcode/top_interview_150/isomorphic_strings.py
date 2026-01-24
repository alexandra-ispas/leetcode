class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) != len(t):
            return False

        replacements = {}

        i = 0
        while i < len(s):
            if replacements.get(s[i], None) is not None:
                if replacements[s[i]] != t[i]:
                    return False
            elif t[i] in replacements.values():
                return False
            replacements[s[i]] = t[i]
            i += 1
        return True
