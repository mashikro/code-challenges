# Prompt:
# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, 
# find the one that is missing from the array.

# Test Case:
# Input: [3,0,1]
# Output: 2

# Input: [9,6,4,2,3,5,7,0,1]
# Output: 8

def find_missing_num(lst):
    
    largest = max(lst)
  
    all_numbers = range(largest+2)

    for num in all_numbers:
        if num not in lst:
            return num 


# print(find_missing_num([3,0,1])) #2
# print(find_missing_num([9,6,4,2,3,5,7,0,1])) #8
# print(find_missing_num([1])) #0 
# print(find_missing_num([0])) #1
# print(find_missing_num([0,1,2]))  #3


def find_missing(lst):
    '''Uses hash set'''

    num_set = set(lst)
    n = len(lst) + 1
    for number in range(n):
        if number not in num_set:
            return number


print(find_missing([1])) #0 
print(find_missing([0])) #1
print(find_missing([0,1,2]))  #3



