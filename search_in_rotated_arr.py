# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

# (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

# You are given a target value to search. If found in the array return its index, 
# otherwise return -1.

# You may assume no duplicate exists in the array.

# Your algorithm's runtime complexity must be in the order of O(log n).

# Test Cases: 
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4

# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1

def find_pivot(nums):
    pivot = 0
    for i in range(len(nums)-1):
        if nums[i] < nums[i+1]:
            pivot+=1
        else:
            pivot+=1
            break

    return pivot

# print(find_pivot([4,5,6,7,0,1,2]))

def search_rotated_arr(nums, target):
    if len(nums) == 1:
        if nums[0] == target:
            return 0
    if len(nums) > 1:
        pivot = find_pivot(nums)
    else:
        return -1

    # print('pivot',pivot)
    beg_of_list = nums[pivot:]
    end_of_list = nums[:pivot]

    # print('beg_of_list', beg_of_list)
    # print('end_of_list',end_of_list)


    to_search = None
    len_to_add = 0

    if nums[0] < nums[-1]: #in the case when nums is sorted
        to_search = nums
    elif target < end_of_list[0]:
        to_search = beg_of_list 
        len_to_add = len(end_of_list)
    else:
        to_search = end_of_list
    

    # print('to_search',to_search)
    # print('len_to_add', len_to_add)
    
    for i in range(len(to_search)):
        if to_search[i] == target:
            return len_to_add+i

    return -1




# print(search_rotated_arr([4,5,6,7,0,1,2], 0)) #4
# print(search_rotated_arr([4,5,6,7,0,1,2], 3)) #-1
# print(search_rotated_arr([], 3)) #-1
# print(search_rotated_arr([1], 1)) #0
# print(search_rotated_arr([1,3], 1)) #0
print(search_rotated_arr([3, 1], 1)) #1
print(search_rotated_arr([3, 1], 3)) #0