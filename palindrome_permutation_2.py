# Prompt: Write an efficient function that checks whether any permutation 
# of an input string is a palindrome. 

# Test Cases:
# "civic" should return True
# "ivicc" should return True
# "civil" should return False
# "livci" should return False


def check_palindrome_permutation(s):

    if len(s) == 0:
        return True
    
    odd_char = set()
    
    for char in s:
        if char not in odd_char:
            odd_char.add(char)
        else:
            odd_char.remove(char)

    # if len(odd_char) <=1:
    #     return True
    # return False

    return len(odd_char) <=1
print(check_palindrome_permutation('civvic'))
print(check_palindrome_permutation('civic'))
print(check_palindrome_permutation("civil")) #False
print(check_palindrome_permutation("livci"))

#RUNTIME:
# O(n) time and space