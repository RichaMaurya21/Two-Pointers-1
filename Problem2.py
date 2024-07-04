## Problem2 (https://leetcode.com/problems/3sum/)

class Solution:
    def threeSum(self, nums):
        res = []
        nums.sort()
        a = 0

        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            l,r = i+1, len(nums) - 1

            while l < r:
                threeSum = nums[i] + nums[l] + nums[r]
                if threeSum == 0:
                    res.append([nums[i] , nums[l] , nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1

                elif threeSum > 0: 
                    r -= 1

                else:
                    l += 1


        return res



sol = Solution()
nums = [-1,0,1,2,-1,-4]
print(sol.threeSum(nums))
            


        


        