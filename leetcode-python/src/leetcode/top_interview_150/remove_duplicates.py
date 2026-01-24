class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 1
        i = 1
        k = 0
        while i < len(nums):
            if nums[i] != nums[k]:
                k = k + 1
                nums[k] = nums[i]
            i = i + 1
        return k + 1


def test_remove_duplicates():
    solution = Solution()
    nums = [1, 1, 2]

    k = solution.removeDuplicates(nums)
    assert k == 2
    assert nums[:k] == [1, 2]


if __name__ == "__main__":
    test_remove_duplicates()
    print("Test passed!")
