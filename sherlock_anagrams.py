# https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps

# Traverse all possible substrings within string
# Check if any two substrings of equal length are anagrams

import collections
# from itertools import combinations 

def is_anagram(s):
    c = collections.Counter(s)
    odd_one = True
    for v in c.values():
        print('v=', v)
        if v%2!=0:
            if odd_one==True:
                odd_one = False
                print("found odd one")
                print("odd_one=", odd_one)
            else:
                return False

    return True

# print(is_anagram("racecar"))
# print(is_anagram("hannah"))
# print(is_anagram("banana"))


def generate_all_canonical_substrings(s):
    substrings = {}

    for i in range(len(s)):
        ss = ''
        for j in range(i, len(s)):
            ss += s[j]
            # x = sorted(ss)
            x = "".join(sorted(ss))
            # print("here:")
            # print(x)
            if x not in substrings:
                substrings[x] = 1
            else:
                substrings[x] +=1
    return substrings


def sherlock_and_anagrams(s): # O(N^^2)
    substrings = generate_all_canonical_substrings(s) #O(N^2)
    # print(substrings)
    ret = 0
   
    for v in substrings.values():
        x = (v*(v-1))/2
        ret += x

    return int(ret)





# O(N**2) + O(Z**2) == O(N+Z)**2
print(sherlock_and_anagrams("mom")) #2
# print("=======================================")
# print(sherlock_and_anagrams2("mom"))
# print(sherlock_and_anagrams("abba")) #4
# print(sherlock_and_anagrams("abcd")) #0

# print(sherlock_and_anagrams("kkkk")) #10



