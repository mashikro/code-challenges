# Prompt: Write a function to find the 2nd largest element in a binary search tree. 
# Fair to assume: the largest element is simply the "rightmost" element, so we dont even need to check the left subtree
    


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


def find_largest(root_node):
    '''Recursive helper func for finding the rightmost aka largest element'''

    current = root_node
    while current:
        if not current.right:
            return current.data
        current = current.right

#takes into consideration if largest node has a left subtree where the 2nd largest may be
def find_second_largest(root_node):
    if (root_node is None or
            (root_node.left is None and root_node.right is None)):
        raise ValueError('Tree must have at least 2 nodes')

    current = root_node
    while current:
        # Case: current is largest and has a left subtree
        # 2nd largest is the largest in that subtree
        if current.left and not current.right:
            return find_largest(current.left)

        # Case: current is parent of largest, and largest has no children,
        # so current is 2nd largest
        if (current.right and
                not current.right.left and
                not current.right.right):
            return current.data

        current = current.right

#make a BST for testing:
#should return 8 w/o the last 3 nodes
five_root = BinaryTreeNode(5) 
three = five_root.insert_left(3)
eight = five_root.insert_right(8)
seven = eight.insert_left(7)
twelve = eight.insert_right(12)
#should return 11 with nodes below
ten = twelve.insert_left(10)
nine = ten.insert_left(9)
eleven = ten.insert_right(11)

print(find_second_largest(five_root)) 




#does not consider if the largest node has a left subtree
def find_2nd_largest_element_in_BST(root_node):

    if root_node == None:
        raise ValueError('This tree is empty')

    if (not root_node.left) and (not root_node.right):
        raise ValueError('Only one node in Tree. Need at least 2')


    current = root_node
    # taking a greedy algo approach here and have these two var to keep track of 
    # largest and second_largest and get things done in one pass
    largest = root_node.data
    second_largest = 0


    while current.right != None:

        print('current.right',current.right)
        print('current.right.data',current.right.data)
        print('largest', largest)
        print('second_largest', second_largest)


        if current.right.data > largest:
            second_largest = largest
            largest = current.right.data
            current = current.right


    return second_largest


