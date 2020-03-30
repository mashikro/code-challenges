# Your company delivers breakfast via autonomous quadcopter drones. And something 
# mysterious has happened.
# Each breakfast delivery is assigned a unique ID, a positive integer. When one of 
# the company's 100 drones takes off with a delivery, the delivery's ID is added 
# to a list, delivery_id_confirmations. When the drone comes back and lands, the ID 
# is again added to the same list.

# After breakfast this morning there were only 99 drones on the tarmac. One of 
# the drones never made it back from a delivery. We suspect a secret agent from 
# Amazon placed an order and stole one of our patented drones. To track them down, 
# we need to find their delivery ID.

# Given the list of IDs, which contains many duplicate integers and one unique 
# integer, find the unique integer.

# The IDs are not guaranteed to be sorted or sequential. Orders aren't always 
# fulfilled in the order they were received, and some deliveries get cancelled before takeoff.

# input=[1,2,3,4,2,3,4] #1

def find_unique_id(delivery_id_confirmations):

    import collections
    counts = collections.Counter(delivery_id_confirmations)

    for k, v in counts.items():
        if v == 1:
            return k


# print(find_unique_id([1,2,3,4,2,3,4])) #1
# Runtime: O(n) time and space

def find_unique_id2(delivery_id_confirmations):

    seen=set()

    for value in delivery_id_confirmations:
        if value in seen:
            seen.remove(value)
        else:
            seen.add(value)

    if seen:
        print(seen)
        return next(iter(seen)) #returns the next element in seen

    
# print(find_unique_id2([1,2,3,4,2,3,4])) #1

# Runtime: O(n) time and O(m) space

def find_unique_id_bitwise(delivery_ids):
    unique_delivery_id = 0

    for delivery_id in delivery_ids:
        unique_delivery_id ^= delivery_id
        # print(unique_delivery_id)

    return unique_delivery_id


print(find_unique_id_bitwise([1,2,3,4,2,3,4])) #1





