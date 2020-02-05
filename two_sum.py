# Problem
# Given an array of integers, return indices of the two numbers such that they add 
# up to a specific target.

# You may assume that each input would have exactly one solution, and you may not 
# use the same element twice.

#Ex test case

# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1]


def find_two_sum(nums, target):

    index_1 = None
    index_2 = None

    for i in range(len(nums)):
        looking_for = target - nums[i]
        if looking_for in nums[(i+1):]:
            index_1 = i
            break
    
    for i in range(len(nums)):
        if (nums[i] == looking_for) and (i != index_1):
            index_2 = i

    return [index_1, index_2]
# runtime: O(n2)+O(n) = O(n^2)

# print(find_two_sum([3,2,3], 6)) #[0,2]
# print(find_two_sum([2, 7, 11, 15], 9)) #[0, 1]
# print(find_two_sum([3,2,4], 6)) #[1,2]


def find_two_sum2(nums, target):

    seen = {}

    for i in range(len(nums)):
        looking_for = target - nums[i]

        if looking_for in seen: 

            return[seen[looking_for], i]

        else:
            seen[nums[i]] = i
    return []

#runtime is O(n)
print(find_two_sum2([3,2,4], 6)) #[1,2]
print(find_two_sum2([3,2,3], 6)) #[0,2]
print(find_two_sum2([2, 7, 11, 15], 9)) #[0, 1]






