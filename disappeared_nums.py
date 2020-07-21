# Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

# Find all the elements of [1, n] inclusive that do not appear in this array.

# Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

# Example:

# Input:
# [4,3,2,7,8,2,3,1]

# Output:
# [5,6]


def find_disappeared_nums___(lst):
    missing = []
    set_=set(lst)
    for num in range(1, len(lst)+1):
        if num not in set_:
            missing.append(num)

    return missing



def find_disappeared_nums(lst):

    ss = set(range(1, len(lst)+1))
    s = set(lst)

    return list(ss-s)

print(find_disappeared_nums([4,3,2,7,8,2,3,1]))
print(find_disappeared_nums([4,3,2,7,8,2,3,1,10,11]))
print(find_disappeared_nums([]))
print(find_disappeared_nums([1,1]))