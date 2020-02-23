# Prompt: Given all three lists, write a function to check that my service is first-come, 
# first-served. All food should come out in the same order customers requested it.

# Test Case:
# Input:
# Take Out Orders: [1, 3, 5]
# Dine In Orders: [2, 4, 6]
# Served Orders: [1, 2, 3, 5, 4, 6]
# Output: True

def check_order(take_out_orders, dine_in_orders, served_orders):
    # print('take_out_orders', take_out_orders)
    # print('dine_in_orders', dine_in_orders)

    for i in range(len(served_orders)):
        if take_out_orders and served_orders[i] == take_out_orders[0]:
            take_out_orders.pop(0)
            # print('take_out_orders', take_out_orders)
        elif dine_in_orders and served_orders[i] == dine_in_orders[0]:
            dine_in_orders.pop(0)
            # print('dine_in_orders', dine_in_orders)
        else:
            return False
    return True


# print(check_order([1, 3, 5], [2, 4, 6], [1, 2, 3, 5, 4, 6])) #True
# print(check_order([1, 3, 5], [2, 4, 6], [1, 2, 4, 6, 5, 3])) #False

#Runtime: O(n^2)



def check_order_recursively(take_out_orders, dine_in_orders, served_orders):


    # Base case
    if len(served_orders) == 0:
        return True

    if take_out_orders and served_orders[0] == take_out_orders[0]:
        return check_order_recursively(take_out_orders[1:], dine_in_orders, served_orders[1:])

    elif dine_in_orders and served_orders[0] == dine_in_orders[0]:
        return check_order_recursively(take_out_orders, dine_in_orders[1:], served_orders[1:])

    else:
        return False

# print(check_order_recursively([1, 3, 5], [2, 4, 6], [1, 2, 3, 5, 4, 6])) #True
# print(check_order_recursively([1, 3, 5], [2, 4, 6], [1, 2, 4, 6, 5, 3])) #False


#Runtime: O(n^2) because we have 2 list slices in the return statements

def check_order_faster(take_out_orders, dine_in_orders, served_orders):

    out_index = 0
    in_index = 0
    served_index = 0

    for order in served_orders:
        if out_index < len(take_out_orders) and take_out_orders[out_index] == served_orders[served_index]:
            out_index +=1
            served_index +=1
        elif in_index < len(dine_in_orders) and dine_in_orders[in_index] == served_orders[served_index]:
            in_index +=1
            served_index +=1
        else:
            return False

    return True
        


print(check_order_faster([1, 3, 5], [2, 4, 6], [1, 2, 3, 5, 4, 6])) #True
print(check_order_faster([1, 3, 5], [2, 4, 6], [1, 2, 4, 6, 5, 3])) #False  

# Runtime: O(n) time and space     

