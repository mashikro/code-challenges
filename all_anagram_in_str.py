# Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

# Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

# The order of output does not matter.
# Input:
# s: "cbaebabacd" p: "abc"

# Output:
# [0, 6]

# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".

     

def find_all_anagrams_(s, p):
    import collections
    p_count = collections.Counter(p)
  
    indices = []

    for i in range(len(s)):
        current = []
        for j in range(i, len(s)):
            # print('s[j]:', s[j])
            if i+len(p)<=len(s):
                if len(current) < len(p):
                    current.append(s[j])
                    # print('current:', current)
                if len(current) ==len(p):
                    if collections.Counter(current) == p_count:
                        indices.append(i)
                        # print('indices:', indices)
                        break
    return indices




def find_all_anagrams(s, p):
    import collections
    p_count = collections.Counter(p)
    indices = []
    i = 0
    j = len(p)
    while j <= len(s):
        if collections.Counter(s[i:j]) == p_count:
            indices.append(i)
            
        i+=1
        j+=1
    return indices

print(find_all_anagrams("cbaebabacd", "abc"))
print(find_all_anagrams("abab", "ab")) #[0,1,2]
print(find_all_anagrams("ababababab","aab")) #[0,2,4,6]





