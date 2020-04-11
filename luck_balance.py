# Prompt: https://www.hackerrank.com/challenges/luck-balance/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=greedy-algorithms

# input:
# k - number of important contest we can lose
# contests - 2d arr where first list is amount of luck, second list contest importance

def calculate_luck(k, contests):

    L = contests[0] #amount of luck
    T = contests[1] # contest's importance rating where 1-impor. 0-unimpo
    max_luck = 0
  

    important = []
    not_important = []

    i = 0
    while i < len(L):
        if T[i] == 0: 
            not_important.append(L[i])
        if T[i] == 1 : 
            important.append(L[i]) 
        i+=1

    important.sort()

    i = len(important)-1
  
    while i >= 0:
        if k > 0:
            max_luck += important[i]
            k -=1
        elif k == 0: 
            max_luck -= important[i]
        i-=1

    max_luck+=sum(not_important)

    return max_luck

# print(calculate_luck(2, [[5,1,4], [1,1,0]])) #10
# print(calculate_luck(3, [[5,2,1,8,10,5], [1,1,1,1,0,0]])) #29 



def calculate_luck(k, contests):
    important = []
    not_important = []

    for i in range(len(contests)):
        if contests[i][1] == 1:
            important.append(contests[i][0])
        if contests[i][1] == 0:
            not_important.append(contests[i][0])

    max_luck = 0

    important.sort()

    i = len(important)-1
    while i >= 0:
        if k > 0:
            max_luck += important[i]
            k -=1
        elif k == 0: 
            max_luck -= important[i]
        i-=1

    max_luck+=sum(not_important)

    return max_luck

print(calculate_luck(2, [[5,1], [1,1], [4, 0]])) #10










