# integer numbers and +, *
# 1+2*3+4 -> 11

# tokenize the str 
# have a priority system for * of 2 int(token)

# 1+2*3+4 -> ['1', '+', ...]

#     +
#.  1    +
#      *   4
#.   2   3
#1+6+20


def find_result(lst):
    '''Parses the math exp in one pass but makes in place changes'''
    i = 0
    res = 0
    while i < len(lst):
        if lst[i] == '*':
            temp = int(lst[i-1]) * int(lst[i+1])
            del lst[i-1:i+2]
            lst.insert(i - 1, temp)
        if lst[i] == '+':
            res += int(lst[i-1])
        if i == len(lst)-1:
            res += int(lst[-1])
        i +=1
        
    return res

# lst = ['1', '+', '2', '*', '3', '+', '4']
# print('before', lst)
# print(find_result(lst))
# print('after', lst)

#Runtime:
    # O(n) while loop
    # O(n) 'insert' 
    # O(n) 'del' 
    #--------------
    #O(n^3) time
    #O(1) space

def find_result2(lst):
    '''Parses the math exp in one pass w/o manipulating len of input lst'''

    i = 0
    res = 0
    while i < len(lst):
        if lst[i] == '*':
            temp = int(lst[i-1]) * int(lst[i+1])
            lst[i-1] = 0
            lst[i] = 0
            lst[i+1] = temp
        if lst[i] == '+':
            res += int(lst[i-1])
        if i == len(lst)-1:
            res += int(lst[-1])
        i +=1
        
    return res

lst2 = ['1', '+', '2', '*', '3', '+', '4']
print('before', lst2)
print(find_result2(lst2))
print('after', lst2)

#Runtime: O(n) time and O(1) space