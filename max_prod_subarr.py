# prompt: Given an integer array nums, find the contiguous subarray within an 
# array (containing at least one number) which has the largest product.

# Test Case: 
# Input: [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.

# Input: [2]
# Output: 2

def find_max_product(nums):
    if len(nums) == 0:
        return 0
    if len(nums) <2:
        return nums[0]
    
    current_max = nums[0]
    current_min = nums[0]
    final_max = nums[0]

    for i in range(1, len(nums)):

        temp_current_max = current_max

        current_max = max(max(current_max*nums[i], current_min*nums[i]), nums[i])
        current_min = min(min(temp_current_max*nums[i], current_min*nums[i]), nums[i])
        final_max = max(current_max, final_max)

        print('current_max', current_max)
        print('current_min', current_min)
        print('FINAL', final_max)

    return final_max


print(find_max_product([2,3,-2,4])) #6
print(find_max_product([2])) #2

print(find_max_product([-2,3,-4])) #24

print(find_max_product([-4,-3])) #12

# Runtime: O(n) time and O(1) space


















def find_max_product2(nums):
    positiveArray = [0] * len(nums) 
    negativeArray = [0] * len(nums)
    if nums[0] > 0:
        positiveArray[0] = nums[0]
    else:
        if len(nums) == 1:
            return nums[0]
        negativeArray[0] = nums[0]
    for i in range(1,len(nums)):
        if nums[i] < 0:
            positiveArray[i] = negativeArray[i-1]*nums[i]
            negativeArray[i] = min(nums[i],positiveArray[i-1]*nums[i])
        if nums[i] > 0:
            positiveArray[i] = max(nums[i],positiveArray[i-1]*nums[i])
            negativeArray[i] = negativeArray[i-1]*nums[i]
    return max(positiveArray)