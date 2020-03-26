# Balanced strings are those who have equal quantity of 'L' and 'R' characters.

# Given a balanced string s split it in the maximum amount of balanced strings.

# Return the maximum amount of splitted balanced strings.

# Input: s = "RLRRLLRLRL"
# Output: 4
# Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring 
# contains same number of 'L' and 'R'.

def split_str(s):

    ret = 0
    temp = ''
    for char in s:
        temp+=char

        if len(temp)%2==0 and (temp.count('R') == temp.count('L')):
            ret+=1
            temp = ""

    return ret


print(split_str("RLRRLLRLRL")) #4
print(split_str("RLLLLRRRLR")) #3

# Runtime: O(1) space and O(n) * O(m) time = O(n) time

def split_str_faster(s):
    ret = 0
    L_count = 0
    R_count = 0

    for char in s:
        if char=='R':
            R_count+=1
        elif char=='L':
            L_count+=1

        if R_count==L_count:
            ret+=1
            L_count=0
            R_count=0
    return ret

print(split_str_faster("RLRRLLRLRL")) #4
print(split_str_faster("RLLLLRRRLR")) #3
# Runtime: O(1) space and O(n) time




