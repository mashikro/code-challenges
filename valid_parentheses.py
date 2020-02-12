# Prompt: Given a string containing just the characters '(', ')', '{', '}', '[' and ']', 
# determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.

# Note that an empty string is also considered valid.

# Test Case:
# Input: "()"
# Output: true

# Input: "()[]{}"
# Output: true

# Input: "(]"
# Output: false

def valid_parens(s):

    if len(s) == 0:
        return True
    if len(s) % 2 != 0:
        return False

    parens = {')':'(',
            ']':'[',
            '}':'{'}

    stack_list = [] #python list being treated like a stack

    for char in s:

        if char in parens.values():
            stack_list.append(char)

        elif char in parens: #looks at keys only
            if stack_list:
                if parens[char] == stack_list[-1]:
                    stack_list.pop()
            else:
                return False

    if len(stack_list) < 1:
        return True
    return False

print(valid_parens('')) 
print(valid_parens('()'))
print(valid_parens('()[]{}'))

print(valid_parens('(]')) #false
print(valid_parens("([)]")) #false
print(valid_parens("(])")) #false


#Runtime: O(n)









