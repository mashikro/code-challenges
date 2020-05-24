# Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

# Calling next() will return the next smallest number in the BST.

# In computer programming, an iterator is an object that enables a programmer to traverse a container, 
# particularly lists. This is the Wikipedia definition of an iterator. Naturally, the easiest way to 
# implement an iterator would be on an array like container interface. So, if we had an array, all 
# we would need is a pointer or an index and we could easily implement the two required functions 
# next() and hasNext().

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


############### Approach 1: Flattening the BST into an arr using inorder traversal (left, root, right)
class BSTIterator_:

    def __init__(self, root):

         # Array containing all the nodes in the sorted order
        self.nodes_sorted = []
        
        # Pointer to the next smallest element in the BST
        self.index = -1
        
        # Call to flatten the input binary search tree
        self._inorder(root)
        
    def _inorder(self, root):
        if not root:
            return
        self._inorder(root.left)
        self.nodes_sorted.append(root.val)
        # print(self.nodes_sorted)
        self._inorder(root.right)

    def next(self):
        """
        @return the next smallest number
        """

        self.index += 1
        return self.nodes_sorted[self.index]
        
    def hasNext(self):
        """
        @return whether we have a next smallest number
        """

        return self.index + 1 < len(self.nodes_sorted)


############### Approach 2: Controlled Recursion with a stack
# Initialize an empty stack S which will be used to simulate the inorder traversal for 
# our binary search tree. Note that we will be following the same approach for inorder traversal 
# as before except that now we will be using our own stack rather than the system stack. 
# Since we are using a custom data structure, we can pause and resume the recursion at will.

class BSTIterator:

    def __init__(self, root):

        # Stack for the recursion simulation
        self.stack = []
        
        # Remember that the algorithm starts with a call to the helper function
        # with the root node as the input
        self._leftmost_inorder(root)
        
    def _leftmost_inorder(self, root):
        # For a given node, add all the elements in the leftmost branch of the tree
        # add it to the stack.
        while root:
            print('root', root)
            self.stack.append(root)
            print('self.stack', self.stack)
            root = root.left
            print('new root', root)


    def next(self):
        """
        @return the next smallest number
        """

        # Node at the top of the stack is the next smallest element
        topmost_node = self.stack.pop()
        
        # Need to maintain the invariant. If the node has a right child, call the 
        # helper function for the right child
        if topmost_node.right:
            self._leftmost_inorder(topmost_node.right)
        return topmost_node.val
        
    def hasNext(self):
        """
        @return whether we have a next smallest number
        """

        return len(self.stack) > 0


# Test Code

root = TreeNode(7)
root.left = TreeNode(3)
root.right = TreeNode(15)
root.right.left = TreeNode(9)
root.right.right = TreeNode(20)


# Your BSTIterator object will be instantiated and called as such:
obj = BSTIterator(root)
param_1 = obj.next()
print(param_1)
param_2 = obj.hasNext()
print(param_2)

