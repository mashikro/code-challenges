# Prompt: Given an array of strings, group anagrams together.
# All inputs will be in lowercase.
# The order of your output does not matter.

# TestCase:
# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]


def signature(s):

    ret = list(s)
    ret.sort() 
    return ''.join(ret)

# print(signature('bbaacc'))


def group_anagrams(strs):
    
    sigs = [signature(word) for word in strs]
    # print(sigs)

    words = {} #key==sig, value == word

    for i in range(len(strs)):
        if not sigs[i] in words:
            words[sigs[i]] = [strs[i]]
        else:
            words[sigs[i]].append(strs[i])
    # print(words)


    return list(words.values())


print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

# Runtime of fn signature: O(n log n)
# Runtime group_anagrams: O(n) + O(n log n) + O(n) + O(n) --> O(n log n) time
# Runtime: sigs - O(n) + words O(n) --> O(2n) space