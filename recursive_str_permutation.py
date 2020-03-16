# Prompt: Write a recursive function for generating all permutations of an input 
# string. Return them as a set.

# Don't worry about time or space complexity—if we wanted efficiency we'd write an iterative version.

# To start, assume every character in the input string is unique.

# Your function can have loops—it just needs to also be recursive.

# Test Case: 
# Input: 'abc'
# 3!=3*2*1 = 6
# Output: {'abc', 'cba', 'bac', 'cab', 'acb', 'bca'}


# takes a single-element string (x) and a longer string s and returns list
# of strings, each one with x merged in a different position.
def merge_positions(first, s):
    '''Puts first in different positions in s'''
    ret = []
    for i in range(len(s)+1):
        m = s[:i] + first + s[i:]
        ret.append(m)
    return ret

# print(merge_positions("x", "abc"))

def get_permutations(string):
    '''Returns len(string)! string permutations recursively'''
    def pr(x):
        '''Custom printer func'''
        print("["+string+"] "+str(x))

    pr('---------------------')

    if len(string) <= 1:
        return set([string])

    first = string[0] # first element of string
    rest = string[1:]
    allperms = set()
    
    pr('first:'+first)
    pr("rest="+rest)

    for s in get_permutations(rest):
        pr("permutation of rest: "+s)
        merges = merge_positions(first, s)
        pr("merges:"+str(merges))
        for item in merges:
            allperms.add(item)
    
    pr("length of allperms: "+str(len(allperms)))
    return allperms

print(get_permutations('xabc'))  #4*3*2*1=24




