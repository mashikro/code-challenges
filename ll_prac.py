# Make a Node class

class Node(object):

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return "<Node: {}>".format(self.data)

# Make some instances of Node

apple = Node('apple')
print(apple)
berry = Node('berry')
cherry = Node('cherry')

apple.next=berry
berry.next=cherry

# Make a LL class with the traverse method

class LinkedList(object):

    def __init__(self):
        self.head = None
        self.tail = None


    def traverse_list(self):

        print('=======')
        current = self.head

        while current is not None:
            print(current.data)
            current = current.next


# Make LL instances 

fruit_ll = LinkedList()

fruit_ll.head = apple
fruit_ll.tail = cherry

fruit_ll.traverse_list()