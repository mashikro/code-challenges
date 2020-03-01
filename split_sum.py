# Prompt: From Facebook production engineer role q:split array in such a way that their sum is same 

# Test Case: 
# Input: [1, 5, 4, 3, 2, 5]
# Output: 2 list that sum to 10 each

def split_sum(lst):

    target_sum = sum(lst)/2
    print('target_sum',target_sum)

    lst_1 = []
    lst_2 = []

    for num in lst:

        if sum(lst_1) < target_sum:
            lst_1.append(num)
        else:
            lst_2.append(num)

    return (lst_1, lst_2)

print(split_sum([1, 5, 4, 3, 2, 5]))
