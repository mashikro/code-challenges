# Given a linked list, remove the n-th node from the end of list and return its head.

# Example:

# Given linked list: 1->2->3->4->5, and n = 2.

# After removing the second node from the end, the linked list becomes 1->2->3->5.

#Given n will always be valid.

# I think this can be done in one pass using 2 runners. 

def remove_nth_node_from_end(head, n):

    length = 0

    start = Node(0)
    start.next = head

    current = head

    while current:
        length +=1
        current = current.next

    length = length-n
    current = start
    while length > 0:
        length -=1
        current = current.next

    current.next.val, current.next.next = current.next.next.val, current.next.next.next

    return start.next
#Runtime: O(n) time but 2 passes and O(1) space
def remove_nth_node_from_end_faster(head, n):

    start = Node(0)
    start.next = head

    first = start
    second = start

    while n >= 0:
        first = first.next 
        n-=1


    while first:
        first = first.next
        second = second.next

    second.next = second.next.next #second is 3, thus second.next is 4, which we skip by making it second.next.next which is 5

    return start.next
#Runtime: O(n) time one pass and O(1) space
# Testing code:

class Node():
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList():
    def __init__(self, head):
        self.head = head

    def print_(self):

        current = self.head

        while current:
            print(current.val)
            current = current.next

one = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)
five = Node(5)

one.next = two
two.next= three
three.next = four
four.next = five

ll = LinkedList(one)
print('---------')
ll.print_()

print('----FUNC CALL-----')
# print(remove_nth_node_from_end(one, 2))
print(remove_nth_node_from_end_faster(one, 2))


print('---------')
ll.print_()



