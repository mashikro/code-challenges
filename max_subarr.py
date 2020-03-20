# Prompt: Given an integer array nums, find the contiguous subarray 
# (containing at least one number) which has the largest sum and return its sum.

# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.

def find_max_subarr(lst):

    if len(lst) < 1:
        return 0

    if len(lst) == 1:
        return lst[0]

    largest = lst[0]

    for i in range(len(lst)):
        temp_num = 0 
        for j in range(len(lst)-i):
            temp_num += (lst[j+i])

            if temp_num > largest:
                largest = temp_num

    return largest


print(find_max_subarr([-2,1,-3,4,-1,2,1,-5,4])) #6
print(find_max_subarr([2,4,5,-4,2])) #11
print(find_max_subarr([-2,-1])) #-1

# Runtime: slow: O(n^2)

def find_max_subarr3(nums):
    
    maxsum,currentsum = nums[0],nums[0]
 
    for num in nums[1:]:
        currentsum = max(num,currentsum+num)
        maxsum = max(maxsum,currentsum)
       
    
    return maxsum

print(find_max_subarr3([-2,1,-3,4,-1,2,1,-5,4])) #6
print(find_max_subarr3([2,4,5,-4,2])) #11
print(find_max_subarr3([-2,-1])) #-1

# Runtime: O(n)



