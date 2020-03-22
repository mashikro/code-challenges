# Prompt: Given a directed Graph, design an algo, to find out wether, there is a route bt 2 nodes

#find route between 2 nodes --> Breadth First Search - finds shortest path
# write a graph method called is_connected()

from collections import deque

class Node():

    def __init__(self, data, connected_to=None):

        if connected_to is None:
            connected_to = set()

        self.data = data
        self.connected_to = connected_to

    def add_neighbor(self, neighbor):

        self.connected_to.add(neighbor)

    def __repr__(self):

        return "<Graph Node:{}>".format(self.data)

class Graph():

    def __init__(self, nodes=None):
        if nodes is None:
            self.nodes = set()
        self.nodes = nodes
        self.num_nodes = 0


    def is_connected(self, node_1, node_2):
        '''Breadth First Search - finds the shortest path bt 2 nodes'''

        if node_1 in node_2.connected_to:
            return True

        possibilities = deque()
        seen = set()

        possibilities.append(node_1)
        seen.add(node_1)
        
        

        while possibilities:
            current_node = possibilities.popleft()

            if current_node == node_2:
                return True

            for n in current_node.connected_to:
                possibilities.append(n)
                seen.add(n)

            for n in seen:
                print(n)
       
        # print('SEEN', seen)
        
        return False


#Test Code for True
#Nodes
one = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)
five = Node(5)

#Add connections
one.add_neighbor(two)
one.add_neighbor(three)
two.add_neighbor(one)
three.add_neighbor(one)
three.add_neighbor(four)
three.add_neighbor(five)



#make graph
g = Graph({one, two, three, four, five})

print(g.is_connected(one, five))

print('**************')
#Test Code for False
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')

a.add_neighbor(b)
a.add_neighbor(c)
b.add_neighbor(c)
# c.add_neighbor(d)


gr = Graph({a,b,c,d})
print(gr.is_connected(a, d))






