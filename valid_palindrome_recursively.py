# Prompt: write a recursive function, is_palindrome, that takes a string and 
# returns a boolean true if the input string is a palindrome, otherwise false.

def is_palindrome(string_):
    #base case
    if len(string_)<= 1:
        return True
        
    #fail fast
    if string_[0] != string_[-1]: 
        return False
        
    #coming from either ends
    return is_palindrome(string_[1:-1])

print(is_palindrome('hannah'))
print(is_palindrome('applea'))