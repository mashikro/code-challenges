# prompt: https://www.hackerrank.com/challenges/counting-valleys/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup
# input: 
# n: the number of steps Gary takes
# s: a string describing his path
# output: number of valleys 

# test case:
# 8
# UDDDUDUU -> 1

def counting_valleys(n, s): #Valley is one above sea level which is l == 0

    level = 0
    valley = 0

    for i in range(n):
        print('i', i)
        print('*****level', level)
        print('valley', valley)

        if s[i] == 'U':
            level +=1
            print('leveled up!!', level)

            if level == 0: #sea level
                valley +=1
                print('valley+++++', valley)
        else:
            level -=1

    return valley


print(counting_valleys(11, 'UDDDUDUUDUU')) #2
# print(counting_valleys(8, 'UDDDUDUU')) #1

# Runtime: O(n) time O(1) space