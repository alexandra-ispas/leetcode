class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        mapping = {")": "(", "}": "{", "]": "["}

        stack = []

        for ch in s:
            if ch not in mapping:
                stack.append(ch)
            else:
                if len(stack) == 0:
                    return False
                item = stack.pop()
                if mapping[ch] != item:
                    return False

        return len(stack) == 0
