"""
3SUM :

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

"""




def three_sum(nums):
    # a = sorted(nums)  # Step 1: Sort the array output:[]
    print(nums.sort())
    triplets = [] 
    
    for i in range(len(nums) - 2):
        # Skip duplicate elements                               [-1, 0, 1, 2, -1, -4] 
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        a = nums[i]    
        left = i+1
        right = len(nums) - 1  # Step 3: Initialize two pointers 0 1 5 
        
        while left < right:  # Step 4: Check for pairs
            total = nums[i] + nums[left] + nums[right] 
            if total < 0:
                left += 1  # Increase the left pointer to increase total  2 
            elif total > 0:
                right -= 1  # Decrease the right pointer to decrease total 4
            else:
                # Found a triplet
                triplets.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                
                # Skip duplicates for left pointer
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                    
                # Skip duplicates for right pointer
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
                    
    return triplets

# Example usage
nums = [-1, 0, 1, 2, -1, -4]
output = three_sum(nums)
print(output)  # Output: [[-1, -1, 2], [-1, 0, 1]]
