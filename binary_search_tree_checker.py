# Prompt: Write a function to check that a binary tree is a valid binary search tree. 
#     A binary tree is a tree where every node has two or fewer children. 
#     The children are usually called left and right.

#     A binary search tree is a binary tree where the nodes are ordered in a specific way. For every node:
#     The nodes to the left are smaller than the current node.
#     The nodes to the right are larger than the current node.


class BinaryTreeNode(object):

    def __init__(self, data):
        self.data = data
        self.left  = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right


def check_valid_BST(tree_node):

    if tree_node == None: #checks for a tree with no nodes - True bc balanced 
        return True

    if (not tree_node.left) and (not tree_node.right): #checks if root node even has a left and a right subtree. if not, its balanced
        return True

    current = tree_node

    while current:

        if (current.data < current.left.data) or (current.data > current.right.data): #tries to fail fast if left is greater than root OR right is smaller than root
            return False

        # in other cases checks left and right deeper
        return (check_valid_BST(current.left) and check_valid_BST(current.right)) #note how you can have multiple func calls in one return


#make a BST for testing:
#everything below should return True
five_root = BinaryTreeNode(5) 
four = five_root.insert_left(4)
six = five_root.insert_right(6)
three = four.insert_left(3)
eight = four.insert_right(8)
#make it false
seven = six.insert_left(7)
two = six.insert_right(2)

print(check_valid_BST(five_root)) 

# runtime: O(n) time and O(n) space.

  