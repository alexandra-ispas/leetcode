class Solution:
    def merge(self, nums1, m, nums2, n):
        # Start from the end to avoid overwriting elements
        i = m - 1  # Last element in nums1
        j = n - 1  # Last element in nums2
        k = m + n - 1  # Last position in nums1

        # Merge from the back
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        # If there are remaining elements in nums2, copy them
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1


def test_merge():
    solution = Solution()
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3

    solution.merge(nums1, m, nums2, n)
    assert nums1 == [1, 2, 2, 3, 5, 6]


if __name__ == "__main__":
    test_merge()
    print("Test passed!")
