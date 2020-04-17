# Prompt: https://www.hackerrank.com/challenges/alternating-characters/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings

# Test Cases:

# Input:
# AAAA
# BBBBB
# ABABABAB
# BABABA
# AAABBB

# Output:
# 3
# 4
# 0
# 0
# 4

def find_min_deletion(s):

    ret = [s[0]]

    for letter in s:
        if ret[-1] != letter:
            ret.append(letter)

    return len(s) - len(ret)

print(find_min_deletion('AAAA')) #3
print(find_min_deletion('ABABABAB')) #0
print(find_min_deletion('AAABBB')) #4
print(find_min_deletion('AABAAB')) #2