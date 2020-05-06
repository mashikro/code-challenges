# Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

# Note:

# Given target value is a floating point.
# You are guaranteed to have only one unique value in the BST that is closest to the target.

# closest = min(current.val, closest, key = lambda x: abs(target - x)) 
        # key = lambda x: abs(target - x) is an anonymous func and helps min() choose the min bases 
        # smallest diff between current.val and target OR closest and target


# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def find(root, target):

    current = root
    closest = root.val

    while current:
        x = abs(current.val - target)
        y = abs(closest - target)

        if x<y: #looking for the smallest difference 
            closest = current.val
        else:
            closest = closest
        

        if target < current.val:
            current = current.left

        else:
            current = current.right

    return closest

