# Prompt: https://www.hackerrank.com/challenges/repeated-string/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

# Test Case: 
# Input: s = 'abcac' n = 10
# Output: 4

def count_repeated_str(s, n):

    if not s:
        return 0

    mul = n//len(s)
    leftover = n%len(s)

    count = s.count('a')
    print('count', count)

    if leftover > 0:
        x = s[:leftover].count('a')
        return mul*count+x
    
    return mul*count


#Runtime: O(n) time O(1) space
print(count_repeated_str('abcac',10)) #4
print(count_repeated_str('aba', 10)) #7
print(count_repeated_str('a', 100)) #100
print(count_repeated_str('', 100)) #0
print(count_repeated_str('aab', 10)) #7
print(count_repeated_str('aab', 11)) #8
print(count_repeated_str('abab', 10)) #5