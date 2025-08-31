class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []

        operations = ["+", "-", "*", "/"]

        for t in tokens:
            if t not in operations:
                stack.append(int(t))
            else:
                right = stack.pop()
                left = stack.pop()
                if t == "+":
                    stack.append(left + right)
                elif t == "-":
                    stack.append(left - right)
                elif t == "*":
                    stack.append(left * right)
                elif t == "/":
                    stack.append(int(float(left) / float(right)))
        return stack.pop()
