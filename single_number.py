# Given a non-empty array of integers nums, every element appears twice except for one. 
# Find that single one.

# Input: nums = [2,2,1]
# Output: 1

# Input: nums = [4,1,2,1,2]
# Output: 4

def find_single_num(nums):
    import collections
    count=collections.Counter(nums)

    for k, v in count.items():
        if v == 1:
            return k

# print(find_single_num([2,2,1]))
# print(find_single_num([4,1,2,1,2]))



# Follow up: Could you implement a solution with a linear runtime complexity and 
# without using extra memory?

def find_single_num2(nums):
    '''Implemented using math'''

    return 2*sum(set(nums)) - sum(nums)


print(find_single_num2([2,2,1]))
# ex: 
# set([2,2,1]) -> [2,1] 
# 2*sum([2,1]) -> 6
# 6 - sum(2,2,1) => 1
print(find_single_num2([4,1,2,1,2]))




