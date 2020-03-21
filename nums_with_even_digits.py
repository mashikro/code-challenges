# Given an array nums of integers, return how many of them contain an even number of digits.

# Input: nums = [12,345,2,6,7896]
# Output: 2
# Explanation: 
# 12 contains 2 digits (even number of digits). 
# 345 contains 3 digits (odd number of digits). 
# 2 contains 1 digit (odd number of digits). 
# 6 contains 1 digit (odd number of digits). 
# 7896 contains 4 digits (even number of digits). 
# Therefore only 12 and 7896 contain an even number of digits.

def find_nums_with_even_num_digits(nums):

    def is_even_len(n):
        s = str(n)
        if len(s)%2==0:
            return True
        return False

    num_even = 0

    for num in nums:
        if is_even_len(num):
            num_even += 1

    return num_even

print(find_nums_with_even_num_digits([12,345,2,6,7896])) #2
print(find_nums_with_even_num_digits([555,901,482,1771])) #1