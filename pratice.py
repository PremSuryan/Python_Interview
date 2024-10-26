# class Solution:
#     def __init__(self,nums_value) -> None:
#         self.nums_value = nums_value
        
#     def sum(self):
#         return nums_value
    

# nums_value =  [-1,0,1,2,-1,-4]
# obj= Solution(nums_value)
# obj.sum(nums_value)


class Solution:
    def __init__(self, nums_value) -> None:
        self.nums_value = nums_value

    def three_sum(self):
        nums = sorted(self.nums_value)  # Sort the array
        triplets = []

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # Skip duplicates

            left, right = i + 1, len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    triplets.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

        return triplets

# Example usage
nums_value = [-1, 0, 1, 2, -1, -4]
obj = Solution(nums_value)
output = obj.three_sum()
print(output)  # Output: [[-1, -1, 2], [-1, 0, 1]]  -4 -4 1 , -4 -1 0
