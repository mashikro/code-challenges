# Prompt: https://www.hackerrank.com/challenges/special-palindrome-again/problem



def substrCount(n, s):
    ret = 0
    for i in range(0, n):
        for j in range(i, n):
            if s[i] == s[j]: # special substring (all characters same)
                ret += 1
            else:
                # check for special with middle char s[j]
                left = s[i:j]
                k = j + len(left)
                right= s[j+1:k+1]
                if left == right:
                    ret += 1
                # always break from for loop if s[i] != s[j]
                break

    return ret

print(substrCount(5, 'asasd'))
print(substrCount(7, 'abcbaba'))
print(substrCount(4, 'aaaa'))


# returns boolean whether string s is special.
def is_special(s):
    mid_idx = -1
    if len(s) % 2 == 1: # odd number of chars
        mid_idx = len(s)//2

    for i in range(1, len(s)):
        if i != mid_idx: # skip checking the mid_idx
            if s[i] != s[0]:
                return False

    return True

# print(is_special('aaaaa'))
# print(is_special('aabaa'))
# print(is_special('aabaaa'))
# print(is_special('aba'))

def all_substrings(s):
    ret = []
    for i in range(0, len(s)):
        for j in range(i, len(s)):
            ret.append(s[i:j+1])
    return ret

#print(all_substrings("foo"))

# n = len(s)
def substrCountBrute(n, s):
    ret = 0
    for sub in all_substrings(s):
        if is_special(sub):
            ret += 1
    return ret



