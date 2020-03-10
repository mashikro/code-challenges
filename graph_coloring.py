# Prompt: Given an undirected graph ↴ with maximum degree D, find a graph coloring using at most 
# D+1 colors.

class GraphNode:

    def __init__(self, label):
        self.label = label
        self.neighbors = set()
        self.color = None

a = GraphNode('a')
b = GraphNode('b')
c = GraphNode('c')
d = GraphNode('d')
e = GraphNode('e')
f = GraphNode('f')
g = GraphNode('g')


a.neighbors.add(b)
a.neighbors.add(d)

b.neighbors.add(a)
b.neighbors.add(c)
b.neighbors.add(d)

c.neighbors.add(b)
c.neighbors.add(f)
c.neighbors.add(g)

d.neighbors.add(e)
d.neighbors.add(a)
d.neighbors.add(b)

f.neighbors.add(g)
f.neighbors.add(c)

g.neighbors.add(f)
g.neighbors.add(c)

e.neighbors.add(d)


graph = [a, b, c, d, e, f, g]
colors = ['pink', 'red', 'green', 'blue']

def color_graph(graph, colors):
    for node in graph:
        if node in node.neighbors:
            raise Exception('Legal coloring impossible for node with loop: {}'.format(node.label))
        
        print('node', node.label)

        # Get the node's neighbors' colors, as a set so we
        # can check if a color is illegal in constant time
        illegal_colors = set([
            neighbor.color
            for neighbor in node.neighbors
            if neighbor.color
        ])
        
        print('illegal', illegal_colors)

        # Assign the first legal color
        for color in colors:
            if color not in illegal_colors:
                node.color = color
                print('color-assigned', color)
                break

color_graph(graph, colors)

# Runtime: O(N + M) where N is len(graph) and M is number of edges