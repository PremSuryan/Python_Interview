"""Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

 

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

"""




class Solution:
    def __init__(self, nums: list[int], k: int):
        """
        Do not return anything, modify nums in-place instead.
        """
        self.nums = nums
        self.k =k

    def rotate(self):
        # rotate_num = []
        num1 = self.nums
        n = len(num1) 

        # self.k %= n  # Normalize k to avoid unnecessary rotations
        print(self.nums[-self.k:])   #[5,6,7]
        self.nums[:] = self.nums[-self.k:] + self.nums[:-self.k] 
        



input_nums = [1, 2, 3, 4, 5, 6, 7]
k=3
obj = Solution(input_nums, k)
obj.rotate()  
print(obj.nums) 

