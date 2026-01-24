class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        result = []
        while i >= 0 or j >= 0:
            if i >= 0:
                carry += int(a[i])
                i -= 1

            if j >= 0:
                carry += int(b[j])
                j -= 1

            result.append(str(carry % 2))
            carry = carry // 2

        if carry == 1:
            result.append("1")

        return "".join(reversed(result))
