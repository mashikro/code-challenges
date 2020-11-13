# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

from collections import Counter

def generate_prefixes(lst):
    prefix = []
    for i in range(len(lst)):
        word = lst[i]
        p = ""
        for j in range(len(word)):
            letter = word[j]
            p+=letter
            prefix.append(p)
        

    return prefix


def find_longest_common_prefix(lst):

    all_possible_prefixes = generate_prefixes(lst)
    print("all_possible_prefixes")
    print(all_possible_prefixes)
    
    count = Counter(all_possible_prefixes)
    print("count")
    print(count)

    x = []
    for k,v in count.items():
        if v == len(lst):
            x.append(k)
    print("x=", x)
    if x:
        return max(x)
    return ""

print(find_longest_common_prefix(["flower","flow","flight"]))
print(find_longest_common_prefix(["dog","racecar","car"]))