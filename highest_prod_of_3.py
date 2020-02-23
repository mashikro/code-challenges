# Prompt:
# Given a list of integers, find the highest product you can get from 
# three of the integers. The input list_of_ints will always have at least three integers.

# Test Case:
# Input: [1,2,3,4]
# Output: 24

#does not deal with negatives!
def find_largest_prod(lst):

    lst.sort() 

    largest = 1

    for num in lst[-3:]:
        largest *= num

    return largest

#runtime O(n lg n)

# print(find_largest_prod([1,2,3,4]))
# print(find_largest_prod([2, 4, 1,3]))


def find_largest_prod2(list_of_ints):
    
    if len(list_of_ints) < 3:
        raise ValueError('Less than 3 items!')

    # We're going to start at the 3rd item (at index 2)
    # so pre-populate highests and lowests based on the first 2 items.
    # We could also start these as None and check below if they're set
    # but this is arguably cleaner
    highest = max(list_of_ints[0], list_of_ints[1])
    lowest  = min(list_of_ints[0], list_of_ints[1])
    highest_product_of_2 = list_of_ints[0] * list_of_ints[1]
    lowest_product_of_2  = list_of_ints[0] * list_of_ints[1]

    # Except this one--we pre-populate it for the first *3* items.
    # This means in our first pass it'll check against itself, which is fine.
    highest_product_of_3 = list_of_ints[0] * list_of_ints[1] * list_of_ints[2]


    # Walk through items, starting at index 2, 3rd item in list
    for i in range(2, len(list_of_ints)):
        current = list_of_ints[i]
        
        # Do we have a new highest product of 3?
        # It's either the current highest,
        # or the current times the highest product of two
        # or the current times the lowest product of two
        highest_product_of_3 = max(highest_product_of_3,
                                   current * highest_product_of_2,
                                   current * lowest_product_of_2)

        # Do we have a new highest product of two?
        highest_product_of_2 = max(highest_product_of_2,
                                   current * highest,
                                   current * lowest)

        # Do we have a new lowest product of two?
        lowest_product_of_2 = min(lowest_product_of_2,
                                  current * highest,
                                  current * lowest)

        # Do we have a new highest?
        highest = max(highest, current)

        # Do we have a new lowest?
        lowest = min(lowest, current)

    return highest_product_of_3 

print(find_largest_prod2([2, 4, 1,3])) #24
print(find_largest_prod2([2, 4, 1,3, 5])) #60

#runtime: O(n) time and O(1) additional space.



