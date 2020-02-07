# Given an array of integers, find if the array contains any duplicates.

# Your function should return true if any value appears at least twice in the array, 
# and it should return false if every element is distinct.

# Input: [1,2,3,1]
# Output: true

def find_duplicates(lst):

    for n in lst:
        if lst.count(n) > 1:
            return True
    return False


print(find_duplicates([1,2,3,1])) # true
print(find_duplicates([1,2,3])) #false
print(find_duplicates([1,1,1,3,3,4,3,2,4,2])) #true

# runtime: 1 for loop: O(n) and hidden if statement .count() has a runtime of O(n) 
# runtime: O(n^2)

def find_duplicates_2(lst):

    counts = {}

    for n in lst:
        if n not in counts:
            counts[n] = 1
        else:
            counts[n] += 1


    for n in list(counts.values()):
        if n > 1:
            return True
    return False


print(find_duplicates_2([1,2,3,1])) # true
print(find_duplicates_2([1,2,3])) #false
print(find_duplicates_2([1,1,1,3,3,4,3,2,4,2])) #true

# runtime: O(n) + O(m) -> O(n+m) -> O(n)