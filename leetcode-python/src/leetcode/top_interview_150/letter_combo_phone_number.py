class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits or len(digits) == 0:
            return []

        result = []

        mapping = {
            2: ["a", "b", "c"],
            3: ["d", "e", "f"],
            4: ["g", "h", "i"],
            5: ["j", "k", "l"],
            6: ["m", "n", "o"],
            7: ["p", "q", "r", "s"],
            8: ["t", "u", "v"],
            9: ["w", "x", "y", "z"],
        }

        def backtrack(i, current):
            if i == len(digits):
                result.append(current)
                return

            letters = mapping[int(digits[i])]
            for l in letters:
                backtrack(i + 1, current + l)

        backtrack(0, "")
        return result
