# prompt: Given an integer array nums, find the contiguous subarray within an 
# array (containing at least one number) which has the largest product.

# Test Case: 
# Input: [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.

# Input: [2]
# Output: 2

def find_max_product(nums):

    if len(nums) < 2:
        return nums[0]

    current = nums[0]
    max_ = nums[0]


    for num in nums[1:]:

        current = max(num, (current * num))
        max_ = max(max_, current)

    return max_

print(find_max_product([2,3,-2,4])) #6
print(find_max_product([2])) #2

print(find_max_product([-2,3,-4])) #24

print(find_max_product([-4,-3])) #12