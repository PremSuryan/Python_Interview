"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

"""
# Using For LOOP
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):  # Start from i + 1 to avoid using the same element
                if nums[i] + nums[j] == target:
                    return [i, j]  # Return the indices

# Example usage
nums = [2, 7, 11, 15]
target = 9
result = twoSum(nums, target)
print(result)  # Output: [0, 1]

#-------------------------------------------
def twoSum( nums, target):
    d={}
    for i in range(0,len(nums)):
        value=nums[i]
        diff = target-value
        if value not in d:
            d[diff] =i
            print(d[diff]) # 0
        else:
            current_index =i #1
            prev_index=d[value] #0
            return [current_index, prev_index]


nums=[2,7,11,15]
target = 9
print(twoSum(nums, target))
            


        