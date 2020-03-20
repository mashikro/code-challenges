# prompt: Given sorted (inc order) arr with unique int elemts write an algo to 
# create a binary search tree with min height
# test case
# input: [1,2,3,4,5,6,7]


class BSTNode(object):

    def __init__(self,data, left=None, right=None):
        self.data=data
        self.left=left
        self.right=right

    def __repr__(self):

        return "<BST Node:{}>".format(self.data)

    def insert_left(self, new_node):

        if self.left == None:
            self.left = new_node
 

    def insert_right(self, new_node):

        if self.right == None:
            self.right = new_node
 

    def print_(self, depth=0):
        if self.left:
            self.left.print_(depth+1)
        print('  '*depth, self.data)
        if self.right:
            self.right.print_(depth+1)


def make_min_tree(nums):
    '''Takes in arr of nums and returns a BST node'''

    if not nums:
        return None
    
    mid = len(nums)//2 
    
    first_half = nums[:mid]
    second_half = nums[mid+1:]

    root = BSTNode(nums[mid])
    r1 = make_min_tree(first_half)
    r2 = make_min_tree(second_half)


    root.insert_left(r1)
    root.insert_right(r2)

    return root



# make_min_tree([1,2,3]).print_()
# print('********')
make_min_tree([1,2,3,4,5,6,7]).print_()







