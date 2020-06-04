# Prompt: https://www.hackerrank.com/challenges/staircase/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign

def build_staircase(num_stairs):

    n = num_stairs - 2
    for stairs in range(1, num_stairs):
        print(' ' * n, '#' * stairs)
        n -= 1
    print('#' * num_stairs)
    
build_staircase(4)
