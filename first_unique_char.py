# Given a string, find the first non-repeating character in it 
# and return it's index. If it doesn't exist, return -1. You may assume the string contain only lowercase letters.

# s = "leetcode"
# return 0.

# s = "loveleetcode",
# return 2.

def find_first_unique_char(s):

    count = {}

    for i in range(len(s)):
        if not s[i] in count:
            count[s[i]] = {'i': i, 'c': 1}
        else:
            count[s[i]]['c'] +=1

    # print(count)

    for v in count.values():
        if v['c'] < 2:
            return v['i']

    return -1



print(find_first_unique_char("leetcode")) #0
print(find_first_unique_char("loveleetcode")) #2

# Runtime: O(n) space and O(n+n) time = O(n)

def find_first_unique_char2(s):
    # build hash map : character and how often it appears
    import collections
    
    count = collections.Counter(s) # <---- easy and fast way to do the below but can't customize like I did below
    

    for i in range(len(s)):
        if count[s[i]] == 1:
            return i

    return -1


print(find_first_unique_char2("leetcode")) #0
print(find_first_unique_char2("loveleetcode")) #2

#note that collections.Counter() is much more faster than making my own dict. 


