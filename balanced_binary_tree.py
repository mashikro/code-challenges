# Prompt: Write a function to see if a binary tree is "superbalanced" 
# (a new tree property we just made up). A tree is "superbalanced" if the difference between 
# the depths of any two leaf nodes is no greater than one.
# So that means:
    # There are more than 2 different leaf depths
    # There are exactly 2 leaf depths and they are more than 1 apart.

class BinaryTreeNode(object):

    def __init__(self, data):
        self.data = data
        self.left  = None
        self.right = None

    def insert_left(self, data):
        self.left = BinaryTreeNode(data)
        return self.left

    def insert_right(self, data):
        self.right = BinaryTreeNode(data)
        return self.right

    #Traditional DFS as a class method
    def depth_first_search(self, data):
        
        to_visit = [self] #stack
        
        while to_visit:
            
            current = to_visit.pop()

            if current.data == data:
                return current 
            
            to_visit.extend(current.children)

#DFS as a external func that takes in a tree root to start.
def is_balanced(tree_root):

    # A tree with no nodes is superbalanced, since there are no leaves!
    if tree_root is None:
        return True

    # We short-circuit as soon as we find more than 2
    depths = []

    # We'll treat this list as a stack that will store tuples of (node, depth)
    to_visit = []
    to_visit.append((tree_root, 0))

    while to_visit:
        # Pop a node and its depth from the top of our stack
        node, depth = to_visit.pop()

        # Case: we found a leaf
        if (not node.left) and (not node.right):
            # We only care if it's a new depth
            if depth not in depths:
                depths.append(depth)

                # Two ways we might now have an unbalanced tree:
                #   1) more than 2 different leaf depths
                #   2) 2 leaf depths that are more than 1 apart
                if ((len(depths) > 2) or
                        (len(depths) == 2 and abs(depths[0] - depths[1]) > 1)):
                    return False
        else:
            # Case: this isn't a leaf - keep stepping down, add left first and then right, check for both! 
            if node.left:
                to_visit.append((node.left, depth + 1))
            if node.right:
                to_visit.append((node.right, depth + 1))

    return True

masha = BinaryTreeNode('masha')
aaron = masha.insert_left('aaron')
ashley = masha.insert_right('ashley')
david = aaron.insert_left('david')
rachel = david.insert_left('rachel')


print(is_balanced(masha)) #w/ ashley its False w/o True


