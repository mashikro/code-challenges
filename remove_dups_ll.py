# Propt: Write code to remove duplicates from unsorted linked list

# input: 1,3,5,2,1,5,6,2,2,3
# output: 1,3,5,2,6

class Node(object):

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):

        return '<Node at: {}>'.format(self.data)


class LinkedList(object):

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node

        if self.tail:
            self.tail.next = new_node

        self.tail = new_node

    def traverse(self):

        current=self.head

        while current is not None:

            print(current.data)
            current = current.next


    def remove_dups(self):

        counts = {}

        current = self.head
        new_ll = LinkedList()

        while current is not None:

            if current.data not in counts:
                counts[current.data] = 1
                new_ll.append(current.data)
            else:
                counts[current.data] += 1

            current = current.next

        return new_ll

    def __repr__(self):

        return '<Linked List head: {}, tail {}>'.format(self.head, self.tail)


node_1=Node(1)
node_2=Node(2)
node_11=Node(1)
node_111=Node(1)
node_22=Node(2)
node_3=Node(3)
node_6=Node(6)

node_1.next=node_2
node_2.next=node_11
node_11.next = node_111
node_111.next= node_22
node_22.next = node_3
node_3.next=node_6

linked_lst = LinkedList()
linked_lst.head=node_1
linked_lst.tail=node_6

new_ll = linked_lst.remove_dups()



