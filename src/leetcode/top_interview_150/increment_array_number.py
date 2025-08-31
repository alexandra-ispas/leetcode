class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        carry = 1
        i = len(digits) - 1
        while i >= 0:
            dig = (digits[i] + carry) % 10
            carry = (digits[i] + carry) / 10
            digits[i] = dig
            i -= 1
        if carry != 0:
            return [carry] + digits
        return digits
