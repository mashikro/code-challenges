# Prompt: Write a function which finds an integer that appears more than 
# once in our list. (If there are multiple duplicates, you only need to 
# find one of them.)

# Test Case:
# Input: [1,5,6,7,8,4,3,1,4]
# Output: 1 or 4

def find_duplicate(lst):

    count = {}

    for num in lst:
        if num not in count:
            count[num] =1
        else:
            count[num] +=1


    for k, v in count.items():
        print('k', k)
        if v > 1: 
            return k


# print(find_duplicate([1,5,6,7,8,4,3,1,4]))


# or even simpler let's use a set()

def find_repeat(numbers):
    numbers_seen = set()
    for number in numbers:
        if number in numbers_seen:
            return number
        else:
            numbers_seen.add(number)

    # Whoops--no duplicate
    raise Exception('no duplicate!')

#both are O(n) time and space

def find_dups(lst):
    lst.sort()

    for i in range(len(lst)-1):
        if lst[i] == lst[i+1]:
            return lst[i]

    raise Exception('no duplicate!')

# print(find_dups([1,5,6,7,8,4,3,1,4]))

#Runtime: O(n log n) time and O(1) space
# but since we sorted in place, that may cause problems elsewhere

def find_repeat2(numbers):
    floor = 1
    ceiling = len(numbers) - 1

    while floor < ceiling:
        # Divide our range 1..n into an upper range and lower range
        # (such that they don't overlap)
        # Lower range is floor..midpoint
        # Upper range is midpoint+1..ceiling
        midpoint = floor + ((ceiling - floor) // 2)
        lower_range_floor, lower_range_ceiling = floor, midpoint
        upper_range_floor, upper_range_ceiling = midpoint+1, ceiling

        # Count number of items in lower range
        items_in_lower_range = 0
        for item in numbers:
            # Is it in the lower range?
            if item >= lower_range_floor and item <= lower_range_ceiling:
                items_in_lower_range += 1

        distinct_possible_integers_in_lower_range = (
            lower_range_ceiling
            - lower_range_floor
            + 1
        )
        if items_in_lower_range > distinct_possible_integers_in_lower_range:
            # There must be a duplicate in the lower range
            # so use the same approach iteratively on that range
            floor, ceiling = lower_range_floor, lower_range_ceiling
        else:
            # There must be a duplicate in the upper range
            # so use the same approach iteratively on that range
            floor, ceiling = upper_range_floor, upper_range_ceiling

    # Floor and ceiling have converged
    # We found a number that repeats!
    return floor

print(find_repeat2([1,5,6,7,8,4,3,1,4]))


# Runtime: O(1) space and O(n log n) time
        





