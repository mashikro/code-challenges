# Propt: Implement an algorithm to determine if a str has all unique chars. 
# What if you connect use additional data structures

# Testcase: 
# input = 'masha'
# output = False

# input = 'abc'
# output = True

def is_unique(s):

    for letter in s:
        if s.count(letter) > 1:
            return False
    return True

print(is_unique('masha'))
print(is_unique('abc'))