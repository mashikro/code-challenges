# Prompt:
# You have a singly-linked list ↴ and want to check if it contains a cycle.
# A singly-linked list is built with nodes, where each node has:
#     node.next—the next node in the list.
#     node.value—the data held in the node. For example, if our linked list stores people 
#     in line at the movies, node.value might be the person's name.

# A cycle occurs when a node’s next points back to a previous node in the list. 
# The linked list is no longer linear with a beginning and end—instead, it cycles 
# through a loop of nodes.

# Write a function contains_cycle() that takes the first node in a singly-linked 
# list and returns a boolean indicating whether the list contains a cycle.
# Input: first node
# output: boolen

# test case:
# a > b < > c // c points a
# output: True

class LinkedListNode(object):

    def __init__(self, data):
        self.data = data
        self.next  = None

    def __repr__(self):

        return "<Node at: {}>".format(self.data)

#Runtime O(n) and O(n)space
def contains_cycle(first_node):

    seen = set()

    current = first_node

    while current:
        if current.data in seen:
            return True
        else:
            seen.add(current.data)
            current= current.next

    return False

#Runtime O(n) time and O(1)space
def contains_cycle_v2(first_node):
    '''Two finger algorithm'''

    fast_runner = first_node
    slow_runner = first_node

    while fast_runner is not None and fast_runner.next is not None:
        fast_runner = fast_runner.next.next
        slow_runner = slow_runner.next
        
        if fast_runner == slow_runner:
            return True
            
    return False

# Testing

#true case:
a = LinkedListNode('A')
b = LinkedListNode('B')
c = LinkedListNode('C')

a.next = b
b.next = c
c.next = a

print(a.next) #B
print(b.next) #C
print(c.next) #B

print(contains_cycle(a))
print('----V2------')
print(contains_cycle_v2(a))

# false case:
print('------------------')
one = LinkedListNode(1)
two = LinkedListNode(2)
three = LinkedListNode(3)

one.next = two
two.next = three

print(one.next) #2
print(two.next) #3
print(contains_cycle(one))
print('----V2------')
print(contains_cycle_v2(one))









