# Propt: Given two strings write a method to decide if one is permutation of the other

# test case:
# input1: 'apple'
# input2: 'alepp'
# output: True

# input1: 'apple'
# input2: 'alpp'
# output: False

def check_permutation(s1,s2):

    if len(s1) == len(s2):
        # list_s1 = list(s1) #O(n)
        for l in s2: #O(n)
            if l not in s1: #O(n)
                return False
        return True

    return False

print(check_permutation('apple', 'alepp')) 
print(check_permutation('apple', 'alpp'))
print(check_permutation('apple', 'alppw')) #False

# runtime: O(n)+ O(n)*O(n) -> O(n^2+n)
# runtime: O(n)*O(n) -> O(n^2)


#from solution that uses python's built in Counter()
# O(N)
from collections import Counter


def check_permutation(str1, str2):
    if len(str1) != len(str2):
        return False
    counter = Counter()
    for c in str1:
        counter[c] += 1
    for c in str2:
        if counter[c] == 0:
            return False
        counter[c] -= 1
    return True