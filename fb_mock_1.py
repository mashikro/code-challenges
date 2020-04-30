# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

# Note: For the purpose of this problem, we define empty string as valid palindrome.

# Example 1:

# Input: "A man, a plan, a canal: Panama"
# Output: true
# Example 2:

# Input: "race a car"
# Output: false

def format_str(s):
    ret = []
    
    for l in s:
        if l.isalnum():
            ret.append(l.lower())
            
    return ret
def is_palindrome2(s):     
    formatted_s = format_str(s)
    
    i = 0
    j = -1
    
    while i < len(formatted_s):
        if formatted_s[i] != formatted_s[j]:
            return False
        i+=1
        j-=1
    
    return True

# print(is_palindrome("race a car"))
# print(is_palindrome("0P"))

####################### NEXT PROBLEM 

# Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

# Example 1:

# Input: "aba"
# Output: True
# Example 2:

# Input: "abca"
# Output: True
# Explanation: You could delete the character 'c'.
# Note:

# The string will only contain lowercase characters a-z. The maximum length of the string is 50000.
def is_palindrome(s, i, j):
    
    while i < j:
        if s[i] != s[j]:
            return False
        i+=1
        j-=1
    
    return True 
def valid_palindrome(s):
    

    i = 0
    j = len(s)-1

    while i < j:
        if s[i] == s[j]:
            i+=1
            j-=1
        else:
            return is_palindrome(s, i, j-1) or is_palindrome(s, i+1, j)

    return True

# print(valid_palindrome('aba')) #True
# print(valid_palindrome('abca')) #True
# print(valid_palindrome("abc")) #False
# print(valid_palindrome("deeee")) #True
# print(valid_palindrome("tebbem")) #False
# print(valid_palindrome("cbbcc")) #True
# print(valid_palindrome("eccer")) #True
# print(valid_palindrome("ebcbbececabbacecbbcbe")) #True





























