# Given a sorted array nums, remove the duplicates in-place such that each element
# appear only once and return the new length.

# Do not allocate extra space for another array, you must do this by modifying the 
# input array in-place with O(1) extra memory.

# Given nums = [1,1,2],

# Your function should return length = 2, with the first two elements of nums being 
# 1 and 2 respectively.

# It doesn't matter what you leave beyond the returned length.

def remove_duplicate_in_place(nums):
    i = 0

    while i < len(nums)-1:
        if nums[i] == nums[i+1]:
            nums.pop(i)  #use the index to remove item
            i -=1 #everytime you remove list gets shorter so decrement to avoud Index out of range error. 
        i +=1

    return len(nums) #could also return i+1

# nums = [1,1,2]
# print(nums)
# print('-----')
# print(remove_duplicate_in_place(nums))
# print(nums)

# nums2=[0,0,1,1,1,2,2,3,3,4]
# nums2 = [-1,0,0,0,0,3,3]
# print(nums2)
# print('-----')
# print(remove_duplicate_in_place(nums2))
# print(nums2)









