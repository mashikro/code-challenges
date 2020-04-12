# Prompt: Given a string, find the length of the longest substring without repeating characters.

# Input: "abcabcbb"
# Output: 3 
# Explanation: The answer is "abc", with the length of 3

# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
######BRUTE FORCE########

def find_longest(s):

    if len(s) == 1:
        return 1
    max_len = 0

    for i in range(len(s)):
        current_len = 1

        substr = {s[i]}
        for j in range(i+1, len(s)):
            # print(substr)
            # print(s[j])
            if not s[j] in substr:
                substr.add(s[j])

                current_len += 1
            else:
                break
        max_len = max(max_len, current_len)


    return max_len

# print(find_longest("busvutpwmu"))#7
# print(find_longest("nfpdmpi")) #5
# print(find_longest("anviaj")) #5
# print(find_longest('bbbbb')) #1
# print(find_longest("abcabcbb")) #3
# print(find_longest("aab")) #2
# print(find_longest("dvdf"))#3
# print(find_longest(' ')) #1

#Runtime: O(n^2) time and O(k) space where k is len of set

def find_longest_substr(s):
    d = {}
    max_len = 0
    beg = 0

    for i in range(len(s)):
        print('d', d)
        print('s[i]', s[i])
        if s[i] in d:
            beg = max(beg, d[s[i]])
            print('beg', beg)

        max_len = max(max_len, (i - beg+1))
        print('max_len', max_len)

        d[s[i]] = i+1

    return max_len

print(find_longest_substr("aabaab!bb")) #3
# print(find_longest_substr("bbtablud")) #6
# print(find_longest_substr(' ')) #1
# print(find_longest_substr("busvutpwmu"))#7
# print(find_longest_substr('bbbbb')) #1
# print(find_longest_substr("abcabcbb")) #3
# print(find_longest_substr("aab")) #2
# print(find_longest_substr("dvdf"))#3
# print(find_longest_substr("anviaj")) #5
# print(find_longest_substr("nfpdmpi"))#5

#Runtime O(n) time and O(k) space k is size of dict



 def find_longest_substr2(s):
    n = len(s)
    if n < 2:
        return n
    
    d = {}
    for i in range(len(s)):
        if not s[i] in d:
            d[s[i]] = i
      

    print(d)
    max_len = 0 
    beg = 0
    substr = s[beg]
    current_len = len(substr)


    for i in range(1,len(s)):
        print('i', i)
        print('s[i]', s[i])
        print('***substr', substr)
        if s[i] in substr:
            beg = d[s[i]] + 1
            d[s[i]] = beg
            print(d)
            current_len = len(substr)
        else:
            substr = s[beg:i+1]
            current_len = len(substr)
        max_len = max(current_len, max_len)
    
    return max_len


