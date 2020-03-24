# Given an array, rotate the array to the right by k steps, where k is non-negative.

# Input: [1,2,3,4,5,6,7] and k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]

def rotate_arr(lst, step):

    new_lst=[0]*len(lst)

    i = -1 #start from back of lst
    for num in lst:
        new_lst[i+step] = lst[i]
        i-=1 #update i

    return new_lst

# print(rotate_arr([1,2,3,4,5,6,7], 3)) # [5,6,7,1,2,3,4]

# runtime: O(n) time and space

def rotate_arr_in_place(nums, k):
    #here k acts like the rotation point where everything after k needs to be placed before 
    # and everything before k needs to be placed after it
    k = k%len(nums) 
    tmp = nums[-k:] # here we save nums that's going to come first in rotated arr so we dont lose them
    nums[k:] = nums[:-k]  # here we place nums before k to come after it
    nums[:k] = tmp #here we place nums at the end of lst to begining 


arr = [1,2,3,4,5,6,7]
rotate_arr_in_place(arr, 3)
print(arr)


# easier to see rotation here:
# k %= len(nums)
# nums[k:], nums[:k] = nums[:-k], nums[-k:]

