## Problem1 (https://leetcode.com/problems/sort-colors/)

class Solution:
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        low = 0
        mid = 0
        high = len(nums)-1

        while mid <= high:
            if nums[mid] == 0:
                nums[mid], nums[low] = nums[low],nums[mid]
                mid += 1
                low += 1

            elif nums[mid] == 1:
                mid += 1

            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1

        return nums


sol = Solution()
nums = [2,0,2,1,1,0]
print(sol.sortColors(nums))