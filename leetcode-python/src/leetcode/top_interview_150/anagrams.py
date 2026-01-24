class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) != len(t):
            return False

        dictionary_s = {}
        dictionary_t = {}

        i = 0
        while i < len(s):
            dictionary_s[s[i]] = dictionary_s.get(s[i], 0) + 1
            dictionary_t[t[i]] = dictionary_t.get(t[i], 0) + 1
            i += 1
        return dictionary_s == dictionary_t

        # i = 0
        # while i < len(t):
        #     ch = t[i]
        #     if t[i] not in dictionary.keys():
        #         return False
        #     else:
        #         dictionary[ch] = dictionary[ch] - 1
        #         if dictionary[ch] == 0:
        #             del dictionary[ch]
        #     i += 1
        # return True
