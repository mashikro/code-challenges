# Prompt: write a recursive function that takes a
# list of numbers and returns the sum of all the numbers in the list.

def find_sum_recursively(lst):
    # base case
    if not lst:
        return 0
    if len(lst) <= 1:
        return lst[0]


    return lst[0]+find_sum_recursively(lst[1:])


print(find_sum_recursively([1,2,3,4,5,6])) #21
print(find_sum_recursively([])) #21