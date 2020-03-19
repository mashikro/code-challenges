# Prompt: Hooray! It's opposite day. Linked lists go the opposite way today.
# Write a function for reversing a linked list. Do it in place.

# Your function will have one input: the head of the list.

# Your function should return the new head of the list.


class LinkedListNode(object):

    def __init__(self, value):
        self.value = value
        self.next  = None

def reverse(head):
    current = head
    previous_node = None
    next_node = None

    # Until we have 'fallen off' the end of the list
    while current:
        # Copy a pointer to the next element
        # before we overwrite current.next
        next_node = current.next

        # Reverse the 'next' pointer. flips the pointer goes from A->B TO B->A
        current.next = previous_node

        # Step forward in the list
        previous_node = current
        current = next_node
        
    # We return previous_node because when we exit the list, current_node is None. 
    # Which means that the last node we visited—previous_node—was the tail of the original 
    # list, and thus the head of our reversed list.
    return previous_node

def print_(a):

    current = a

    while current:
        print("Node:",current.value)
        current = current.next


#Testing

a = LinkedListNode('A')
b = LinkedListNode('B')
c = LinkedListNode('C')
d = LinkedListNode('D')


a.next = b
b.next = c
c.next = d
print_(a)


print('-----Reversed-----')

print_(reverse(a))







