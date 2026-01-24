class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        items = filter(bool, path.split("/"))

        stack = []

        for item in items:
            if item == ".":
                continue
            if item == "..":
                # if you are in the root, 'cd ..' will have no effect
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(item)

        return "/" + "/".join(stack)
