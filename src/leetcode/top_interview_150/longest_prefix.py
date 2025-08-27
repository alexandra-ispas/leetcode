class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        # i = 0
        # while i < min([len(s) for s in strs]):
        #     chr = strs[0][i]
        #     if all([s[i] == chr for s in strs]):
        #         i += 1
        #     else:
        #         break
        # return strs[0][:i]

        strs.sort()

        first = strs[0]
        last = strs[len(strs) - 1]

        i = 0
        while i < min(len(first), len(last)):
            if first[i] != last[i]:
                break
            else:
                i += 1
        return first[:i]
