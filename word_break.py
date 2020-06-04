# Given a non-empty string s and a dictionary wordDict containing a list of non-empty words,
#  determine if s can be segmented into a space-separated sequence of one or more dictionary words.

# Note:

# The same word in the dictionary may be reused multiple times in the segmentation.
# You may assume the dictionary does not contain duplicate words.

# Example 1:

# Input: s = "leetcode", wordDict = ["leet", "code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".
# Example 2:

# Input: s = "applepenapple", wordDict = ["apple", "pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
#              Note that you are allowed to reuse a dictionary word.
# Example 3:

# Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
# Output: false

def word_break_(s, word_dict):
    if len(word_dict) == 0:
        return False

    current = ""
    count = 0
    j = 0
    for i in range(len(s)):
        current+=s[i]
        # print('current:', current)
        if current in word_dict:
            if j < len(word_dict) and current == word_dict[j]:
                count +=1
                current = ""
            # else:
            #     current = ""
           
            j+=1
        

    if count >= 1:
        return True
    else:
        return False

# print(word_break("leetcode", ["leet", "code"])) #True
# print(word_break("applepenapple", ["apple", "pen"])) #True
# print(word_break("catsandog", ["cats", "dog", "sand", "and", "cat"])) #False
# # print(word_break("a", [])) #False
# print(word_break("bb", ["a","b","bbb","bbbb"])) #True

# print(word_break("cars" , ["car","ca","rs"])) #True


def word_break(s, word_dict):
   
    dp = [False]*(len(s)+1)
    dp[0] = True
    for i in range(len(s)):
        for j in range(i, len(s)):
            if dp[i] and s[i:j+1] in word_dict:
                dp[j+1] = True

    return dp[-1]

print(word_break("leetcode", ["leet", "code"])) #True
print(word_break("applepenapple", ["apple", "pen"])) #True
print(word_break("catsandog", ["cats", "dog", "sand", "and", "cat"])) #False ['cat', 'cats', 'sand', 'and', 'dog']
print(word_break("a", [])) #False
print(word_break("bb", ["a","b","bbb","bbbb"])) #True

print(word_break("cars" , ["car","ca","rs"])) #True