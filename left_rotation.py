# Prompt: https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays


def left_rotation(a, d): #a-list and d-number of rotations

    new_l = [0] * len(a)

    for i in range(len(a)): #O(n)
        new_i = i-d
        new_l[new_i] = a[i]

    return new_l

print(left_rotation([1,2,3,4,5],2))
