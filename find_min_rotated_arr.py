# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

# (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

# Find the minimum element.

# You may assume no duplicate exists in the array.

# Test Cases:
# Input: [3,4,5,1,2] 
# Output: 1

# Input: [4,5,6,7,0,1,2]
# Output: 0

def find_min(nums):

    if len(nums) == 1:
        return nums[0]

    min_ = nums[0]
    for i in range(1, len(nums)):
        current_min = nums[i]
        min_ = min(min_, nums[i])
    
    return min_

# print(find_min([3,4,5,1,2]))
# print(find_min([4,5,6,7,0,1,2]))
# print(find_min([1]))
# print(find_min([1,2]))

def find_pivot(nums):
    # pivot = None

    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            return i+1
    return 0


def find_min2(nums):

    if len(nums) == 1:
        return nums[0]

    pivot_i = find_pivot(nums)

    min_ = nums[pivot_i]
    for num in nums[pivot_i:]:
        current_min = num
        min_ = min(min_, num)
    
    return min_
print(find_min2([3,4,5,1,2]))
print(find_min2([4,5,6,7,0,1,2]))
print(find_min2([1]))
print(find_min2([1,2]))

