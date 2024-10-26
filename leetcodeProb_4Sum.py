"""
4SUM Probolem:


Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.


"""


def four_sum(nums, target):
    nums.sort()  # Sort the array to make it easier to avoid duplicates
    n = len(nums)
    result = set()  # Use a set to avoid duplicate quadruplets

    for i in range(n - 3):
        for j in range(i + 1, n - 2):
            left, right = j + 1, n - 1
            while left < right:
                current_sum = nums[i] + nums[j] + nums[left] + nums[right]
                if current_sum == target:
                    result.add((nums[i], nums[j], nums[left], nums[right]))
                    left += 1
                    right -= 1
                    # Skip duplicates
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif current_sum < target:
                    left += 1
                else:
                    right -= 1

            # Skip duplicates for j
            while j + 1 < n - 2 and nums[j] == nums[j + 1]:
                j += 1

        # Skip duplicates for i
        while i + 1 < n - 3 and nums[i] == nums[i + 1]:
            i += 1

    return list(map(list, result))  # Convert set of tuples back to list of lists

# Example usage:
nums = [1, 0, -1, 0, -2, 2]
target = 0
output = four_sum(nums, target)
print(output)
