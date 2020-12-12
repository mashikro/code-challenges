# https://leetcode.com/problems/linked-list-cycle/

def has_cycle(head_node):

    current = head_node
    seen = set()

    while current:
        if current in seen:
            return True
        seen.add(current)
        current = current.next
    return False


class Node(object):
    
    def __init__(self, data):
        self.data = data
        self.next = None

three = Node(3)
two = Node(2)
zero = Node(0)
four = Node(4)

three.next = two
two.next = zero
zero.next = four
four.next = two

print(has_cycle(three)) 
# O(n) checking in set() is O(1)