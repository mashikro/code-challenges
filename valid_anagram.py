# Given two strings s and t , write a function to determine if t is an anagram of s.

# Test cases:
# Input: s = "anagram", t = "nagaram"
# Output: true

# Input: s = "rat", t = "car"
# Output: false

# An anagram is a word or phrase formed by rearranging the letters of a different 
# word or phrase, typically using all the original letters exactly once. 


def valid_anagram(s, t):
    
    if len(s) == len(t):
        
        counts = {}
        print('counts', counts)
        
        for l in s:
            if l not in counts:
                counts[l] = 1
            else:
                counts[l] +=1
        print('counts 2', counts)

        for char in t:
            if char in counts:
                counts[char] -= 1

        print('counts 3', counts)

        for v in counts.values():
            if v != 0:
                return False
        return True
    return False
# print(valid_anagram("anagram", "nagaram"))
# print(valid_anagram("rat", "car"))
# print(valid_anagram("a", "ab")) #False
# print(valid_anagram("aacc", "ccac")) #false
print(valid_anagram('', '')) #True


# Runtime is O(n)