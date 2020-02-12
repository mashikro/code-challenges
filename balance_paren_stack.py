# Deques are a generalization of stacks and queues (the name is pronounced “deck” and is short 
# for “double-ended queue”). 
# Deques support thread-safe, memory efficient appends and pops from either side of 
# the deque with approximately the same O(1) performance in either direction
from collections import deque 

# OR use a class 

# class Stack(object):
#     """Stack implemented using a list."""

#     def __init__(self):
#         self._stack = []

#     def push(self, item):
#         """Add item to top."""

#         self._stack.append(item)

#     def pop(self):
#         """Remove top item."""

#         return self._stack.pop()

#     def peek(self):
#         """Return, but don't remove, top item."""

#         return self._stack[-1]

#     def is_empty(self):
#         """Is the stack empty?"""

#         return not self._stack


def is_parens_balanced(symbols):

    stack=deque()

    for char in symbols:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack: #if there is nothing in there return False
                return False
            else:
                stack.pop()

    if stack: #if there is something, return False
        return False
    return True


print(is_parens_balanced('((3+4)-(1+2))/(1+1)')) #True
print(is_parens_balanced('((3+4)-(1+2))/(1+1')) #False

print(is_parens_balanced(''))

