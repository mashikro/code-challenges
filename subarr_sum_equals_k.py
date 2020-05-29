# Given an array of integers and an integer k, you need to find the total number of 
# continuous subarrays whose sum equals to k.

# Example 1:

# Input:nums = [1,1,1], k = 2
# Output: 2


def subarr_sum_(nums, k):
    subarrs = 0
    i = 0 
    j = 1
    current = nums[0]

    while j <= len(nums) and i < j:
        # print('i', i)
        # print('j', j)
        # print('current:', current)
        # print('subarrs:', subarrs)
  
        if current == k:
            subarrs+=1
        if j == len(nums):
            i+=1
            if i<j:
                current = nums[i]
                j=i+1
        else:
            current+=nums[j]
            j+=1        

    return subarrs

# print(subarr_sum([1,1,2,1], 2)) #2


# print(subarr_sum([1,2,1,2,1], 3)) #4
# print(subarr_sum([1,2,3], 3)) #2
# print(subarr_sum([1,2,0,3], 3)) #4


def subarr_sum(nums, k):
    subarrs = 0

    for i in range(len(nums)):
        current = nums[i]
        for j in range(i, len(nums)):
            # print('i', i)
            # print('j', j)
            # print('current', current)
            if current == k:
                subarrs+=1
            if j+1 <len(nums):
                current+=nums[j+1]


    return subarrs


print(subarr_sum([1,1,2,1], 2)) #2
print(subarr_sum([1,2,1,2,1], 3)) #4
print(subarr_sum([1,2,3], 3)) #2
print(subarr_sum([1,2,0,3], 3)) #4
print(subarr_sum([1,2], 3))
