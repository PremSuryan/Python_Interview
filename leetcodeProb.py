"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

"""
def medianArray(nums1, nums2):
    appendArray = nums1.extend(nums2)
    sortingValue = sorted(nums1)
    print(sortingValue)
    n = len(sortingValue)

    if n%2==0:
        med = (sortingValue[n // 2 - 1] + sortingValue[n // 2]) / 2.0
    else:
        med = sortingValue[n // 2]

    return float(med)


nums1 = [1,3]
nums2 = [2]
output = medianArray(nums1, nums2)
print(output)
