# Prompt: https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup&h_r=next-challenge&h_v=zen

def find_min_route(lst):

    steps = 0
    i = 0

    while i < len(lst)-1:
        steps+=1
        
        if i+2 < len(lst) and lst[i+2] == 0:
            i+=2

        elif lst[i+1] == 0:
            i+=1

    return steps


print(find_min_route([0,1,0,0,0,1,0])) #3
print(find_min_route([0,0,1,0,0,1,0])) #4
print(find_min_route([0,0,0,0,1,0])) #3
print(find_min_route([0,0,0,1,0,0])) #3

# Runtime: O(n) time and O(1) space