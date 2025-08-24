class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        k = 0
        while i < len(nums):
            if nums[i] != val:
                nums[k] = nums[i]
                k = k + 1
            i = i + 1

        return k


def test_remove_element():
    solution = Solution()
    nums = [3, 2, 2, 3]
    val = 3

    k = solution.removeElement(nums, val)
    assert k == 2
    assert nums[:k] == [2, 2]


if __name__ == "__main__":
    test_remove_element()
    print("Test passed!")
