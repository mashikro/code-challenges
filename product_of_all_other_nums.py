# Prompt: Write a function get_products_of_all_ints_except_at_index() that takes a list 
# of integers and returns a list of the products

# Input:[1, 7, 3, 4]
# Output:[84, 12, 28, 21]

def find_product_except_self(lst):

    #need to keep track of prod from left and right side of lst
    L, R, ret = [0] * len(lst), [0] * len(lst), [0] * len(lst)

    L[0]=1

    for i in range(1, len(lst)):
        L[i] = L[i-1] * lst[i-1]

    R[-1]=1

    for i in reversed(range(len(lst)-1)):
        R[i] = R[i+1] * lst[i+1]


    for i in range(len(lst)):
        ret[i] = L[i] * R[i]

    return ret


print(find_product_except_self([1, 7, 3, 4]))