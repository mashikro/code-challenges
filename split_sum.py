# Prompt: From Facebook production engineer role:
# Given a non-empty array containing only positive integers, find if the array can be 
# partitioned into two subsets such that the sum of elements in both subsets is equal.

# Note:
# Each of the array element will not exceed 100.
# The array size will not exceed 200.

# Example 1:

# Input: [1, 5, 11, 5]

# Output: true

# Explanation: The array can be partitioned as [1, 5, 5] and [11].

def split_sum(lst):

    if len(lst) < 2:
        return False

    target = sum(lst)/2
    # print('target',target)

    lst.sort(reverse=True)
    # print('lst.sort()', lst)


    sum_1 = 0
    sum_2 = 0

    # print('sum_1', sum_1)
    # print('sum_2', sum_2)

    i = 0
    while i < len(lst): 
        looking_for_1 = target - sum_1
        looking_for_2 = target - sum_2
        if (sum_1 < sum_2):
            if (sum_1 < target):
                if looking_for_1 in lst:
                    sum_1 += looking_for_1
                    lst.remove(looking_for_1)
                    i -=1 #list became shorter
                else:
                    sum_1+=(lst[i]) #if looking_for not in lst add next available
        
        else: 
            if (sum_2 < target):
                if looking_for_2 in lst:
                    sum_2 += looking_for_2
                    lst.remove(looking_for_2)
                    i-=1
                else:
                    sum_2+=(lst[i])
        i+=1
      
    return sum_1 == sum_2

print(split_sum([3,3,3,4,5])) #True
print(split_sum([1,2,3,4,5,6,7])) # True
print(split_sum([1, 5, 11, 5])) #True
print(split_sum([1])) #False
print(split_sum([1, 2, 3, 5])) #False
print(split_sum([[2,2,3,5]])) #False




