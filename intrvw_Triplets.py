"""
Code
Testcase
Test Result
Test Result


15. 3Sum
Attempted
Medium
Topics
Companies
Hint
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

"""

class Solution:
    def __init__(self, nums):
        self.nums = nums

    def sumThree(self):
        n = self.nums
        sortNum = sorted(self.nums)
        triplets = []

        for i in range(len(sortNum) - 2):
            if i>0 and nums[i] == nums[i-1]:
                continue


            left,right = i=1 , len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total < 0:
                    

nums = [-1,0,1,2,-1,-4] 
obj = Solution(nums)
print(obj.sumThree())
