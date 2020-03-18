# Prompt: 
# You're working with an intern that keeps coming to you with JavaScript code that 
# won't run because the braces, brackets, and parentheses are off. To save you both 
# some time, you decide to write a braces/brackets/parentheses validator.

# Test Cases:
# "{ [ ] ( ) }" should return True
# "{ [ ( ] ) }" should return False
# "{ [ }" should return False

def bracket_validator(s):
    brackets = {'(': ')',
                '{': '}',
                '[':']'}

    stack_ = []

    for item in s:
        if item in brackets:
            stack_.append(item)
        elif item in brackets.values():
            if not stack_:
                return False
            else:
                x = stack_.pop() #opener
                if item != brackets[x]: 
                    return False
    return stack_ == []

print(bracket_validator("{[]()}")) #True
print(bracket_validator("{[(])}")) #False
print(bracket_validator("{[}")) #False
print(bracket_validator("(])"))