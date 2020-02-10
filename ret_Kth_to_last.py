# Implement Algorithm to find the kth to last element of a singly linked lst

#setup

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

    def traverse(self):

        current=self.head

        count = 0

        while current is not None:
            count += 1
            print(current.data)
            current = current.next

        return count

    def find_kth_element(self, element):

        length_ll = self.traverse()

        stop_num = length_ll-element
        count = 0
        current=self.head

        while current is not None:
            if count == stop_num:
                return current.data
            count+=1
            current = current.next

    def __repr__(self):

        return '<Linked List head: {}, tail {}>'.format(self.head, self.tail)

apple = Node('apple')
berry = Node('berry')
cherry = Node('cherry')
durian = Node('durian')

apple.next = berry
berry.next = cherry
cherry.next = durian

ll = LinkedList()
ll.head = apple
ll.tail = durian 

ll.find_kth_element(2) #returns 'cherry'



