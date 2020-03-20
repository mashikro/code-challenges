# Prompt:write a recursive function that takes a list of numbers and 
# returns the maximum number in the list.

def find_max_recursively(lst):

    if not lst:
        raise Exception('Empty List')
    if len(lst)<=1:
        return lst[0]
    
    mid = len(lst)//2
    first_half = lst[:mid]
    second_half = lst[mid:]

    res1=find_max_recursively(first_half)
    res2=find_max_recursively(second_half)

    if res1<res2:
        return res2
    return res1

   

# print(find_max_recursively([1,4,5,3,6])) #6
# print(find_max_recursively([5,3,1,4])) #5


#Runtime of algo is depth of recursion OR have many recurive calls made O(n)

def find_max_recursively_2(lst):

    if not lst:
        raise Exception('Empty List')
    if len(lst)<=1:
        return lst[0]

    num1 = lst[0]

    num2 = find_max_recursively_2(lst[1:])

    if num1<num2:
        return num2
    return num1

print(find_max_recursively_2([1,4,5,3,6]))