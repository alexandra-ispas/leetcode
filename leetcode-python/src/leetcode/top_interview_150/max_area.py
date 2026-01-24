class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # length * height
        # (i2-i1)*(j2-j1)

        max_area = 0

        i1 = 0
        i2 = len(height) - 1

        while i1 < i2:
            area = (i2 - i1) * min(height[i2], height[i1])

            if area > max_area:
                max_area = area
            if height[i1] < height[i2]:
                i1 += 1
            else:
                i2 -= 1
            print(max_area)
        return max_area
