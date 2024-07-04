## Problem3 (https://leetcode.com/problems/container-with-most-water/)
class Solution:
    def maxArea(self, height):
        l, r = 0, len(height) - 1
        max_area = 0
        area = 0
        while l < r:
            area = (r-l)* min(height[l],height[r])
            max_area = max(max_area, area)
            if height[l] < height[r]:
                l += 1

            else:
                r -= 1

        return max_area

sol = Solution()
height = [1,8,6,2,5,4,8,3,7]
print(sol.maxArea(height))