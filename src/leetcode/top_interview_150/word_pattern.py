class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        mappings = {}
        words = list(filter(bool, s.split(" ")))

        if len(pattern) != len(words):
            return False

        i = 0

        while i < len(pattern):
            ch = pattern[i]

            if ch in mappings.keys():
                value = mappings[ch]
                if value != words[i]:
                    return False
            elif words[i] in mappings.values():
                return False
            mappings[ch] = words[i]

            i += 1
        return True
