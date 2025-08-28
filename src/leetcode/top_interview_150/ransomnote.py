class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        if len(ransomNote) > len(magazine):
            return False

        r = {}

        for ch in magazine:
            r[ch] = r.get(ch, 0) + 1

        for ch in ransomNote:
            if ch not in r:
                return False
            r[ch] = r.get(ch) - 1
            if r[ch] == 0:
                del r[ch]

        return True
